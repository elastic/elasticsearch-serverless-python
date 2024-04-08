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

    @_rewrite_parameters()
    def delete_model(
        self,
        *,
        inference_id: str,
        task_type: t.Optional[
            t.Union[
                "t.Literal['completion', 'rerank', 'sparse_embedding', 'text_embedding']",
                str,
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Delete model in the Inference API

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/delete-inference-api.html>`_

        :param inference_id: The inference Id
        :param task_type: The task type
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(task_type)}/{_quote(inference_id)}"
        elif inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(inference_id)}"
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
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "DELETE", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    def get_model(
        self,
        *,
        inference_id: str,
        task_type: t.Optional[
            t.Union[
                "t.Literal['completion', 'rerank', 'sparse_embedding', 'text_embedding']",
                str,
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Get a model in the Inference API

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/get-inference-api.html>`_

        :param inference_id: The inference Id
        :param task_type: The task type
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(task_type)}/{_quote(inference_id)}"
        elif inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(inference_id)}"
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
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters(
        body_fields=True,
    )
    def inference(
        self,
        *,
        inference_id: str,
        input: t.Union[str, t.Sequence[str]],
        task_type: t.Optional[
            t.Union[
                "t.Literal['completion', 'rerank', 'sparse_embedding', 'text_embedding']",
                str,
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        query: t.Optional[str] = None,
        task_settings: t.Optional[t.Any] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Perform inference on a model

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/post-inference-api.html>`_

        :param inference_id: The inference Id
        :param input: Text input to the model. Either a string or an array of strings.
        :param task_type: The task type
        :param query: Query input, required for rerank task. Not required for other tasks.
        :param task_settings: Optional task settings
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if input is None:
            raise ValueError("Empty value passed for parameter 'input'")
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(task_type)}/{_quote(inference_id)}"
        elif inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(inference_id)}"
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __body: t.Dict[str, t.Any] = {}
        __query: t.Dict[str, t.Any] = {}
        if input is not None:
            __body["input"] = input
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if pretty is not None:
            __query["pretty"] = pretty
        if query is not None:
            __body["query"] = query
        if task_settings is not None:
            __body["task_settings"] = task_settings
        if not __body:
            __body = None  # type: ignore[assignment]
        __headers = {"accept": "application/json"}
        if __body is not None:
            __headers["content-type"] = "application/json"
        return self.perform_request(  # type: ignore[return-value]
            "POST", __path, params=__query, headers=__headers, body=__body
        )

    @_rewrite_parameters(
        body_name="model_config",
    )
    def put_model(
        self,
        *,
        inference_id: str,
        model_config: t.Mapping[str, t.Any],
        task_type: t.Optional[
            t.Union[
                "t.Literal['completion', 'rerank', 'sparse_embedding', 'text_embedding']",
                str,
            ]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        Configure a model for use in the Inference API

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/put-inference-api.html>`_

        :param inference_id: The inference Id
        :param model_config:
        :param task_type: The task type
        """
        if inference_id in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'inference_id'")
        if model_config is None:
            raise ValueError("Empty value passed for parameter 'model_config'")
        if task_type not in SKIP_IN_PATH and inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(task_type)}/{_quote(inference_id)}"
        elif inference_id not in SKIP_IN_PATH:
            __path = f"/_inference/{_quote(inference_id)}"
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
        __body = model_config
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "PUT", __path, params=__query, headers=__headers, body=__body
        )