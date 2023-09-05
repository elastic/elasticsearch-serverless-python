# -*- coding: utf-8 -*-
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

import re
import warnings

import pytest
from elastic_transport import ApiResponseMeta, BaseNode, HttpHeaders, NodeConfig
from elastic_transport._node import NodeApiResponse
from elastic_transport.client_utils import DEFAULT

from elasticsearch_serverless import Elasticsearch, __versionstr__
from elasticsearch_serverless.exceptions import (
    ApiError,
    ConnectionError,
    ElasticsearchWarning,
    UnsupportedProductError,
)


class DummyNode(BaseNode):
    def __init__(self, config: NodeConfig):
        self.resp_status = config._extras.pop("status", 200)
        self.resp_error = config._extras.pop("exception", None)
        self.resp_data = config._extras.pop("data", b"{}")
        self.resp_headers = config._extras.pop(
            "headers", {"X-elastic-product": "Elasticsearch"}
        )
        self.calls = []

        super().__init__(config)

    def perform_request(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        if self.resp_error:
            raise self.resp_error
        return NodeApiResponse(
            ApiResponseMeta(
                status=self.resp_status,
                headers=HttpHeaders(self.resp_headers),
                http_version="1.1",
                duration=0.0,
                node=self.config,
            ),
            self.resp_data,
        )


CLUSTER_NODES = """{
  "_nodes" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0
  },
  "cluster_name" : "elasticsearch",
  "nodes" : {
    "SRZpKFZdQguhhvifmN6UVA" : {
      "name" : "SRZpKFZ",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1",
      "version" : "5.0.0",
      "build_hash" : "253032b",
      "roles" : [ "master", "data", "ingest" ],
      "http" : {
        "bound_address" : [ "[fe80::1]:9200", "[::1]:9200", "127.0.0.1:9200" ],
        "publish_address" : "1.1.1.1:123",
        "max_content_length_in_bytes" : 104857600
      }
    }
  }
}"""

CLUSTER_NODES_7x_PUBLISH_HOST = """{
  "_nodes" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0
  },
  "cluster_name" : "elasticsearch",
  "nodes" : {
    "SRZpKFZdQguhhvifmN6UVA" : {
      "name" : "SRZpKFZ",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1",
      "version" : "5.0.0",
      "build_hash" : "253032b",
      "roles" : [ "master", "data", "ingest" ],
      "http" : {
        "bound_address" : [ "[fe80::1]:9200", "[::1]:9200", "127.0.0.1:9200" ],
        "publish_address" : "somehost.tld/1.1.1.1:123",
        "max_content_length_in_bytes" : 104857600
      }
    }
  }
}"""

CLUSTER_NODES_MASTER_ONLY = """{
  "_nodes" : {
    "total" : 2,
    "successful" : 2,
    "failed" : 0
  },
  "cluster_name" : "elasticsearch",
  "nodes" : {
    "SRZpKFZdQguhhvifmN6UVA" : {
      "name" : "SRZpKFZa",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1",
      "version" : "5.0.0",
      "build_hash" : "253032b",
      "roles" : ["master"],
      "http" : {
        "bound_address" : [ "[fe80::1]:9200", "[::1]:9200", "127.0.0.1:9200" ],
        "publish_address" : "somehost.tld/1.1.1.1:123",
        "max_content_length_in_bytes" : 104857600
      }
    },
    "SRZpKFZdQguhhvifmN6UVB" : {
      "name" : "SRZpKFZb",
      "transport_address" : "127.0.0.1:9300",
      "host" : "127.0.0.1",
      "ip" : "127.0.0.1",
      "version" : "5.0.0",
      "build_hash" : "253032b",
      "roles" : [ "master", "data", "ingest" ],
      "http" : {
        "bound_address" : [ "[fe80::1]:9200", "[::1]:9200", "127.0.0.1:9200" ],
        "publish_address" : "somehost.tld/1.1.1.1:124",
        "max_content_length_in_bytes" : 104857600
      }
    }
  }
}"""


class TestTransport:
    def test_request_timeout_extracted_from_params_and_passed(self):
        client = Elasticsearch(
            "http://localhost:9200", meta_header=False, node_class=DummyNode
        )

        client.info(params={"request_timeout": 42})
        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        assert calls[0][0] == ("GET", "/")
        assert calls[0][1]["request_timeout"] == 42

    def test_opaque_id(self):
        client = Elasticsearch(
            "http://localhost:9200",
            meta_header=False,
            node_class=DummyNode,
            opaque_id="app-1",
        )

        client.info()
        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        assert calls[0][0] == ("GET", "/")
        assert calls[0][1]["headers"]["x-opaque-id"] == "app-1"

        # Now try with an 'x-opaque-id' set on perform_request().
        client.info(opaque_id="request-2")
        calls = client.transport.node_pool.get().calls
        assert 2 == len(calls)
        assert calls[1][0] == ("GET", "/")
        assert calls[1][1]["headers"]["x-opaque-id"] == "request-2"

    def test_custom_user_agent_on_initialization(self):
        client = Elasticsearch(
            "http://localhost:9200", headers={"user-agent": "custom/1.2.3"}
        )
        headers = [node.config for node in client.transport.node_pool.all()][0].headers
        assert list(headers.keys()) == ["user-agent"]
        assert headers["user-agent"].startswith(f"elasticsearch-py/{__versionstr__} (")

    def test_request_with_custom_user_agent_header(self):
        client = Elasticsearch(
            "http://localhost:9200", meta_header=False, node_class=DummyNode
        )

        client.info(headers={"User-Agent": "my-custom-value/1.2.3"})
        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        assert calls[0][0] == ("GET", "/")
        assert calls[0][1]["headers"]["user-agent"] == "my-custom-value/1.2.3"

    def test_request_with_custom_user_agent_header_set_at_client_level(self):
        client = Elasticsearch(
            "http://localhost:9200",
            meta_header=False,
            node_class=DummyNode,
            headers={"User-Agent": "my-custom-value/1.2.3"},
        )

        client.info()
        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        assert calls[0][0] == ("GET", "/")
        assert calls[0][1]["headers"]["user-agent"] == "my-custom-value/1.2.3"

    def test_client_meta_header(self):
        client = Elasticsearch("http://localhost:9200", node_class=DummyNode)
        client.info()

        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        headers = calls[0][1]["headers"]
        assert re.search(
            r"^esv=[0-9.]+p?,py=[0-9.]+p?,t=[0-9.]+p?$",
            headers["x-elastic-client-meta"],
        )

        class DummyNodeWithMeta(DummyNode):
            _CLIENT_META_HTTP_CLIENT = ("dm", "1.2.3")

        client = Elasticsearch("http://localhost:9200", node_class=DummyNodeWithMeta)
        client.info(headers={"CustoM": "header"})

        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        headers = calls[0][1]["headers"]
        assert re.search(
            r"^esv=[0-9.]+p?,py=[0-9.]+p?,t=[0-9.]+p?,dm=1.2.3$",
            headers["x-elastic-client-meta"],
        )
        assert headers["Custom"] == "header"

    def test_client_meta_header_not_sent(self):
        client = Elasticsearch(
            "http://localhost:9200", meta_header=False, node_class=DummyNode
        )
        client.info()

        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        assert calls[0][1]["headers"] == {
            "accept": "application/vnd.elasticsearch+json; compatible-with=8",
        }

    def test_meta_header_type_error(self):
        with pytest.raises(TypeError) as e:
            Elasticsearch("https://localhost:9200", meta_header=1)
        assert str(e.value) == "'meta_header' must be of type bool"

    def test_body_surrogates_replaced_encoded_into_bytes(self):
        client = Elasticsearch("http://localhost:9200", node_class=DummyNode)
        client.search(query={"match": "你好\uda6a"})

        calls = client.transport.node_pool.get().calls
        assert 1 == len(calls)
        assert (
            calls[0][1]["body"]
            == b'{"query":{"match":"\xe4\xbd\xa0\xe5\xa5\xbd\xed\xa9\xaa"}}'
        )

    def test_kwargs_passed_on_to_node_pool(self):
        dt = object()
        client = Elasticsearch("http://localhost:9200", dead_node_backoff_factor=dt)
        assert dt is client.transport.node_pool.dead_node_backoff_factor

    def test_custom_node_class(self):
        class MyConnection(object):
            def __init__(self, *_, **__):
                pass

            def perform_request(*_, **__):
                pass

        client = Elasticsearch("http://localhost:9200", node_class=MyConnection)
        assert 1 == len(client.transport.node_pool)
        assert isinstance(client.transport.node_pool.all()[0], MyConnection)

    def test_request_will_fail_after_x_retries(self):
        client = Elasticsearch(
            NodeConfig(
                "http",
                "localhost",
                9200,
                _extras={"exception": ConnectionError("abandon ship!")},
            ),
            node_class=DummyNode,
        )

        with pytest.raises(ConnectionError) as e:
            client.info()
        calls = client.transport.node_pool.get().calls
        assert 4 == len(calls)
        assert len(e.value.errors) == 3
        del calls[:]

        with pytest.raises(ConnectionError):
            client.options(max_retries=5).info()
        calls = client.transport.node_pool.get().calls
        assert 6 == len(calls)

    def test_failed_connection_will_be_marked_as_dead(self):
        client = Elasticsearch(
            NodeConfig(
                "http",
                "localhost",
                9200,
                _extras={"exception": ConnectionError("abandon ship!")},
            ),
            node_class=DummyNode,
        )

        with pytest.raises(ConnectionError):
            client.info()
        assert 0 == len(client.transport.node_pool._alive_nodes)

    def test_resurrected_connection_will_be_marked_as_live_on_success(self):
        client = Elasticsearch(
            NodeConfig("http", "localhost", 9200),
            node_class=DummyNode,
        )
        node1 = client.transport.node_pool.get()
        client.transport.node_pool.mark_dead(node1)
        assert len(client.transport.node_pool._alive_nodes) == 0

        client.info()

        assert len(client.transport.node_pool._alive_nodes) == 1


@pytest.mark.parametrize("headers", [{}, {"X-elastic-product": "BAD HEADER"}])
def test_unsupported_product_error(headers):
    client = Elasticsearch(
        NodeConfig("http", "localhost", 9200, _extras={"headers": headers}),
        meta_header=False,
        node_class=DummyNode,
    )

    with pytest.raises(UnsupportedProductError) as e:
        client.info()
    assert str(e.value) == (
        "The client noticed that the server is not Elasticsearch "
        "and we do not support this unknown product"
    )

    calls = client.transport.node_pool.get().calls
    assert len(calls) == 1
    assert calls[0] == (
        ("GET", "/"),
        {
            "body": None,
            "headers": {
                "accept": "application/vnd.elasticsearch+json; compatible-with=8",
            },
            "request_timeout": DEFAULT,
        },
    )


@pytest.mark.parametrize("status", [401, 403, 413, 500])
def test_unsupported_product_error_not_raised_on_non_2xx(status):
    client = Elasticsearch(
        NodeConfig(
            "http", "localhost", 9200, _extras={"headers": {}, "status": status}
        ),
        meta_header=False,
        node_class=DummyNode,
    )
    try:
        client.info()
    except UnsupportedProductError:
        assert False, "Raised UnsupportedProductError"
    except ApiError as e:
        assert e.meta.status == status


@pytest.mark.parametrize("status", [404, 500])
def test_api_error_raised_before_product_error(status):
    client = Elasticsearch(
        NodeConfig(
            "http",
            "localhost",
            9200,
            _extras={
                "headers": {"X-elastic-product": "BAD HEADER"},
                "status": status,
            },
        ),
        meta_header=False,
        node_class=DummyNode,
    )

    with pytest.raises(ApiError) as e:
        client.info()
    assert not isinstance(e.value, UnsupportedProductError)
    assert e.value.status_code == status

    calls = client.transport.node_pool.get().calls
    assert len(calls) == 1
    assert calls[0][0] == ("GET", "/")


@pytest.mark.parametrize(
    "headers",
    [
        {
            "Warning": '299 Elasticsearch-8.0.0-SNAPSHOT-ad975cacd240b3329e160673c432e768dcd7899a "[xpack.monitoring.history.duration] setting was deprecated in Elasticsearch and will be removed in a future release! See the breaking changes documentation for the next major version."',
            "X-elastic-product": "Elasticsearch",
        },
        {
            "Warning": '299 Elasticsearch-8.0.0-SNAPSHOT-ad975cacd240b3329e160673c432e768dcd7899a "[xpack.monitoring.history.duration] setting was deprecated in Elasticsearch and will be removed in a future release! See the breaking changes documentation for the next major version.", 299 Elasticsearch-8.0.0-SNAPSHOT-ad975cacd240b3329e160673c432e768dcd7899a "[xpack.monitoring.history.duration2] setting was deprecated in Elasticsearch and will be removed in a future release! See the breaking changes documentation for the next major version."',
            "X-elastic-product": "Elasticsearch",
        },
    ],
)
def test_warning_header(headers):
    client = Elasticsearch(
        NodeConfig("http", "localhost", 9200, _extras={"headers": headers}),
        meta_header=False,
        node_class=DummyNode,
    )

    with warnings.catch_warnings(record=True) as w:
        client.info()

    assert len(w) == headers["Warning"].count("299")
    assert w[0].category == ElasticsearchWarning
    assert (
        str(w[0].message)
        == "[xpack.monitoring.history.duration] setting was deprecated in Elasticsearch and will be removed in a future release! See the breaking changes documentation for the next major version."
    )
