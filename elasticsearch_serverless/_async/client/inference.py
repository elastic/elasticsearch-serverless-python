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


class InferenceClient(NamespacedClient):

    @_rewrite_parameters(
        body_fields=("input", "task_settings"),
    )
    async def completion(
        self,
        *,
        inference_id: str,
        input: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        task_settings: t.Optional[t.Any] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Perform completion inference on the service</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-inference>`_

        :param inference_id: The inference Id
        :param input: Inference input. Either a string or an array of strings.
        :param task_settings: Optional task settings
        :param timeout: Specifies the amount of time to wait for the inference request
            to complete.
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if input is None and body is None:
            raise ValueError("Empty value passed for parameter 'input'")
        __path_parts: t.Dict[str, str] = {"inference_id": _quote(inference_id)}
        __path = f'/_inference/completion/{__path_parts["inference_id"]}'
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
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if input is not None:
                __body["input"] = input
            if task_settings is not None:
                __body["task_settings"] = task_settings
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
            endpoint_id="inference.completion",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete(
        self,
        *,
        inference_id: str,
        task_type: t.Optional[
            t.Union[
                str,
                t.Literal[
                    "chat_completion",
                    "completion",
                    "rerank",
                    "sparse_embedding",
                    "text_embedding",
                ],
            ]
        ] = None,
        dry_run: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        force: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete an inference endpoint</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-delete>`_

        :param inference_id: The inference identifier.
        :param task_type: The task type
        :param dry_run: When true, the endpoint is not deleted and a list of ingest processors
            which reference this endpoint is returned.
        :param force: When true, the inference endpoint is forcefully deleted even if
            it is still being used by ingest processors or semantic text fields.
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        __path_parts: t.Dict[str, str]
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path_parts = {
                "task_type": _quote(task_type),
                "inference_id": _quote(inference_id),
            }
            __path = f'/_inference/{__path_parts["task_type"]}/{__path_parts["inference_id"]}'
        elif inference_id not in SKIP_IN_PATH:
            __path_parts = {"inference_id": _quote(inference_id)}
            __path = f'/_inference/{__path_parts["inference_id"]}'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        if dry_run is not None:
            __query["dry_run"] = dry_run
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if force is not None:
            __query["force"] = force
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="inference.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get(
        self,
        *,
        task_type: t.Optional[
            t.Union[
                str,
                t.Literal[
                    "chat_completion",
                    "completion",
                    "rerank",
                    "sparse_embedding",
                    "text_embedding",
                ],
            ]
        ] = None,
        inference_id: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get an inference endpoint</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-get>`_

        :param task_type: The task type
        :param inference_id: The inference Id
        """
        __path_parts: t.Dict[str, str]
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path_parts = {
                "task_type": _quote(task_type),
                "inference_id": _quote(inference_id),
            }
            __path = f'/_inference/{__path_parts["task_type"]}/{__path_parts["inference_id"]}'
        elif inference_id not in SKIP_IN_PATH:
            __path_parts = {"inference_id": _quote(inference_id)}
            __path = f'/_inference/{__path_parts["inference_id"]}'
        else:
            __path_parts = {}
            __path = "/_inference"
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
            endpoint_id="inference.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="inference_config",
    )
    async def put(
        self,
        *,
        inference_id: str,
        inference_config: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        task_type: t.Optional[
            t.Union[
                str,
                t.Literal[
                    "chat_completion",
                    "completion",
                    "rerank",
                    "sparse_embedding",
                    "text_embedding",
                ],
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create an inference endpoint.
          When you create an inference endpoint, the associated machine learning model is automatically deployed if it is not already running.
          After creating the endpoint, wait for the model deployment to complete before using it.
          To verify the deployment status, use the get trained model statistics API.
          Look for <code>&quot;state&quot;: &quot;fully_allocated&quot;</code> in the response and ensure that the <code>&quot;allocation_count&quot;</code> matches the <code>&quot;target_allocation_count&quot;</code>.
          Avoid creating multiple endpoints for the same model unless required, as each endpoint consumes significant resources.</p>
          <p>IMPORTANT: The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Mistral, Azure OpenAI, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
          For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models.
          However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the machine learning trained model APIs.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put>`_

        :param inference_id: The inference Id
        :param inference_config:
        :param task_type: The task type
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if inference_config is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'inference_config' and 'body', one of them should be set."
            )
        elif inference_config is not None and body is not None:
            raise ValueError("Cannot set both 'inference_config' and 'body'")
        __path_parts: t.Dict[str, str]
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path_parts = {
                "task_type": _quote(task_type),
                "inference_id": _quote(inference_id),
            }
            __path = f'/_inference/{__path_parts["task_type"]}/{__path_parts["inference_id"]}'
        elif inference_id not in SKIP_IN_PATH:
            __path_parts = {"inference_id": _quote(inference_id)}
            __path = f'/_inference/{__path_parts["inference_id"]}'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        __body = inference_config if inference_config is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="inference.put",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("service", "service_settings"),
    )
    async def put_watsonx(
        self,
        *,
        task_type: t.Union[str, t.Literal["text_embedding"]],
        watsonx_inference_id: str,
        service: t.Optional[t.Union[str, t.Literal["watsonxai"]]] = None,
        service_settings: t.Optional[t.Mapping[str, t.Any]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create a Watsonx inference endpoint.</p>
          <p>Creates an inference endpoint to perform an inference task with the <code>watsonxai</code> service.
          You need an IBM Cloud Databases for Elasticsearch deployment to use the <code>watsonxai</code> inference service.
          You can provision one through the IBM catalog, the Cloud Databases CLI plug-in, the Cloud Databases API, or Terraform.</p>
          <p>When you create an inference endpoint, the associated machine learning model is automatically deployed if it is not already running.
          After creating the endpoint, wait for the model deployment to complete before using it.
          To verify the deployment status, use the get trained model statistics API.
          Look for <code>&quot;state&quot;: &quot;fully_allocated&quot;</code> in the response and ensure that the <code>&quot;allocation_count&quot;</code> matches the <code>&quot;target_allocation_count&quot;</code>.
          Avoid creating multiple endpoints for the same model unless required, as each endpoint consumes significant resources.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/infer-service-watsonx-ai.html>`_

        :param task_type: The task type. The only valid task type for the model to perform
            is `text_embedding`.
        :param watsonx_inference_id: The unique identifier of the inference endpoint.
        :param service: The type of service supported for the specified task type. In
            this case, `watsonxai`.
        :param service_settings: Settings used to install the inference model. These
            settings are specific to the `watsonxai` service.
        """
        if task_type in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'task_type'")
        if watsonx_inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'watsonx_inference_id'")
        if service is None and body is None:
            raise ValueError("Empty value passed for parameter 'service'")
        if service_settings is None and body is None:
            raise ValueError("Empty value passed for parameter 'service_settings'")
        __path_parts: t.Dict[str, str] = {
            "task_type": _quote(task_type),
            "watsonx_inference_id": _quote(watsonx_inference_id),
        }
        __path = f'/_inference/{__path_parts["task_type"]}/{__path_parts["watsonx_inference_id"]}'
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
            if service is not None:
                __body["service"] = service
            if service_settings is not None:
                __body["service_settings"] = service_settings
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
            endpoint_id="inference.put_watsonx",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("input", "query", "task_settings"),
    )
    async def rerank(
        self,
        *,
        inference_id: str,
        input: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        query: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        task_settings: t.Optional[t.Any] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Perform rereanking inference on the service</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-inference>`_

        :param inference_id: The unique identifier for the inference endpoint.
        :param input: The text on which you want to perform the inference task. It can
            be a single string or an array. > info > Inference endpoints for the `completion`
            task type currently only support a single string as input.
        :param query: Query input.
        :param task_settings: Task settings for the individual inference request. These
            settings are specific to the task type you specified and override the task
            settings specified when initializing the service.
        :param timeout: The amount of time to wait for the inference request to complete.
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if input is None and body is None:
            raise ValueError("Empty value passed for parameter 'input'")
        if query is None and body is None:
            raise ValueError("Empty value passed for parameter 'query'")
        __path_parts: t.Dict[str, str] = {"inference_id": _quote(inference_id)}
        __path = f'/_inference/rerank/{__path_parts["inference_id"]}'
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
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if input is not None:
                __body["input"] = input
            if query is not None:
                __body["query"] = query
            if task_settings is not None:
                __body["task_settings"] = task_settings
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
            endpoint_id="inference.rerank",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("input", "task_settings"),
    )
    async def sparse_embedding(
        self,
        *,
        inference_id: str,
        input: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        task_settings: t.Optional[t.Any] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Perform sparse embedding inference on the service</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-inference>`_

        :param inference_id: The inference Id
        :param input: Inference input. Either a string or an array of strings.
        :param task_settings: Optional task settings
        :param timeout: Specifies the amount of time to wait for the inference request
            to complete.
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if input is None and body is None:
            raise ValueError("Empty value passed for parameter 'input'")
        __path_parts: t.Dict[str, str] = {"inference_id": _quote(inference_id)}
        __path = f'/_inference/sparse_embedding/{__path_parts["inference_id"]}'
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
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if input is not None:
                __body["input"] = input
            if task_settings is not None:
                __body["task_settings"] = task_settings
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
            endpoint_id="inference.sparse_embedding",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("input", "task_settings"),
    )
    async def text_embedding(
        self,
        *,
        inference_id: str,
        input: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        task_settings: t.Optional[t.Any] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Perform text embedding inference on the service</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-inference>`_

        :param inference_id: The inference Id
        :param input: Inference input. Either a string or an array of strings.
        :param task_settings: Optional task settings
        :param timeout: Specifies the amount of time to wait for the inference request
            to complete.
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if input is None and body is None:
            raise ValueError("Empty value passed for parameter 'input'")
        __path_parts: t.Dict[str, str] = {"inference_id": _quote(inference_id)}
        __path = f'/_inference/text_embedding/{__path_parts["inference_id"]}'
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
        if timeout is not None:
            __query["timeout"] = timeout
        if not __body:
            if input is not None:
                __body["input"] = input
            if task_settings is not None:
                __body["task_settings"] = task_settings
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
            endpoint_id="inference.text_embedding",
            path_parts=__path_parts,
        )
