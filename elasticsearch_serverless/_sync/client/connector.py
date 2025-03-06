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
from .utils import (
    SKIP_IN_PATH,
    Stability,
    _quote,
    _rewrite_parameters,
    _stability_warning,
)


class ConnectorClient(NamespacedClient):

    @_rewrite_parameters()
    @_stability_warning(Stability.EXPERIMENTAL)
    def check_in(
        self,
        *,
        connector_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Check in a connector.</p>
          <p>Update the <code>last_seen</code> field in the connector and set it to the current timestamp.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-check-in>`_

        :param connector_id: The unique identifier of the connector to be checked in
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_check_in'
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
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.check_in",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    @_stability_warning(Stability.BETA)
    def delete(
        self,
        *,
        connector_id: str,
        delete_sync_jobs: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        hard: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete a connector.</p>
          <p>Removes a connector and associated sync jobs.
          This is a destructive action that is not recoverable.
          NOTE: This action doesn’t delete any API keys, ingest pipelines, or data indices associated with the connector.
          These need to be removed manually.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-delete>`_

        :param connector_id: The unique identifier of the connector to be deleted
        :param delete_sync_jobs: A flag indicating if associated sync jobs should be
            also removed. Defaults to false.
        :param hard: A flag indicating if the connector should be hard deleted.
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if delete_sync_jobs is not None:
            __query["delete_sync_jobs"] = delete_sync_jobs
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if hard is not None:
            __query["hard"] = hard
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    @_stability_warning(Stability.BETA)
    def get(
        self,
        *,
        connector_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        include_deleted: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get a connector.</p>
          <p>Get the details about a connector.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-get>`_

        :param connector_id: The unique identifier of the connector
        :param include_deleted: A flag to indicate if the desired connector should be
            fetched, even if it was soft-deleted.
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if include_deleted is not None:
            __query["include_deleted"] = include_deleted
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    @_stability_warning(Stability.BETA)
    def list(
        self,
        *,
        connector_name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        include_deleted: t.Optional[bool] = None,
        index_name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[str] = None,
        service_type: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        size: t.Optional[int] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get all connectors.</p>
          <p>Get information about all connectors.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-list>`_

        :param connector_name: A comma-separated list of connector names to fetch connector
            documents for
        :param from_: Starting offset (default: 0)
        :param include_deleted: A flag to indicate if the desired connector should be
            fetched, even if it was soft-deleted.
        :param index_name: A comma-separated list of connector index names to fetch connector
            documents for
        :param query: A wildcard query string that filters connectors with matching name,
            description or index name
        :param service_type: A comma-separated list of connector service types to fetch
            connector documents for
        :param size: Specifies a max number of results to get
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_connector"
        __query: t.Dict[str, t.Any] = {}
        if connector_name is not None:
            __query["connector_name"] = connector_name
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if include_deleted is not None:
            __query["include_deleted"] = include_deleted
        if index_name is not None:
            __query["index_name"] = index_name
        if pretty is not None:
            __query["pretty"] = pretty
        if query is not None:
            __query["query"] = query
        if service_type is not None:
            __query["service_type"] = service_type
        if size is not None:
            __query["size"] = size
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.list",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "description",
            "index_name",
            "is_native",
            "language",
            "name",
            "service_type",
        ),
    )
    @_stability_warning(Stability.BETA)
    def post(
        self,
        *,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        index_name: t.Optional[str] = None,
        is_native: t.Optional[bool] = None,
        language: t.Optional[str] = None,
        name: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        service_type: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create a connector.</p>
          <p>Connectors are Elasticsearch integrations that bring content from third-party data sources, which can be deployed on Elastic Cloud or hosted on your own infrastructure.
          Elastic managed connectors (Native connectors) are a managed service on Elastic Cloud.
          Self-managed connectors (Connector clients) are self-managed on your infrastructure.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-put>`_

        :param description:
        :param index_name:
        :param is_native:
        :param language:
        :param name:
        :param service_type:
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_connector"
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
            if description is not None:
                __body["description"] = description
            if index_name is not None:
                __body["index_name"] = index_name
            if is_native is not None:
                __body["is_native"] = is_native
            if language is not None:
                __body["language"] = language
            if name is not None:
                __body["name"] = name
            if service_type is not None:
                __body["service_type"] = service_type
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.post",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "description",
            "index_name",
            "is_native",
            "language",
            "name",
            "service_type",
        ),
    )
    @_stability_warning(Stability.BETA)
    def put(
        self,
        *,
        connector_id: t.Optional[str] = None,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        index_name: t.Optional[str] = None,
        is_native: t.Optional[bool] = None,
        language: t.Optional[str] = None,
        name: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        service_type: t.Optional[str] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create or update a connector.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-put>`_

        :param connector_id: The unique identifier of the connector to be created or
            updated. ID is auto-generated if not provided.
        :param description:
        :param index_name:
        :param is_native:
        :param language:
        :param name:
        :param service_type:
        """
        __path_parts: t.Dict[str, str]
        if connector_id not in SKIP_IN_PATH:
            __path_parts = {"connector_id": _quote(connector_id)}
            __path = f'/_connector/{__path_parts["connector_id"]}'
        else:
            __path_parts = {}
            __path = "/_connector"
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
            if description is not None:
                __body["description"] = description
            if index_name is not None:
                __body["index_name"] = index_name
            if is_native is not None:
                __body["is_native"] = is_native
            if language is not None:
                __body["language"] = language
            if name is not None:
                __body["name"] = name
            if service_type is not None:
                __body["service_type"] = service_type
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.put",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    @_stability_warning(Stability.BETA)
    def sync_job_cancel(
        self,
        *,
        connector_sync_job_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Cancel a connector sync job.</p>
          <p>Cancel a connector sync job, which sets the status to cancelling and updates <code>cancellation_requested_at</code> to the current time.
          The connector service is then responsible for setting the status of connector sync jobs to cancelled.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-cancel>`_

        :param connector_sync_job_id: The unique identifier of the connector sync job
        """
        if connector_sync_job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_sync_job_id'")
        __path_parts: t.Dict[str, str] = {
            "connector_sync_job_id": _quote(connector_sync_job_id)
        }
        __path = (
            f'/_connector/_sync_job/{__path_parts["connector_sync_job_id"]}/_cancel'
        )
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
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.sync_job_cancel",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    @_stability_warning(Stability.BETA)
    def sync_job_delete(
        self,
        *,
        connector_sync_job_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete a connector sync job.</p>
          <p>Remove a connector sync job and its associated data.
          This is a destructive action that is not recoverable.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-delete>`_

        :param connector_sync_job_id: The unique identifier of the connector sync job
            to be deleted
        """
        if connector_sync_job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_sync_job_id'")
        __path_parts: t.Dict[str, str] = {
            "connector_sync_job_id": _quote(connector_sync_job_id)
        }
        __path = f'/_connector/_sync_job/{__path_parts["connector_sync_job_id"]}'
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
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.sync_job_delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    @_stability_warning(Stability.BETA)
    def sync_job_get(
        self,
        *,
        connector_sync_job_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get a connector sync job.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-get>`_

        :param connector_sync_job_id: The unique identifier of the connector sync job
        """
        if connector_sync_job_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_sync_job_id'")
        __path_parts: t.Dict[str, str] = {
            "connector_sync_job_id": _quote(connector_sync_job_id)
        }
        __path = f'/_connector/_sync_job/{__path_parts["connector_sync_job_id"]}'
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
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.sync_job_get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    @_stability_warning(Stability.BETA)
    def sync_job_list(
        self,
        *,
        connector_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        from_: t.Optional[int] = None,
        human: t.Optional[bool] = None,
        job_type: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["access_control", "full", "incremental"]]
                ],
                t.Union[str, t.Literal["access_control", "full", "incremental"]],
            ]
        ] = None,
        pretty: t.Optional[bool] = None,
        size: t.Optional[int] = None,
        status: t.Optional[
            t.Union[
                str,
                t.Literal[
                    "canceled",
                    "canceling",
                    "completed",
                    "error",
                    "in_progress",
                    "pending",
                    "suspended",
                ],
            ]
        ] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get all connector sync jobs.</p>
          <p>Get information about all stored connector sync jobs listed by their creation date in ascending order.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-list>`_

        :param connector_id: A connector id to fetch connector sync jobs for
        :param from_: Starting offset (default: 0)
        :param job_type: A comma-separated list of job types to fetch the sync jobs for
        :param size: Specifies a max number of results to get
        :param status: A sync job status to fetch connector sync jobs for
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_connector/_sync_job"
        __query: t.Dict[str, t.Any] = {}
        if connector_id is not None:
            __query["connector_id"] = connector_id
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if from_ is not None:
            __query["from"] = from_
        if human is not None:
            __query["human"] = human
        if job_type is not None:
            __query["job_type"] = job_type
        if pretty is not None:
            __query["pretty"] = pretty
        if size is not None:
            __query["size"] = size
        if status is not None:
            __query["status"] = status
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.sync_job_list",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("id", "job_type", "trigger_method"),
    )
    @_stability_warning(Stability.BETA)
    def sync_job_post(
        self,
        *,
        id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        job_type: t.Optional[
            t.Union[str, t.Literal["access_control", "full", "incremental"]]
        ] = None,
        pretty: t.Optional[bool] = None,
        trigger_method: t.Optional[
            t.Union[str, t.Literal["on_demand", "scheduled"]]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create a connector sync job.</p>
          <p>Create a connector sync job document in the internal index and initialize its counters and timestamps with default values.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-sync-job-post>`_

        :param id: The id of the associated connector
        :param job_type:
        :param trigger_method:
        """
        if id is None and body is None:
            raise ValueError("Empty value passed for parameter 'id'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_connector/_sync_job"
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
            if job_type is not None:
                __body["job_type"] = job_type
            if trigger_method is not None:
                __body["trigger_method"] = trigger_method
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.sync_job_post",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    @_stability_warning(Stability.EXPERIMENTAL)
    def update_active_filtering(
        self,
        *,
        connector_id: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Activate the connector draft filter.</p>
          <p>Activates the valid draft filtering for a connector.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-filtering>`_

        :param connector_id: The unique identifier of the connector to be updated
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_filtering/_activate'
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
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="connector.update_active_filtering",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("api_key_id", "api_key_secret_id"),
    )
    @_stability_warning(Stability.BETA)
    def update_api_key_id(
        self,
        *,
        connector_id: str,
        api_key_id: t.Optional[str] = None,
        api_key_secret_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector API key ID.</p>
          <p>Update the <code>api_key_id</code> and <code>api_key_secret_id</code> fields of a connector.
          You can specify the ID of the API key used for authorization and the ID of the connector secret where the API key is stored.
          The connector secret ID is required only for Elastic managed (native) connectors.
          Self-managed connectors (connector clients) do not use this field.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-api-key-id>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param api_key_id:
        :param api_key_secret_id:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_api_key_id'
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
            if api_key_id is not None:
                __body["api_key_id"] = api_key_id
            if api_key_secret_id is not None:
                __body["api_key_secret_id"] = api_key_secret_id
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_api_key_id",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("configuration", "values"),
    )
    @_stability_warning(Stability.BETA)
    def update_configuration(
        self,
        *,
        connector_id: str,
        configuration: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        values: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector configuration.</p>
          <p>Update the configuration field in the connector document.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-configuration>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param configuration:
        :param values:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_configuration'
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
            if configuration is not None:
                __body["configuration"] = configuration
            if values is not None:
                __body["values"] = values
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_configuration",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("error",),
    )
    @_stability_warning(Stability.EXPERIMENTAL)
    def update_error(
        self,
        *,
        connector_id: str,
        error: t.Optional[t.Union[None, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector error field.</p>
          <p>Set the error field for the connector.
          If the error provided in the request body is non-null, the connector’s status is updated to error.
          Otherwise, if the error is reset to null, the connector status is updated to connected.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-error>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param error:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if error is None and body is None:
            raise ValueError("Empty value passed for parameter 'error'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_error'
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
            if error is not None:
                __body["error"] = error
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_error",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("advanced_snippet", "filtering", "rules"),
    )
    @_stability_warning(Stability.BETA)
    def update_filtering(
        self,
        *,
        connector_id: str,
        advanced_snippet: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        filtering: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        rules: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector filtering.</p>
          <p>Update the draft filtering configuration of a connector and marks the draft validation state as edited.
          The filtering draft is activated once validated by the running Elastic connector service.
          The filtering property is used to configure sync rules (both basic and advanced) for a connector.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-filtering>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param advanced_snippet:
        :param filtering:
        :param rules:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_filtering'
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
            if advanced_snippet is not None:
                __body["advanced_snippet"] = advanced_snippet
            if filtering is not None:
                __body["filtering"] = filtering
            if rules is not None:
                __body["rules"] = rules
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_filtering",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("validation",),
    )
    @_stability_warning(Stability.EXPERIMENTAL)
    def update_filtering_validation(
        self,
        *,
        connector_id: str,
        validation: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector draft filtering validation.</p>
          <p>Update the draft filtering validation info for a connector.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/update-connector-filtering-validation-api.html>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param validation:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if validation is None and body is None:
            raise ValueError("Empty value passed for parameter 'validation'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_filtering/_validation'
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
            if validation is not None:
                __body["validation"] = validation
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_filtering_validation",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("index_name",),
    )
    @_stability_warning(Stability.BETA)
    def update_index_name(
        self,
        *,
        connector_id: str,
        index_name: t.Optional[t.Union[None, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector index name.</p>
          <p>Update the <code>index_name</code> field of a connector, specifying the index where the data ingested by the connector is stored.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-index-name>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param index_name:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if index_name is None and body is None:
            raise ValueError("Empty value passed for parameter 'index_name'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_index_name'
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
            if index_name is not None:
                __body["index_name"] = index_name
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_index_name",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("description", "name"),
    )
    @_stability_warning(Stability.BETA)
    def update_name(
        self,
        *,
        connector_id: str,
        description: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        name: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector name and description.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-name>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param description:
        :param name:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_name'
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
            if description is not None:
                __body["description"] = description
            if name is not None:
                __body["name"] = name
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_name",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("is_native",),
    )
    @_stability_warning(Stability.BETA)
    def update_native(
        self,
        *,
        connector_id: str,
        is_native: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector is_native flag.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/update-connector-native-api.html>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param is_native:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if is_native is None and body is None:
            raise ValueError("Empty value passed for parameter 'is_native'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_native'
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
            if is_native is not None:
                __body["is_native"] = is_native
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_native",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("pipeline",),
    )
    @_stability_warning(Stability.BETA)
    def update_pipeline(
        self,
        *,
        connector_id: str,
        pipeline: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector pipeline.</p>
          <p>When you create a new connector, the configuration of an ingest pipeline is populated with default settings.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-pipeline>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param pipeline:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if pipeline is None and body is None:
            raise ValueError("Empty value passed for parameter 'pipeline'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_pipeline'
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
            if pipeline is not None:
                __body["pipeline"] = pipeline
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_pipeline",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("scheduling",),
    )
    @_stability_warning(Stability.BETA)
    def update_scheduling(
        self,
        *,
        connector_id: str,
        scheduling: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector scheduling.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-scheduling>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param scheduling:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if scheduling is None and body is None:
            raise ValueError("Empty value passed for parameter 'scheduling'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_scheduling'
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
            if scheduling is not None:
                __body["scheduling"] = scheduling
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_scheduling",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("service_type",),
    )
    @_stability_warning(Stability.BETA)
    def update_service_type(
        self,
        *,
        connector_id: str,
        service_type: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector service type.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-service-type>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param service_type:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if service_type is None and body is None:
            raise ValueError("Empty value passed for parameter 'service_type'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_service_type'
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
            if service_type is not None:
                __body["service_type"] = service_type
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_service_type",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("status",),
    )
    @_stability_warning(Stability.EXPERIMENTAL)
    def update_status(
        self,
        *,
        connector_id: str,
        status: t.Optional[
            t.Union[
                str,
                t.Literal[
                    "configured", "connected", "created", "error", "needs_configuration"
                ],
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update the connector status.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-connector-update-status>`_

        :param connector_id: The unique identifier of the connector to be updated
        :param status:
        """
        if connector_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'connector_id'")
        if status is None and body is None:
            raise ValueError("Empty value passed for parameter 'status'")
        __path_parts: t.Dict[str, str] = {"connector_id": _quote(connector_id)}
        __path = f'/_connector/{__path_parts["connector_id"]}/_status'
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
            if status is not None:
                __body["status"] = status
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="connector.update_status",
            path_parts=__path_parts,
        )
