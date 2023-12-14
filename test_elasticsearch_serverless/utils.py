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

import os
import re
import time
from pathlib import Path
from typing import Optional, Tuple

from elasticsearch_serverless import Elasticsearch, RequestError

SOURCE_DIR = Path(__file__).absolute().parent.parent


def es_url() -> str:
    """Grabs an Elasticsearch URL that must be designated via
    an environment variable, otherwise raises an exception.
    """
    url = os.environ.get("ELASTICSEARCH_URL", None)
    if url is None:
        raise RuntimeError("No ELASTICSEARCH_URL environment variable provided")
    return url


def es_version(client) -> Tuple[int, ...]:
    """Determines the version number and parses the number as a tuple of ints"""
    resp = client.info()
    return parse_version(resp["version"]["number"])


def parse_version(version: Optional[str]) -> Optional[Tuple[int, ...]]:
    """Parses a version number string into it's major, minor, patch as a tuple"""
    if not version:
        return None
    version_number = tuple(
        int(x)
        for x in re.search(r"^([0-9]+(?:\.[0-9]+)*)", version).group(1).split(".")
    )
    return version_number


def wipe_cluster(client, elasticsearch_api_key):
    """Wipes a cluster clean between test cases"""
    close_after_wipe = False
    try:
        # If client is async we need to replace the client
        # with a synchronous one.
        from elasticsearch_serverless import AsyncElasticsearch

        if isinstance(client, AsyncElasticsearch):
            node_config = client.transport.node_pool.get().config
            client = Elasticsearch(node_config, api_key=elasticsearch_api_key)
            close_after_wipe = True
    except ImportError:
        pass

    is_xpack = True
    if is_xpack:
        wipe_data_streams(client)
    wipe_indices(client)

    if is_xpack:
        wipe_xpack_templates(client)
    else:
        client.indices.delete_template(name="*")
        client.indices.delete_index_template(name="*")
        client.cluster.delete_component_template(name="*")

    if is_xpack:
        wipe_transforms(client)

    if close_after_wipe:
        client.close()


def wipe_data_streams(client):
    try:
        client.indices.delete_data_stream(name="*", expand_wildcards="all")
    except Exception:
        client.indices.delete_data_stream(name="*")


def wipe_indices(client):
    indices = client.cat.indices().strip().splitlines()
    if len(indices) > 0:
        index_names = [i.split(" ")[2] for i in indices]
        client.options(ignore_status=404).indices.delete(
            index=",".join(index_names),
            expand_wildcards="all",
        )


def wipe_xpack_templates(client):
    # Delete component templates, need to retry because sometimes
    # indices aren't cleaned up in time before we issue the delete.
    templates = client.cluster.get_component_template()["component_templates"]
    templates_to_delete = [
        template for template in templates if not is_xpack_template(template["name"])
    ]
    for _ in range(3):
        for template in list(templates_to_delete):
            try:
                client.cluster.delete_component_template(
                    name=template["name"],
                )
            except RequestError:
                pass
            else:
                templates_to_delete.remove(template)

        if not templates_to_delete:
            break
        time.sleep(0.01)


def wipe_transforms(client: Elasticsearch, timeout=30):
    end_time = time.time() + timeout
    while time.time() < end_time:
        resp = client.transform.get_transform(transform_id="*")
        if resp["count"] == 0:
            break
        for trasnform in resp["transforms"]:
            client.options(ignore_status=404).transform.stop_transform(
                transform_id=trasnform["id"]
            )
            client.options(ignore_status=404).transform.delete_transform(
                transform_id=trasnform["id"]
            )


def is_xpack_template(name):
    if name.startswith(".monitoring-"):
        return True
    elif name.startswith(".watch") or name.startswith(".triggered_watches"):
        return True
    elif name.startswith(".data-frame-"):
        return True
    elif name.startswith(".ml-"):
        return True
    elif name.startswith(".transform-"):
        return True
    elif name.startswith(".deprecation-"):
        return True
    if name in {
        ".watches",
        "security_audit_log",
        ".slm-history",
        ".async-search",
        "saml-service-provider",
        "logs",
        "logs-settings",
        "logs-mappings",
        "metrics",
        "metrics-settings",
        "metrics-mappings",
        "synthetics",
        "synthetics-settings",
        "synthetics-mappings",
        ".snapshot-blob-cache",
        "ilm-history",
        "logstash-index-template",
        "security-index-template",
        "data-streams-mappings",
    }:
        return True
    return False


def es_api_key() -> str:
    """
    Gets Elasticsearch API key ID and secret from environment variables, raises ValueError if none found
    """
    api_key = os.environ.get("ES_API_KEY", None)
    if api_key is None:
        raise RuntimeError("No ES_API_KEY environment variable provided")
    return api_key
