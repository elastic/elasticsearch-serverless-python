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
    async def authenticate(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Authenticate a user.</p>
          <p>Authenticates a user and returns information about the authenticated user.
          Include the user information in a <a href="https://en.wikipedia.org/wiki/Basic_access_authentication">basic auth header</a>.
          A successful call returns a JSON structure that shows user information such as their username, the roles that are assigned to the user, any assigned metadata, and information about the realms that authenticated and authorized the user.
          If the user cannot be authenticated, this API returns a 401 status code.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-authenticate>`_
        """
        __path_parts: t.Dict[str, str] = {}
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
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="security.authenticate",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("expiration", "metadata", "name", "role_descriptors"),
    )
    async def create_api_key(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        expiration: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        name: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union[bool, str, t.Literal["false", "true", "wait_for"]]
        ] = None,
        role_descriptors: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create an API key.</p>
          <p>Create an API key for access without requiring basic authentication.</p>
          <p>IMPORTANT: If the credential that is used to authenticate this request is an API key, the derived API key cannot have any privileges.
          If you specify privileges, the API returns an error.</p>
          <p>A successful request returns a JSON structure that contains the API key, its unique id, and its name.
          If applicable, it also returns expiration information for the API key in milliseconds.</p>
          <p>NOTE: By default, API keys never expire. You can specify expiration information when you create the API keys.</p>
          <p>The API keys are created by the Elasticsearch API key service, which is automatically enabled.
          To configure or turn off the API key service, refer to API key service setting documentation.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-create-api-key>`_

        :param expiration: The expiration time for the API key. By default, API keys
            never expire.
        :param metadata: Arbitrary metadata that you want to associate with the API key.
            It supports nested data structure. Within the metadata object, keys beginning
            with `_` are reserved for system usage.
        :param name: A name for the API key.
        :param refresh: If `true` (the default) then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` then do nothing with refreshes.
        :param role_descriptors: An array of role descriptors for this API key. When
            it is not specified or it is an empty array, the API key will have a point
            in time snapshot of permissions of the authenticated user. If you supply
            role descriptors, the resultant permissions are an intersection of API keys
            permissions and the authenticated user's permissions thereby limiting the
            access scope for API keys. The structure of role descriptor is the same as
            the request for the create role API. For more details, refer to the create
            or update roles API. NOTE: Due to the way in which this permission intersection
            is calculated, it is not possible to create an API key that is a child of
            another API key, unless the derived key is created without any privileges.
            In this case, you must explicitly specify a role descriptor with no privileges.
            The derived API key can be used for authentication; it will not have authority
            to call Elasticsearch APIs.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_security/api_key"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if not __body:
            if expiration is not None:
                __body["expiration"] = expiration
            if metadata is not None:
                __body["metadata"] = metadata
            if name is not None:
                __body["name"] = name
            if role_descriptors is not None:
                __body["role_descriptors"] = role_descriptors
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.create_api_key",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete_role(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union[bool, str, t.Literal["false", "true", "wait_for"]]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete roles.</p>
          <p>Delete roles in the native realm.
          The role management APIs are generally the preferred way to manage roles, rather than using file-based role management.
          The delete roles API cannot remove roles that are defined in roles files.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-delete-role>`_

        :param name: The name of the role.
        :param refresh: If `true` (the default) then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` then do nothing with refreshes.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_security/role/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="security.delete_role",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_api_key(
        self,
        *,
        active_only: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        id: t.Optional[str] = None,
        name: t.Optional[str] = None,
        owner: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        realm_name: t.Optional[str] = None,
        username: t.Optional[str] = None,
        with_limited_by: t.Optional[bool] = None,
        with_profile_uid: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get API key information.</p>
          <p>Retrieves information for one or more API keys.
          NOTE: If you have only the <code>manage_own_api_key</code> privilege, this API returns only the API keys that you own.
          If you have <code>read_security</code>, <code>manage_api_key</code> or greater privileges (including <code>manage_security</code>), this API returns all API keys regardless of ownership.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-get-api-key>`_

        :param active_only: A boolean flag that can be used to query API keys that are
            currently active. An API key is considered active if it is neither invalidated,
            nor expired at query time. You can specify this together with other parameters
            such as `owner` or `name`. If `active_only` is false, the response will include
            both active and inactive (expired or invalidated) keys.
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
        :param with_profile_uid: Determines whether to also retrieve the profile uid,
            for the API key owner principal, if it exists.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_security/api_key"
        __query: t.Dict[str, t.Any] = {}
        if active_only is not None:
            __query["active_only"] = active_only
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
        if with_profile_uid is not None:
            __query["with_profile_uid"] = with_profile_uid
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="security.get_api_key",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_builtin_privileges(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get builtin privileges.</p>
          <p>Get the list of cluster privileges and index privileges that are available in this version of Elasticsearch.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-get-builtin-privileges>`_
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_security/privilege/_builtin"
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
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="security.get_builtin_privileges",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_role(
        self,
        *,
        name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get roles.</p>
          <p>Get roles in the native realm.
          The role management APIs are generally the preferred way to manage roles, rather than using file-based role management.
          The get roles API cannot retrieve roles that are defined in roles files.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-get-role>`_

        :param name: The name of the role. You can specify multiple roles as a comma-separated
            list. If you do not specify this parameter, the API returns information about
            all roles.
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_security/role/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_security/role"
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
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="security.get_role",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("application", "cluster", "index"),
    )
    async def has_privileges(
        self,
        *,
        user: t.Optional[str] = None,
        application: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        cluster: t.Optional[
            t.Sequence[
                t.Union[
                    str,
                    t.Literal[
                        "all",
                        "cancel_task",
                        "create_snapshot",
                        "cross_cluster_replication",
                        "cross_cluster_search",
                        "delegate_pki",
                        "grant_api_key",
                        "manage",
                        "manage_api_key",
                        "manage_autoscaling",
                        "manage_behavioral_analytics",
                        "manage_ccr",
                        "manage_data_frame_transforms",
                        "manage_data_stream_global_retention",
                        "manage_enrich",
                        "manage_ilm",
                        "manage_index_templates",
                        "manage_inference",
                        "manage_ingest_pipelines",
                        "manage_logstash_pipelines",
                        "manage_ml",
                        "manage_oidc",
                        "manage_own_api_key",
                        "manage_pipeline",
                        "manage_rollup",
                        "manage_saml",
                        "manage_search_application",
                        "manage_search_query_rules",
                        "manage_search_synonyms",
                        "manage_security",
                        "manage_service_account",
                        "manage_slm",
                        "manage_token",
                        "manage_transform",
                        "manage_user_profile",
                        "manage_watcher",
                        "monitor",
                        "monitor_data_frame_transforms",
                        "monitor_data_stream_global_retention",
                        "monitor_enrich",
                        "monitor_inference",
                        "monitor_ml",
                        "monitor_rollup",
                        "monitor_snapshot",
                        "monitor_stats",
                        "monitor_text_structure",
                        "monitor_transform",
                        "monitor_watcher",
                        "none",
                        "post_behavioral_analytics_event",
                        "read_ccr",
                        "read_fleet_secrets",
                        "read_ilm",
                        "read_pipeline",
                        "read_security",
                        "read_slm",
                        "transport_client",
                        "write_connector_secrets",
                        "write_fleet_secrets",
                    ],
                ]
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        index: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Check user privileges.</p>
          <p>Determine whether the specified user has a specified list of privileges.
          All users can use this API, but only to determine their own privileges.
          To check the privileges of other users, you must use the run as feature.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-has-privileges>`_

        :param user: Username
        :param application:
        :param cluster: A list of the cluster privileges that you want to check.
        :param index:
        """
        __path_parts: t.Dict[str, str]
        if user not in SKIP_IN_PATH:
            __path_parts = {"user": _quote(user)}
            __path = f'/_security/user/{__path_parts["user"]}/_has_privileges'
        else:
            __path_parts = {}
            __path = "/_security/user/_has_privileges"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if application is not None:
                __body["application"] = application
            if cluster is not None:
                __body["cluster"] = cluster
            if index is not None:
                __body["index"] = index
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.has_privileges",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("id", "ids", "name", "owner", "realm_name", "username"),
    )
    async def invalidate_api_key(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        id: t.Optional[str] = None,
        ids: t.Optional[t.Sequence[str]] = None,
        name: t.Optional[str] = None,
        owner: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        realm_name: t.Optional[str] = None,
        username: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Invalidate API keys.</p>
          <p>This API invalidates API keys created by the create API key or grant API key APIs.
          Invalidated API keys fail authentication, but they can still be viewed using the get API key information and query API key information APIs, for at least the configured retention period, until they are automatically deleted.</p>
          <p>To use this API, you must have at least the <code>manage_security</code>, <code>manage_api_key</code>, or <code>manage_own_api_key</code> cluster privileges.
          The <code>manage_security</code> privilege allows deleting any API key, including both REST and cross cluster API keys.
          The <code>manage_api_key</code> privilege allows deleting any REST API key, but not cross cluster API keys.
          The <code>manage_own_api_key</code> only allows deleting REST API keys that are owned by the user.
          In addition, with the <code>manage_own_api_key</code> privilege, an invalidation request must be issued in one of the three formats:</p>
          <ul>
          <li>Set the parameter <code>owner=true</code>.</li>
          <li>Or, set both <code>username</code> and <code>realm_name</code> to match the user's identity.</li>
          <li>Or, if the request is issued by an API key, that is to say an API key invalidates itself, specify its ID in the <code>ids</code> field.</li>
          </ul>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-invalidate-api-key>`_

        :param id:
        :param ids: A list of API key ids. This parameter cannot be used with any of
            `name`, `realm_name`, or `username`.
        :param name: An API key name. This parameter cannot be used with any of `ids`,
            `realm_name` or `username`.
        :param owner: Query API keys owned by the currently authenticated user. The `realm_name`
            or `username` parameters cannot be specified when this parameter is set to
            `true` as they are assumed to be the currently authenticated ones. NOTE:
            At least one of `ids`, `name`, `username`, and `realm_name` must be specified
            if `owner` is `false`.
        :param realm_name: The name of an authentication realm. This parameter cannot
            be used with either `ids` or `name`, or when `owner` flag is set to `true`.
        :param username: The username of a user. This parameter cannot be used with either
            `ids` or `name` or when `owner` flag is set to `true`.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_security/api_key"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if id is not None:
                __body["id"] = id
            if ids is not None:
                __body["ids"] = ids
            if name is not None:
                __body["name"] = name
            if owner is not None:
                __body["owner"] = owner
            if realm_name is not None:
                __body["realm_name"] = realm_name
            if username is not None:
                __body["username"] = username
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.invalidate_api_key",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "applications",
            "cluster",
            "description",
            "global_",
            "indices",
            "metadata",
            "remote_cluster",
            "remote_indices",
            "run_as",
            "transient_metadata",
        ),
        parameter_aliases={"global": "global_"},
    )
    async def put_role(
        self,
        *,
        name: str,
        applications: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        cluster: t.Optional[
            t.Sequence[
                t.Union[
                    str,
                    t.Literal[
                        "all",
                        "cancel_task",
                        "create_snapshot",
                        "cross_cluster_replication",
                        "cross_cluster_search",
                        "delegate_pki",
                        "grant_api_key",
                        "manage",
                        "manage_api_key",
                        "manage_autoscaling",
                        "manage_behavioral_analytics",
                        "manage_ccr",
                        "manage_data_frame_transforms",
                        "manage_data_stream_global_retention",
                        "manage_enrich",
                        "manage_ilm",
                        "manage_index_templates",
                        "manage_inference",
                        "manage_ingest_pipelines",
                        "manage_logstash_pipelines",
                        "manage_ml",
                        "manage_oidc",
                        "manage_own_api_key",
                        "manage_pipeline",
                        "manage_rollup",
                        "manage_saml",
                        "manage_search_application",
                        "manage_search_query_rules",
                        "manage_search_synonyms",
                        "manage_security",
                        "manage_service_account",
                        "manage_slm",
                        "manage_token",
                        "manage_transform",
                        "manage_user_profile",
                        "manage_watcher",
                        "monitor",
                        "monitor_data_frame_transforms",
                        "monitor_data_stream_global_retention",
                        "monitor_enrich",
                        "monitor_inference",
                        "monitor_ml",
                        "monitor_rollup",
                        "monitor_snapshot",
                        "monitor_stats",
                        "monitor_text_structure",
                        "monitor_transform",
                        "monitor_watcher",
                        "none",
                        "post_behavioral_analytics_event",
                        "read_ccr",
                        "read_fleet_secrets",
                        "read_ilm",
                        "read_pipeline",
                        "read_security",
                        "read_slm",
                        "transport_client",
                        "write_connector_secrets",
                        "write_fleet_secrets",
                    ],
                ]
            ]
        ] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        global_: t.Optional[t.Mapping[str, t.Any]] = None,
        human: t.Optional[bool] = None,
        indices: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        refresh: t.Optional[
            t.Union[bool, str, t.Literal["false", "true", "wait_for"]]
        ] = None,
        remote_cluster: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        remote_indices: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        run_as: t.Optional[t.Sequence[str]] = None,
        transient_metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create or update roles.</p>
          <p>The role management APIs are generally the preferred way to manage roles in the native realm, rather than using file-based role management.
          The create or update roles API cannot update roles that are defined in roles files.
          File-based role management is not available in Elastic Serverless.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-put-role>`_

        :param name: The name of the role that is being created or updated. On Elasticsearch
            Serverless, the role name must begin with a letter or digit and can only
            contain letters, digits and the characters '_', '-', and '.'. Each role must
            have a unique name, as this will serve as the identifier for that role.
        :param applications: A list of application privilege entries.
        :param cluster: A list of cluster privileges. These privileges define the cluster-level
            actions for users with this role.
        :param description: Optional description of the role descriptor
        :param global_: An object defining global privileges. A global privilege is a
            form of cluster privilege that is request-aware. Support for global privileges
            is currently limited to the management of application privileges.
        :param indices: A list of indices permissions entries.
        :param metadata: Optional metadata. Within the metadata object, keys that begin
            with an underscore (`_`) are reserved for system use.
        :param refresh: If `true` (the default) then refresh the affected shards to make
            this operation visible to search, if `wait_for` then wait for a refresh to
            make this operation visible to search, if `false` then do nothing with refreshes.
        :param remote_cluster: A list of remote cluster permissions entries.
        :param remote_indices: A list of remote indices permissions entries. NOTE: Remote
            indices are effective for remote clusters configured with the API key based
            model. They have no effect for remote clusters configured with the certificate
            based model.
        :param run_as: A list of users that the owners of this role can impersonate.
            *Note*: in Serverless, the run-as feature is disabled. For API compatibility,
            you can still specify an empty `run_as` field, but a non-empty list will
            be rejected.
        :param transient_metadata: Indicates roles that might be incompatible with the
            current cluster license, specifically roles with document and field level
            security. When the cluster license doesn’t allow certain features for a given
            role, this parameter is updated dynamically to list the incompatible features.
            If `enabled` is `false`, the role is ignored, but is still listed in the
            response from the authenticate API.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_security/role/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if refresh is not None:
            __query["refresh"] = refresh
        if not __body:
            if applications is not None:
                __body["applications"] = applications
            if cluster is not None:
                __body["cluster"] = cluster
            if description is not None:
                __body["description"] = description
            if global_ is not None:
                __body["global"] = global_
            if indices is not None:
                __body["indices"] = indices
            if metadata is not None:
                __body["metadata"] = metadata
            if remote_cluster is not None:
                __body["remote_cluster"] = remote_cluster
            if remote_indices is not None:
                __body["remote_indices"] = remote_indices
            if run_as is not None:
                __body["run_as"] = run_as
            if transient_metadata is not None:
                __body["transient_metadata"] = transient_metadata
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.put_role",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "aggregations",
            "aggs",
            "from_",
            "query",
            "search_after",
            "size",
            "sort",
        ),
        parameter_aliases={"from": "from_"},
    )
    async def query_api_keys(
        self,
        *,
        aggregations: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        aggs: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        search_after: t.Optional[
            t.Sequence[t.Union[None, bool, float, int, str]]
        ] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[
            t.Union[
                t.Sequence[t.Union[str, t.Mapping[str, t.Any]]],
                t.Union[str, t.Mapping[str, t.Any]],
            ]
        ] = None,
        typed_keys: t.Optional[bool] = None,
        with_limited_by: t.Optional[bool] = None,
        with_profile_uid: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Find API keys with a query.</p>
          <p>Get a paginated list of API keys and their information.
          You can optionally filter the results with a query.</p>
          <p>To use this API, you must have at least the <code>manage_own_api_key</code> or the <code>read_security</code> cluster privileges.
          If you have only the <code>manage_own_api_key</code> privilege, this API returns only the API keys that you own.
          If you have the <code>read_security</code>, <code>manage_api_key</code>, or greater privileges (including <code>manage_security</code>), this API returns all API keys regardless of ownership.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-query-api-keys>`_

        :param aggregations: Any aggregations to run over the corpus of returned API
            keys. Aggregations and queries work together. Aggregations are computed only
            on the API keys that match the query. This supports only a subset of aggregation
            types, namely: `terms`, `range`, `date_range`, `missing`, `cardinality`,
            `value_count`, `composite`, `filter`, and `filters`. Additionally, aggregations
            only run over the same subset of fields that query works with.
        :param aggs: Any aggregations to run over the corpus of returned API keys. Aggregations
            and queries work together. Aggregations are computed only on the API keys
            that match the query. This supports only a subset of aggregation types, namely:
            `terms`, `range`, `date_range`, `missing`, `cardinality`, `value_count`,
            `composite`, `filter`, and `filters`. Additionally, aggregations only run
            over the same subset of fields that query works with.
        :param from_: The starting document offset. It must not be negative. By default,
            you cannot page through more than 10,000 hits using the `from` and `size`
            parameters. To page through more hits, use the `search_after` parameter.
        :param query: A query to filter which API keys to return. If the query parameter
            is missing, it is equivalent to a `match_all` query. The query supports a
            subset of query types, including `match_all`, `bool`, `term`, `terms`, `match`,
            `ids`, `prefix`, `wildcard`, `exists`, `range`, and `simple_query_string`.
            You can query the following public information associated with an API key:
            `id`, `type`, `name`, `creation`, `expiration`, `invalidated`, `invalidation`,
            `username`, `realm`, and `metadata`. NOTE: The queryable string values associated
            with API keys are internally mapped as keywords. Consequently, if no `analyzer`
            parameter is specified for a `match` query, then the provided match query
            string is interpreted as a single keyword value. Such a match query is hence
            equivalent to a `term` query.
        :param search_after: The search after definition.
        :param size: The number of hits to return. It must not be negative. The `size`
            parameter can be set to `0`, in which case no API key matches are returned,
            only the aggregation results. By default, you cannot page through more than
            10,000 hits using the `from` and `size` parameters. To page through more
            hits, use the `search_after` parameter.
        :param sort: The sort definition. Other than `id`, all public fields of an API
            key are eligible for sorting. In addition, sort can also be applied to the
            `_doc` field to sort by index order.
        :param typed_keys: Determines whether aggregation names are prefixed by their
            respective types in the response.
        :param with_limited_by: Return the snapshot of the owner user's role descriptors
            associated with the API key. An API key's actual permission is the intersection
            of its assigned role descriptors and the owner user's role descriptors (effectively
            limited by it). An API key cannot retrieve any API key’s limited-by role
            descriptors (including itself) unless it has `manage_api_key` or higher privileges.
        :param with_profile_uid: Determines whether to also retrieve the profile UID
            for the API key owner principal. If it exists, the profile UID is returned
            under the `profile_uid` response field for each API key.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_security/_query/api_key"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
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
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if typed_keys is not None:
            __query["typed_keys"] = typed_keys
        if with_limited_by is not None:
            __query["with_limited_by"] = with_limited_by
        if with_profile_uid is not None:
            __query["with_profile_uid"] = with_profile_uid
        if not __body:
            if aggregations is not None:
                __body["aggregations"] = aggregations
            if aggs is not None:
                __body["aggs"] = aggs
            if from_ is not None:
                __body["from"] = from_
            if query is not None:
                __body["query"] = query
            if search_after is not None:
                __body["search_after"] = search_after
            if size is not None:
                __body["size"] = size
            if sort is not None:
                __body["sort"] = sort
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.query_api_keys",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("from_", "query", "search_after", "size", "sort"),
        parameter_aliases={"from": "from_"},
    )
    async def query_role(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        search_after: t.Optional[
            t.Sequence[t.Union[None, bool, float, int, str]]
        ] = None,
        size: t.Optional[int] = None,
        sort: t.Optional[
            t.Union[
                t.Sequence[t.Union[str, t.Mapping[str, t.Any]]],
                t.Union[str, t.Mapping[str, t.Any]],
            ]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Find roles with a query.</p>
          <p>Get roles in a paginated manner.
          The role management APIs are generally the preferred way to manage roles, rather than using file-based role management.
          The query roles API does not retrieve roles that are defined in roles files, nor built-in ones.
          You can optionally filter the results with a query.
          Also, the results can be paginated and sorted.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-query-role>`_

        :param from_: The starting document offset. It must not be negative. By default,
            you cannot page through more than 10,000 hits using the `from` and `size`
            parameters. To page through more hits, use the `search_after` parameter.
        :param query: A query to filter which roles to return. If the query parameter
            is missing, it is equivalent to a `match_all` query. The query supports a
            subset of query types, including `match_all`, `bool`, `term`, `terms`, `match`,
            `ids`, `prefix`, `wildcard`, `exists`, `range`, and `simple_query_string`.
            You can query the following information associated with roles: `name`, `description`,
            `metadata`, `applications.application`, `applications.privileges`, and `applications.resources`.
        :param search_after: The search after definition.
        :param size: The number of hits to return. It must not be negative. By default,
            you cannot page through more than 10,000 hits using the `from` and `size`
            parameters. To page through more hits, use the `search_after` parameter.
        :param sort: The sort definition. You can sort on `username`, `roles`, or `enabled`.
            In addition, sort can also be applied to the `_doc` field to sort by index
            order.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_security/_query/role"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if from_ is not None:
                __body["from"] = from_
            if query is not None:
                __body["query"] = query
            if search_after is not None:
                __body["search_after"] = search_after
            if size is not None:
                __body["size"] = size
            if sort is not None:
                __body["sort"] = sort
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.query_role",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("expiration", "metadata", "role_descriptors"),
    )
    async def update_api_key(
        self,
        *,
        id: str,
        error_trace: t.Optional[bool] = None,
        expiration: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        metadata: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        role_descriptors: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update an API key.</p>
          <p>Update attributes of an existing API key.
          This API supports updates to an API key's access scope, expiration, and metadata.</p>
          <p>To use this API, you must have at least the <code>manage_own_api_key</code> cluster privilege.
          Users can only update API keys that they created or that were granted to them.
          To update another user’s API key, use the <code>run_as</code> feature to submit a request on behalf of another user.</p>
          <p>IMPORTANT: It's not possible to use an API key as the authentication credential for this API. The owner user’s credentials are required.</p>
          <p>Use this API to update API keys created by the create API key or grant API Key APIs.
          If you need to apply the same update to many API keys, you can use the bulk update API keys API to reduce overhead.
          It's not possible to update expired API keys or API keys that have been invalidated by the invalidate API key API.</p>
          <p>The access scope of an API key is derived from the <code>role_descriptors</code> you specify in the request and a snapshot of the owner user's permissions at the time of the request.
          The snapshot of the owner's permissions is updated automatically on every call.</p>
          <p>IMPORTANT: If you don't specify <code>role_descriptors</code> in the request, a call to this API might still change the API key's access scope.
          This change can occur if the owner user's permissions have changed since the API key was created or last modified.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-security-update-api-key>`_

        :param id: The ID of the API key to update.
        :param expiration: The expiration time for the API key. By default, API keys
            never expire. This property can be omitted to leave the expiration unchanged.
        :param metadata: Arbitrary metadata that you want to associate with the API key.
            It supports a nested data structure. Within the metadata object, keys beginning
            with `_` are reserved for system usage. When specified, this value fully
            replaces the metadata previously associated with the API key.
        :param role_descriptors: The role descriptors to assign to this API key. The
            API key's effective permissions are an intersection of its assigned privileges
            and the point in time snapshot of permissions of the owner user. You can
            assign new privileges by specifying them in this parameter. To remove assigned
            privileges, you can supply an empty `role_descriptors` parameter, that is
            to say, an empty object `{}`. If an API key has no assigned privileges, it
            inherits the owner user's full permissions. The snapshot of the owner's permissions
            is always updated, whether you supply the `role_descriptors` parameter or
            not. The structure of a role descriptor is the same as the request for the
            create API keys API.
        """
        if id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {"id": _quote(id)}
        __path = f'/_security/api_key/{__path_parts["id"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if expiration is not None:
                __body["expiration"] = expiration
            if metadata is not None:
                __body["metadata"] = metadata
            if role_descriptors is not None:
                __body["role_descriptors"] = role_descriptors
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="security.update_api_key",
            path_parts=__path_parts,
        )
