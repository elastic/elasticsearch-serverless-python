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

from elastic_transport import ObjectApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class SecurityClient(NamespacedClient):
    @_rewrite_parameters()
    def authenticate(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Enables authentication as a user and retrieve information about the authenticated
        user.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-authenticate.html>`_
        """
        __path = "/_security/_authenticate"
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
    )
    def create_api_key(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        expiration: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        name: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union["t.Literal['false', 'true', 'wait_for']", bool, str]
        ] = None,
        role_descriptors: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Creates an API key for access without requiring basic authentication.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-create-api-key.html>`_

        :param expiration: Expiration time for the API key. By default, API keys never
            expire.
        :param metadata: Arbitrary metadata that you want to associate with the API key.
            It supports nested data structure. Within the metadata object, keys beginning
            with `_` are reserved for system usage.
        :param name: Specifies the name for this API key.
        :param refresh: If `true` (the default) then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` then do nothing with refreshes.
        :param role_descriptors: An array of role descriptors for this API key. This
            parameter is optional. When it is not specified or is an empty array, then
            the API key will have a point in time snapshot of permissions of the authenticated
            user. If you supply role descriptors then the resultant permissions would
            be an intersection of API keys permissions and authenticated user’s permissions
            thereby limiting the access scope for API keys. The structure of role descriptor
            is the same as the request for create role API. For more details, see create
            or update roles API.
        """
        __path = "/_security/api_key"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expiration is not None:
            __body["expiration"] = expiration
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if metadata is not None:
            __body["metadata"] = metadata
        if name is not None:
            __body["name"] = name
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if role_descriptors is not None:
            __body["role_descriptors"] = role_descriptors
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters()
    def get_api_key(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        id: t.Optional[str] = None,
        name: t.Optional[str] = None,
        owner: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        realm_name: t.Optional[str] = None,
        username: t.Optional[str] = None,
        with_limited_by: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information for one or more API keys.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-get-api-key.html>`_

        :param id: An API key id. This parameter cannot be used with any of `name`, `realm_name`
            or `username`.
        :param name: An API key name. This parameter cannot be used with any of `id`,
            `realm_name` or `username`. It supports prefix search with wildcard.
        :param owner: A boolean flag that can be used to query API keys owned by the
            currently authenticated user. The `realm_name` or `username` parameters cannot
            be specified when this parameter is set to `true` as they are assumed to
            be the currently authenticated ones.
        :param realm_name: The name of an authentication realm. This parameter cannot
            be used with either `id` or `name` or when `owner` flag is set to `true`.
        :param username: The username of a user. This parameter cannot be used with either
            `id` or `name` or when `owner` flag is set to `true`.
        :param with_limited_by: Return the snapshot of the owner user's role descriptors
            associated with the API key. An API key's actual permission is the intersection
            of its assigned role descriptors and the owner user's role descriptors.
        """
        __path = "/_security/api_key"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if id is not None:
            __query["id"] = id
        if name is not None:
            __query["name"] = name
        if owner is not None:
            __query["owner"] = owner
        if pretty is not None:
            __query["pretty"] = pretty
        if realm_name is not None:
            __query["realm_name"] = realm_name
        if username is not None:
            __query["username"] = username
        if with_limited_by is not None:
            __query["with_limited_by"] = with_limited_by
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters(
        body_fields=True,
    )
    def has_privileges(
        self,
        *,
        user: t.Optional[str] = None,
        application: t.Optional[
            t.Union[t.List[t.Mapping[str, t.Any]], t.Tuple[t.Mapping[str, t.Any], ...]]
        ] = None,
        cluster: t.Optional[
            t.Union[
                t.List[
                    t.Union[
                        "t.Literal['all', 'cancel_task', 'create_snapshot', 'grant_api_key', 'manage', 'manage_api_key', 'manage_ccr', 'manage_enrich', 'manage_ilm', 'manage_index_templates', 'manage_ingest_pipelines', 'manage_logstash_pipelines', 'manage_ml', 'manage_oidc', 'manage_own_api_key', 'manage_pipeline', 'manage_rollup', 'manage_saml', 'manage_security', 'manage_service_account', 'manage_slm', 'manage_token', 'manage_transform', 'manage_user_profile', 'manage_watcher', 'monitor', 'monitor_ml', 'monitor_rollup', 'monitor_snapshot', 'monitor_text_structure', 'monitor_transform', 'monitor_watcher', 'read_ccr', 'read_ilm', 'read_pipeline', 'read_slm', 'transport_client']",
                        str,
                    ]
                ],
                t.Tuple[
                    t.Union[
                        "t.Literal['all', 'cancel_task', 'create_snapshot', 'grant_api_key', 'manage', 'manage_api_key', 'manage_ccr', 'manage_enrich', 'manage_ilm', 'manage_index_templates', 'manage_ingest_pipelines', 'manage_logstash_pipelines', 'manage_ml', 'manage_oidc', 'manage_own_api_key', 'manage_pipeline', 'manage_rollup', 'manage_saml', 'manage_security', 'manage_service_account', 'manage_slm', 'manage_token', 'manage_transform', 'manage_user_profile', 'manage_watcher', 'monitor', 'monitor_ml', 'monitor_rollup', 'monitor_snapshot', 'monitor_text_structure', 'monitor_transform', 'monitor_watcher', 'read_ccr', 'read_ilm', 'read_pipeline', 'read_slm', 'transport_client']",
                        str,
                    ],
                    ...,
                ],
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        index: t.Optional[
            t.Union[t.List[t.Mapping[str, t.Any]], t.Tuple[t.Mapping[str, t.Any], ...]]
        ] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Determines whether the specified user has a specified list of privileges.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-has-privileges.html>`_

        :param user: Username
        :param application:
        :param cluster: A list of the cluster privileges that you want to check.
        :param index:
        """
        if user not in SKIP_IN_PATH:
            __path = f"/_security/user/{_quote(user)}/_has_privileges"
        else:
            __path = "/_security/user/_has_privileges"
        __body: t.Dict[str, t.Any] = {}
        __query: t.Dict[str, t.Any] = {}
        if application is not None:
            __body["application"] = application
        if cluster is not None:
            __body["cluster"] = cluster
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if index is not None:
            __body["index"] = index
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters(
        body_fields=True,
    )
    def invalidate_api_key(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        id: t.Optional[str] = None,
        ids: t.Optional[t.Union[t.List[str], t.Tuple[str, ...]]] = None,
        name: t.Optional[str] = None,
        owner: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        realm_name: t.Optional[str] = None,
        username: t.Optional[str] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Invalidates one or more API keys.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-invalidate-api-key.html>`_

        :param id:
        :param ids: A list of API key ids. This parameter cannot be used with any of
            `name`, `realm_name`, or `username`.
        :param name: An API key name. This parameter cannot be used with any of `ids`,
            `realm_name` or `username`.
        :param owner: Can be used to query API keys owned by the currently authenticated
            user. The `realm_name` or `username` parameters cannot be specified when
            this parameter is set to `true` as they are assumed to be the currently authenticated
            ones.
        :param realm_name: The name of an authentication realm. This parameter cannot
            be used with either `ids` or `name`, or when `owner` flag is set to `true`.
        :param username: The username of a user. This parameter cannot be used with either
            `ids` or `name`, or when `owner` flag is set to `true`.
        """
        __path = "/_security/api_key"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if id is not None:
            __body["id"] = id
        if ids is not None:
            __body["ids"] = ids
        if name is not None:
            __body["name"] = name
        if owner is not None:
            __body["owner"] = owner
        if pretty is not None:
            __query["pretty"] = pretty
        if realm_name is not None:
            __body["realm_name"] = realm_name
        if username is not None:
            __body["username"] = username
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters(
        body_fields=True,
        parameter_aliases={"from": "from_"},
    )
    def query_api_keys(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        search_after: t.Optional[
            t.Union[
                t.List[t.Union[None, bool, float, int, str, t.Any]],
                t.Tuple[t.Union[None, bool, float, int, str, t.Any], ...],
            ]
        ] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[
            t.Union[
                t.Union[str, t.Mapping[str, t.Any]],
                t.Union[
                    t.List[t.Union[str, t.Mapping[str, t.Any]]],
                    t.Tuple[t.Union[str, t.Mapping[str, t.Any]], ...],
                ],
            ]
        ] = None,
        with_limited_by: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Retrieves information for API keys using a subset of query DSL

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-query-api-key.html>`_

        :param from_: Starting document offset. By default, you cannot page through more
            than 10,000 hits using the from and size parameters. To page through more
            hits, use the `search_after` parameter.
        :param query: A query to filter which API keys to return. The query supports
            a subset of query types, including `match_all`, `bool`, `term`, `terms`,
            `ids`, `prefix`, `wildcard`, and `range`. You can query all public information
            associated with an API key.
        :param search_after: Search after definition
        :param size: The number of hits to return. By default, you cannot page through
            more than 10,000 hits using the `from` and `size` parameters. To page through
            more hits, use the `search_after` parameter.
        :param sort: Other than `id`, all public fields of an API key are eligible for
            sorting. In addition, sort can also be applied to the `_doc` field to sort
            by index order.
        :param with_limited_by: Return the snapshot of the owner user's role descriptors
            associated with the API key. An API key's actual permission is the intersection
            of its assigned role descriptors and the owner user's role descriptors.
        """
        __path = "/_security/_query/api_key"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = {}
        # The 'sort' parameter with a colon can't be encoded to the body.
        if sort is not None and (
            (isinstance(sort, str) and ":" in sort)
            or (
                isinstance(sort, (list, tuple))
                and all(isinstance(_x, str) for _x in sort)
                and any(":" in _x for _x in sort)
            )
        ):
            __query["sort"] = sort
            sort = None
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __body["from"] = from_
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if query is not None:
            __body["query"] = query
        if search_after is not None:
            __body["search_after"] = search_after
        if size is not None:
            __body["size"] = size
        if sort is not None:
            __body["sort"] = sort
        if with_limited_by is not None:
            __query["with_limited_by"] = with_limited_by
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters(
        body_fields=True,
    )
    def update_api_key(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        human: t.Optional[bool] = None,
        metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        role_descriptors: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Updates attributes of an existing API key.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/security-api-update-api-key.html>`_

        :param id: The ID of the API key to update.
        :param metadata: Arbitrary metadata that you want to associate with the API key.
            It supports nested data structure. Within the metadata object, keys beginning
            with _ are reserved for system usage.
        :param role_descriptors: An array of role descriptors for this API key. This
            parameter is optional. When it is not specified or is an empty array, then
            the API key will have a point in time snapshot of permissions of the authenticated
            user. If you supply role descriptors then the resultant permissions would
            be an intersection of API keys permissions and authenticated user’s permissions
            thereby limiting the access scope for API keys. The structure of role descriptor
            is the same as the request for create role API. For more details, see create
            or update roles API.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path = f"/_security/api_key/{_quote(id)}"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if metadata is not None:
            __body["metadata"] = metadata
        if pretty is not None:
            __query["pretty"] = pretty
        if role_descriptors is not None:
            __body["role_descriptors"] = role_descriptors
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "PUT", __path, params=__query, headers=__headers, body=__body
        )
