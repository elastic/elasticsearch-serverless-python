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

import typing as t

from elastic_transport import HeadApiResponse, ObjectApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class ClusterClient(NamespacedClient):
    @_rewrite_parameters()
    def delete_component_template(
        self,
        *,
        name: t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Deletes a component template

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-component-template.html>`_

        :param name: Comma-separated list or wildcard expression of component template
            names used to limit the request.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path = f"/_component_template/{_quote(name)}"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    def exists_component_template(
        self,
        *,
        name: t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> HeadApiResponse:
        """
        Returns information about whether a particular component template exist

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-component-template.html>`_

        :param name: Comma-separated list of component template names used to limit the
            request. Wildcard (*) expressions are supported.
        :param local: If true, the request retrieves information from the local node
            only. Defaults to false, which means information is retrieved from the master
            node.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path = f"/_component_template/{_quote(name)}"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "HEAD", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    def get_component_template(
        self,
        *,
        name: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns one or more component templates

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-component-template.html>`_

        :param name: Comma-separated list of component template names used to limit the
            request. Wildcard (`*`) expressions are supported.
        :param flat_settings: If `true`, returns settings in flat format.
        :param include_defaults: Return all default configurations for the component
            template (default: false)
        :param local: If `true`, the request retrieves information from the local node
            only. If `false`, information is retrieved from the master node.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name not in SKIP_IN_PATH:
            __path = f"/_component_template/{_quote(name)}"
        else:
            __path = "/_component_template"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if flat_settings is not None:
            __query["flat_settings"] = flat_settings
        if human is not None:
            __query["human"] = human
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    def info(
        self,
        *,
        target: t.Union[
            t.Union[
                "t.Literal['_all', 'http', 'ingest', 'script', 'thread_pool']", str
            ],
            t.Union[
                t.List[
                    t.Union[
                        "t.Literal['_all', 'http', 'ingest', 'script', 'thread_pool']",
                        str,
                    ]
                ],
                t.Tuple[
                    t.Union[
                        "t.Literal['_all', 'http', 'ingest', 'script', 'thread_pool']",
                        str,
                    ],
                    ...,
                ],
            ],
        ],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Returns different information about the cluster.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cluster-info.html>`_

        :param target: Limits the information returned to the specific target. Supports
            a comma-separated list, such as http,ingest.
        """
        if target in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'target'")
        __path = f"/_info/{_quote(target)}"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters(
        body_fields=True,
        parameter_aliases={"_meta": "meta"},
    )
    def put_component_template(
        self,
        *,
        name: str,
        template: t.Mapping[str, t.Any],
        allow_auto_create: t.Optional[bool] = None,
        create: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        meta: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        version: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates or updates a component template

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-component-template.html>`_

        :param name: Name of the component template to create. Elasticsearch includes
            the following built-in component templates: `logs-mappings`; 'logs-settings`;
            `metrics-mappings`; `metrics-settings`;`synthetics-mapping`; `synthetics-settings`.
            Elastic Agent uses these templates to configure backing indices for its data
            streams. If you use Elastic Agent and want to overwrite one of these templates,
            set the `version` for your replacement template higher than the current version.
            If you don’t use Elastic Agent and want to disable all built-in component
            and index templates, set `stack.templates.enabled` to `false` using the cluster
            update settings API.
        :param template: The template to be applied which includes mappings, settings,
            or aliases configuration.
        :param allow_auto_create: This setting overrides the value of the `action.auto_create_index`
            cluster setting. If set to `true` in a template, then indices can be automatically
            created using that template even if auto-creation of indices is disabled
            via `actions.auto_create_index`. If set to `false` then data streams matching
            the template must always be explicitly created.
        :param create: If `true`, this request cannot replace or update existing component
            templates.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param meta: Optional user metadata about the component template. May have any
            contents. This map is not automatically generated by Elasticsearch. This
            information is stored in the cluster state, so keeping it short is preferable.
            To unset `_meta`, replace the template without specifying this information.
        :param version: Version number used to manage component templates externally.
            This number isn't automatically generated or incremented by Elasticsearch.
            To unset a version, replace the template without specifying a version.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        if template is None:
            raise ValueError("Empty value passed for parameter 'template'")
        __path = f"/_component_template/{_quote(name)}"
        __body: t.Dict[str, t.Any] = {}
        __query: t.Dict[str, t.Any] = {}
        if template is not None:
            __body["template"] = template
        if allow_auto_create is not None:
            __body["allow_auto_create"] = allow_auto_create
        if create is not None:
            __query["create"] = create
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if meta is not None:
            __body["_meta"] = meta
        if pretty is not None:
            __query["pretty"] = pretty
        if version is not None:
            __body["version"] = version
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT", __path, params=__query, headers=__headers, body=__body
        )
