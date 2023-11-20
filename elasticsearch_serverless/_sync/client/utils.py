#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import base64
import inspect
import warnings
from datetime import date, datetime
from functools import wraps
from typing import (
    TYPE_CHECKING,
    Any,
    Callable,
    Collection,
    Dict,
    List,
    Mapping,
    Optional,
    Set,
    Tuple,
    Type,
    TypeVar,
    Union,
)

from elastic_transport import HttpHeaders, NodeConfig, RequestsHttpNode
from elastic_transport.client_utils import (
    DEFAULT,
    client_meta_version,
    create_user_agent,
    parse_cloud_id,
    percent_encode,
    url_to_node_config,
)

from ..._version import __versionstr__
from ...compat import to_bytes, to_str, warn_stacklevel

if TYPE_CHECKING:
    from ._base import NamespacedClient

# parts of URL to be omitted
SKIP_IN_PATH: Collection[Any] = (None, "", b"", [], ())

# To be passed to 'client_meta_service' on the Transport
CLIENT_META_SERVICE = ("esv", client_meta_version(__versionstr__))

# Default User-Agent used by the client
USER_AGENT = create_user_agent("elasticsearch-py", __versionstr__)
ELASTIC_API_VERSION = "2023-10-31"

_TYPE_HOST = Union[str, Mapping[str, Union[str, int]], NodeConfig]

_TRANSPORT_OPTIONS = {
    "api_key",
    "http_auth",
    "request_timeout",
    "opaque_id",
    "headers",
    "ignore",
}

F = TypeVar("F", bound=Callable[..., Any])


def client_node_config(
    host: Optional[_TYPE_HOST],
    cloud_id: Optional[str],
    requests_session_auth: Optional[Any] = None,
    **kwargs: Any,
) -> NodeConfig:
    if cloud_id is not None:
        if host is not None:
            raise ValueError(
                "The 'cloud_id' and 'host' parameters are mutually exclusive"
            )
        node_config = cloud_id_to_node_config(cloud_id)
    else:
        assert host is not None
        node_config = host_to_node_config(host)

    # Remove all values which are 'DEFAULT' to avoid overwriting actual defaults.
    node_options = {k: v for k, v in kwargs.items() if v is not DEFAULT}

    # Set the 'User-Agent' default header.
    headers = HttpHeaders(node_options.pop("headers", ()))
    headers.setdefault("user-agent", USER_AGENT)
    headers.setdefault("elastic-api-version", ELASTIC_API_VERSION)

    node_options["headers"] = headers

    # If a custom Requests AuthBase is passed we set that via '_extras'.
    if requests_session_auth is not None:
        node_options.setdefault("_extras", {})[
            "requests.session.auth"
        ] = requests_session_auth

    headers = node_config.headers.copy()  # type: ignore[attr-defined]

    headers_to_add = node_options.pop("headers", ())
    if headers_to_add:
        headers.update(headers_to_add)

    headers.setdefault("user-agent", USER_AGENT)
    headers.setdefault("elastic-api-version", ELASTIC_API_VERSION)

    headers.freeze()
    node_options["headers"] = headers

    return node_config.replace(**node_options)


def host_to_node_config(host: _TYPE_HOST) -> NodeConfig:
    """Transforms the many formats of 'host' into NodeConfig"""
    if isinstance(host, NodeConfig):
        return host
    elif isinstance(host, str):
        return url_to_node_config(host, use_default_ports_for_scheme=True)
    elif isinstance(host, Mapping):
        return host_mapping_to_node_config(host)
    else:
        raise ValueError("'host' must be a URL, NodeConfig, or dictionary")


def host_mapping_to_node_config(host: Mapping[str, Union[str, int]]) -> NodeConfig:
    """Converts an old-style dictionary host specification to a NodeConfig"""

    allow_host_keys = {
        "scheme",
        "host",
        "port",
        "path_prefix",
        "url_prefix",
        "use_ssl",
    }
    disallowed_keys = set(host.keys()).difference(allow_host_keys)
    if disallowed_keys:
        bad_keys_used = "', '".join(sorted(disallowed_keys))
        allowed_keys = "', '".join(sorted(allow_host_keys))
        raise ValueError(
            f"Can't specify the options '{bad_keys_used}' via a "
            f"dictionary in 'host', only '{allowed_keys}' options "
            "are allowed"
        )

    options = dict(host)

    # Handle the deprecated option 'use_ssl'
    if "use_ssl" in options:
        use_ssl = options.pop("use_ssl")
        if not isinstance(use_ssl, bool):
            raise TypeError("'use_ssl' must be of type 'bool'")

        # Ensure the user isn't specifying scheme=http use_ssl=True or vice-versa
        if "scheme" in options and (options["scheme"] == "https") != use_ssl:
            raise ValueError(
                f"Cannot specify conflicting options 'scheme={options['scheme']}' "
                f"and 'use_ssl={use_ssl}'. Use 'scheme' only instead"
            )

        warnings.warn(
            "The 'use_ssl' option is no longer needed as specifying a 'scheme' is now required",
            category=DeprecationWarning,
            stacklevel=warn_stacklevel(),
        )
        options.setdefault("scheme", "https" if use_ssl else "http")

    # Handle the deprecated option 'url_prefix'
    if "url_prefix" in options:
        if "path_prefix" in options:
            raise ValueError(
                "Cannot specify conflicting options 'url_prefix' and "
                "'path_prefix'. Use 'path_prefix' only instead"
            )

        warnings.warn(
            "The 'url_prefix' option is deprecated in favor of 'path_prefix'",
            category=DeprecationWarning,
            stacklevel=warn_stacklevel(),
        )
        options["path_prefix"] = options.pop("url_prefix")

    return NodeConfig(**options)  # type: ignore


def cloud_id_to_node_config(cloud_id: str) -> NodeConfig:
    """Transforms an Elastic Cloud ID into a NodeConfig"""
    es_addr = parse_cloud_id(cloud_id).es_address
    if es_addr is None or not all(es_addr):
        raise ValueError("Cloud ID missing host and port information for Elasticsearch")
    host, port = es_addr
    return NodeConfig(
        scheme="https",
        host=host,
        port=port,
        http_compress=True,
    )


def _base64_auth_header(auth_value: Union[str, List[str], Tuple[str, str]]) -> str:
    """Takes either a 2-tuple or a base64-encoded string
    and returns a base64-encoded string to be used
    as an HTTP authorization header.
    """
    if isinstance(auth_value, (list, tuple)):
        return base64.b64encode(to_bytes(":".join(auth_value))).decode("ascii")
    return to_str(auth_value)


def _escape(value: Any) -> str:
    """
    Escape a single value of a URL string or a query parameter. If it is a list
    or tuple, turn it into a comma-separated string first.
    """

    # make sequences into comma-separated strings
    if isinstance(value, (list, tuple)):
        value = ",".join([_escape(item) for item in value])

    # dates and datetimes into isoformat
    elif isinstance(value, (date, datetime)):
        value = value.isoformat()

    # make bools into true/false strings
    elif isinstance(value, bool):
        value = str(value).lower()

    elif isinstance(value, bytes):
        return value.decode("utf-8", "surrogatepass")

    if not isinstance(value, str):
        return str(value)
    return value


def _quote(value: Any) -> str:
    return percent_encode(_escape(value), ",*")


def _quote_query(query: Mapping[str, Any]) -> str:
    return "&".join([f"{k}={_quote(v)}" for k, v in query.items()])


def _merge_kwargs_no_duplicates(kwargs: Dict[str, Any], values: Dict[str, Any]) -> None:
    for key, val in values.items():
        if key in kwargs:
            raise ValueError(
                f"Received multiple values for '{key}', specify parameters "
                "directly instead of using 'body' or 'params'"
            )
        kwargs[key] = val


def _rewrite_parameters(
    body_name: Optional[str] = None,
    body_fields: bool = False,
    parameter_aliases: Optional[Dict[str, str]] = None,
    ignore_deprecated_options: Optional[Set[str]] = None,
) -> Callable[[F], F]:
    def wrapper(api: F) -> F:
        @wraps(api)
        def wrapped(*args: Any, **kwargs: Any) -> Any:
            nonlocal api, body_name, body_fields

            # Let's give a nicer error message when users pass positional arguments.
            if len(args) >= 2:
                raise TypeError(
                    "Positional arguments can't be used with Elasticsearch API methods. "
                    "Instead only use keyword arguments."
                )

            # We merge 'params' first as transport options can be specified using params.
            if "params" in kwargs and (
                not ignore_deprecated_options
                or "params" not in ignore_deprecated_options
            ):
                params = kwargs.pop("params")
                if params:
                    if not hasattr(params, "items"):
                        raise ValueError(
                            "Couldn't merge 'params' with other parameters as it wasn't a mapping. "
                            "Instead of using 'params' use individual API parameters"
                        )
                    warnings.warn(
                        "The 'params' parameter is deprecated and will be removed "
                        "in a future version. Instead use individual parameters.",
                        category=DeprecationWarning,
                        stacklevel=warn_stacklevel(),
                    )
                    _merge_kwargs_no_duplicates(kwargs, params)

            maybe_transport_options = _TRANSPORT_OPTIONS.intersection(kwargs)
            if maybe_transport_options:
                transport_options = {}
                for option in maybe_transport_options:
                    if (
                        ignore_deprecated_options
                        and option in ignore_deprecated_options
                    ):
                        continue
                    try:
                        option_rename = option
                        if option == "ignore":
                            option_rename = "ignore_status"
                        transport_options[option_rename] = kwargs.pop(option)
                    except KeyError:
                        pass
                if transport_options:
                    warnings.warn(
                        "Passing transport options in the API method is deprecated. Use 'Elasticsearch.options()' instead.",
                        category=DeprecationWarning,
                        stacklevel=warn_stacklevel(),
                    )
                    client = args[0]

                    # Namespaced clients need to unwrapped.
                    namespaced_client: Optional[Type["NamespacedClient"]] = None
                    if hasattr(client, "_client"):
                        namespaced_client = type(client)
                        client = client._client

                    client = client.options(**transport_options)

                    # Re-wrap the client if we unwrapped due to being namespaced.
                    if namespaced_client is not None:
                        client = namespaced_client(client)
                    args = (client,) + args[1:]

            if "body" in kwargs and (
                not ignore_deprecated_options or "body" not in ignore_deprecated_options
            ):
                body = kwargs.pop("body")
                if body is not None:
                    if body_name:
                        if body_name in kwargs:
                            raise TypeError(
                                f"Can't use '{body_name}' and 'body' parameters together because '{body_name}' "
                                "is an alias for 'body'. Instead you should only use the "
                                f"'{body_name}' parameter. See https://github.com/elastic/elasticsearch-py/"
                                "issues/1698 for more information"
                            )

                        warnings.warn(
                            "The 'body' parameter is deprecated and will be removed "
                            f"in a future version. Instead use the '{body_name}' parameter. "
                            "See https://github.com/elastic/elasticsearch-py/issues/1698 "
                            "for more information",
                            category=DeprecationWarning,
                            stacklevel=warn_stacklevel(),
                        )
                        kwargs[body_name] = body

                    elif body_fields:
                        if not hasattr(body, "items"):
                            raise ValueError(
                                "Couldn't merge 'body' with other parameters as it wasn't a mapping. "
                                "Instead of using 'body' use individual API parameters"
                            )
                        warnings.warn(
                            "The 'body' parameter is deprecated and will be removed "
                            "in a future version. Instead use individual parameters.",
                            category=DeprecationWarning,
                            stacklevel=warn_stacklevel(),
                        )
                        _merge_kwargs_no_duplicates(kwargs, body)

            if parameter_aliases:
                for alias, rename_to in parameter_aliases.items():
                    try:
                        kwargs[rename_to] = kwargs.pop(alias)
                    except KeyError:
                        pass

            return api(*args, **kwargs)

        return wrapped  # type: ignore[return-value]

    return wrapper


def is_requests_http_auth(http_auth: Any) -> bool:
    """Detect if an http_auth value is a custom Requests auth object"""
    try:
        from requests.auth import AuthBase

        return isinstance(http_auth, AuthBase)
    except ImportError:
        pass
    return False


def is_requests_node_class(node_class: Any) -> bool:
    """Detect if 'RequestsHttpNode' would be used given the setting of 'node_class'"""
    return (
        node_class is not None
        and node_class is not DEFAULT
        and (
            node_class == "requests"
            or (
                inspect.isclass(node_class) and issubclass(node_class, RequestsHttpNode)
            )
        )
    )
