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
from .utils import _rewrite_parameters


class LicenseClient(NamespacedClient):

    @_rewrite_parameters()
    def get(
        self,
        *,
        accept_enterprise: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get license information.</p>
          <p>Get information about your Elastic license including its type, its status, when it was issued, and when it expires.</p>
          <blockquote>
          <p>info
          If the master node is generating a new cluster state, the get license API may return a <code>404 Not Found</code> response.
          If you receive an unexpected 404 response after cluster startup, wait a short period and retry the request.</p>
          </blockquote>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-license-get>`_

        :param accept_enterprise: If `true`, this parameter returns enterprise for Enterprise
            license types. If `false`, this parameter returns platinum for both platinum
            and enterprise license types. This behavior is maintained for backwards compatibility.
            This parameter is deprecated and will always be set to true in 8.x.
        :param local: Specifies whether to retrieve local information. The default value
            is `false`, which means the information is retrieved from the master node.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_license"
        __query: t.Dict[str, t.Any] = {}
        if accept_enterprise is not None:
            __query["accept_enterprise"] = accept_enterprise
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="license.get",
            path_parts=__path_parts,
        )
