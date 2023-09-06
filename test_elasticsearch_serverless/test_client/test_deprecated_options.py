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

import warnings

import pytest

from elasticsearch_serverless import Elasticsearch, JsonSerializer


def test_http_auth():
    with warnings.catch_warnings(record=True) as w:
        client = Elasticsearch(
            "http://localhost:9200", http_auth=("username", "password")
        )

    assert len(w) == 1
    assert w[0].category == DeprecationWarning
    assert (
        str(w[0].message)
        == "The 'http_auth' parameter is deprecated. Use 'basic_auth' or 'bearer_auth' parameters instead"
    )
    assert client._headers["Authorization"] == "Basic dXNlcm5hbWU6cGFzc3dvcmQ="

    with pytest.raises(ValueError) as e:
        Elasticsearch(
            "http://localhost:9200",
            http_auth=("username", "password"),
            basic_auth=("username", "password"),
        )
    assert (
        str(e.value)
        == "Can't specify both 'http_auth' and 'basic_auth', instead only specify 'basic_auth'"
    )


def test_serializer_and_serializers():
    with pytest.raises(ValueError) as e:
        Elasticsearch(
            "http://localhost:9200",
            serializer=JsonSerializer(),
            serializers={"application/json": JsonSerializer()},
        )
    assert str(e.value) == (
        "Can't specify both 'serializer' and 'serializers' parameters together. "
        "Instead only specify one of the other."
    )

    class CustomSerializer(JsonSerializer):
        pass

    client = Elasticsearch("http://localhost:9200", serializer=CustomSerializer())
    assert isinstance(
        client.transport.serializers.get_serializer("application/json"),
        CustomSerializer,
    )
    assert set(client.transport.serializers.serializers.keys()) == {
        "application/vnd.mapbox-vector-tile",
        "application/x-ndjson",
        "application/json",
        "text/*",
        "application/vnd.elasticsearch+json",
        "application/vnd.elasticsearch+x-ndjson",
    }

    client = Elasticsearch(
        "http://localhost:9200",
        serializers={
            "application/json": CustomSerializer(),
            "application/cbor": CustomSerializer(),
        },
    )
    assert isinstance(
        client.transport.serializers.get_serializer("application/json"),
        CustomSerializer,
    )
    assert set(client.transport.serializers.serializers.keys()) == {
        "application/vnd.mapbox-vector-tile",
        "application/x-ndjson",
        "application/json",
        "text/*",
        "application/vnd.elasticsearch+json",
        "application/vnd.elasticsearch+x-ndjson",
        "application/cbor",
    }
