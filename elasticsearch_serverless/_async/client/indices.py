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


class IndicesClient(NamespacedClient):

    @_rewrite_parameters()
    async def add_block(
        self,
        *,
        index: str,
        block: t.Union[str, t.Literal["metadata", "read", "read_only", "write"]],
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Add an index block.</p>
          <p>Add an index block to an index.
          Index blocks limit the operations allowed on an index by blocking specific operation types.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-add-block>`_

        :param index: A comma-separated list or wildcard expression of index names used
            to limit the request. By default, you must explicitly name the indices you
            are adding blocks to. To allow the adding of blocks to indices with `_all`,
            `*`, or other wildcard expressions, change the `action.destructive_requires_name`
            setting to `false`. You can update this setting in the `elasticsearch.yml`
            file or by using the cluster update settings API.
        :param block: The block type to add to the index.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param expand_wildcards: The type of index that wildcard patterns can match.
            If the request can target data streams, this argument determines whether
            wildcard expressions match hidden data streams. It supports comma-separated
            values, such as `open,hidden`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param master_timeout: The period to wait for the master node. If the master
            node is not available before the timeout expires, the request fails and returns
            an error. It can also be set to `-1` to indicate that the request should
            never timeout.
        :param timeout: The period to wait for a response from all relevant nodes in
            the cluster after updating the cluster metadata. If no response is received
            before the timeout expires, the cluster metadata update still applies but
            the response will indicate that it was not completely acknowledged. It can
            also be set to `-1` to indicate that the request should never timeout.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if block in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'block'")
        __path_parts: t.Dict[str, str] = {
            "index": _quote(index),
            "block": _quote(block),
        }
        __path = f'/{__path_parts["index"]}/_block/{__path_parts["block"]}'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.add_block",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "analyzer",
            "attributes",
            "char_filter",
            "explain",
            "field",
            "filter",
            "normalizer",
            "text",
            "tokenizer",
        ),
    )
    async def analyze(
        self,
        *,
        index: t.Optional[str] = None,
        analyzer: t.Optional[str] = None,
        attributes: t.Optional[t.Sequence[str]] = None,
        char_filter: t.Optional[t.Sequence[t.Union[str, t.Mapping[str, t.Any]]]] = None,
        error_trace: t.Optional[bool] = None,
        explain: t.Optional[bool] = None,
        field: t.Optional[str] = None,
        filter: t.Optional[t.Sequence[t.Union[str, t.Mapping[str, t.Any]]]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        normalizer: t.Optional[str] = None,
        pretty: t.Optional[bool] = None,
        text: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        tokenizer: t.Optional[t.Union[str, t.Mapping[str, t.Any]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get tokens from text analysis.
          The analyze API performs analysis on a text string and returns the resulting tokens.</p>
          <p>Generating excessive amount of tokens may cause a node to run out of memory.
          The <code>index.analyze.max_token_count</code> setting enables you to limit the number of tokens that can be produced.
          If more than this limit of tokens gets generated, an error occurs.
          The <code>_analyze</code> endpoint without a specified index will always use <code>10000</code> as its limit.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-analyze>`_

        :param index: Index used to derive the analyzer. If specified, the `analyzer`
            or field parameter overrides this value. If no index is specified or the
            index does not have a default analyzer, the analyze API uses the standard
            analyzer.
        :param analyzer: The name of the analyzer that should be applied to the provided
            `text`. This could be a built-in analyzer, or an analyzer that’s been configured
            in the index.
        :param attributes: Array of token attributes used to filter the output of the
            `explain` parameter.
        :param char_filter: Array of character filters used to preprocess characters
            before the tokenizer.
        :param explain: If `true`, the response includes token attributes and additional
            details.
        :param field: Field used to derive the analyzer. To use this parameter, you must
            specify an index. If specified, the `analyzer` parameter overrides this value.
        :param filter: Array of token filters used to apply after the tokenizer.
        :param normalizer: Normalizer to use to convert text into a single token.
        :param text: Text to analyze. If an array of strings is provided, it is analyzed
            as a multi-value field.
        :param tokenizer: Tokenizer to use to convert text into tokens.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_analyze'
        else:
            __path_parts = {}
            __path = "/_analyze"
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
            if analyzer is not None:
                __body["analyzer"] = analyzer
            if attributes is not None:
                __body["attributes"] = attributes
            if char_filter is not None:
                __body["char_filter"] = char_filter
            if explain is not None:
                __body["explain"] = explain
            if field is not None:
                __body["field"] = field
            if filter is not None:
                __body["filter"] = filter
            if normalizer is not None:
                __body["normalizer"] = normalizer
            if text is not None:
                __body["text"] = text
            if tokenizer is not None:
                __body["tokenizer"] = tokenizer
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
            endpoint_id="indices.analyze",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("aliases", "mappings", "settings"),
    )
    async def create(
        self,
        *,
        index: str,
        aliases: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        mappings: t.Optional[t.Mapping[str, t.Any]] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        settings: t.Optional[t.Mapping[str, t.Any]] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union[str, t.Literal["all", "index-setting"]]]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create an index.
          You can use the create index API to add a new index to an Elasticsearch cluster.
          When creating an index, you can specify the following:</p>
          <ul>
          <li>Settings for the index.</li>
          <li>Mappings for fields in the index.</li>
          <li>Index aliases</li>
          </ul>
          <p><strong>Wait for active shards</strong></p>
          <p>By default, index creation will only return a response to the client when the primary copies of each shard have been started, or the request times out.
          The index creation response will indicate what happened.
          For example, <code>acknowledged</code> indicates whether the index was successfully created in the cluster, <code>while shards_acknowledged</code> indicates whether the requisite number of shard copies were started for each shard in the index before timing out.
          Note that it is still possible for either <code>acknowledged</code> or <code>shards_acknowledged</code> to be <code>false</code>, but for the index creation to be successful.
          These values simply indicate whether the operation completed before the timeout.
          If <code>acknowledged</code> is false, the request timed out before the cluster state was updated with the newly created index, but it probably will be created sometime soon.
          If <code>shards_acknowledged</code> is false, then the request timed out before the requisite number of shards were started (by default just the primaries), even if the cluster state was successfully updated to reflect the newly created index (that is to say, <code>acknowledged</code> is <code>true</code>).</p>
          <p>You can change the default of only waiting for the primary shards to start through the index setting <code>index.write.wait_for_active_shards</code>.
          Note that changing this setting will also affect the <code>wait_for_active_shards</code> value on all subsequent write operations.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-create>`_

        :param index: Name of the index you wish to create.
        :param aliases: Aliases for the index.
        :param mappings: Mapping for fields in the index. If specified, this mapping
            can include: - Field names - Field data types - Mapping parameters
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param settings: Configuration options for the index.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to `all` or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
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
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        if not __body:
            if aliases is not None:
                __body["aliases"] = aliases
            if mappings is not None:
                __body["mappings"] = mappings
            if settings is not None:
                __body["settings"] = settings
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
            endpoint_id="indices.create",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def create_data_stream(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create a data stream.</p>
          <p>You must have a matching index template with data stream enabled.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-create-data-stream>`_

        :param name: Name of the data stream, which must meet the following criteria:
            Lowercase only; Cannot include `\\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, `,`,
            `#`, `:`, or a space character; Cannot start with `-`, `_`, `+`, or `.ds-`;
            Cannot be `.` or `..`; Cannot be longer than 255 bytes. Multi-byte characters
            count towards this limit faster.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_data_stream/{__path_parts["name"]}'
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
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.create_data_stream",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete indices.
          Deleting an index deletes its documents, shards, and metadata.
          It does not delete related Kibana components, such as data views, visualizations, or dashboards.</p>
          <p>You cannot delete the current write index of a data stream.
          To delete the index, you must roll over the data stream so a new write index is created.
          You can then use the delete index API to delete the previous write index.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete>`_

        :param index: Comma-separated list of indices to delete. You cannot specify index
            aliases. By default, this parameter does not support wildcards (`*`) or `_all`.
            To use wildcards or `_all`, set the `action.destructive_requires_name` cluster
            setting to `false`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.delete",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete_alias(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        name: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete an alias.
          Removes a data stream or index from an alias.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-alias>`_

        :param index: Comma-separated list of data streams or indices used to limit the
            request. Supports wildcards (`*`).
        :param name: Comma-separated list of aliases to remove. Supports wildcards (`*`).
            To remove all aliases, use `*` or `_all`.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "name": _quote(name)}
        __path = f'/{__path_parts["index"]}/_alias/{__path_parts["name"]}'
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
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.delete_alias",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete_data_stream(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete data streams.
          Deletes one or more data streams and their backing indices.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-data-stream>`_

        :param name: Comma-separated list of data streams to delete. Wildcard (`*`) expressions
            are supported.
        :param expand_wildcards: Type of data stream that wildcard patterns can match.
            Supports comma-separated values,such as `open,hidden`.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_data_stream/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.delete_data_stream",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def delete_index_template(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Delete an index template.
          The provided <!-- raw HTML omitted --> may contain multiple template names separated by a comma. If multiple template
          names are specified then there is no wildcard support and the provided names should match completely with
          existing templates.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-delete-index-template>`_

        :param name: Comma-separated list of index template names used to limit the request.
            Wildcard (*) expressions are supported.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_index_template/{__path_parts["name"]}'
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
        return await self.perform_request(  # type: ignore[return-value]
            "DELETE",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.delete_index_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def exists(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> HeadApiResponse:
        """
        .. raw:: html

          <p>Check indices.
          Check if one or more indices, index aliases, or data streams exist.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-exists>`_

        :param index: Comma-separated list of data streams, indices, and aliases. Supports
            wildcards (`*`).
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param flat_settings: If `true`, returns settings in flat format.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param include_defaults: If `true`, return all default settings in the response.
        :param local: If `true`, the request retrieves information from the local node
            only.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if flat_settings is not None:
            __query["flat_settings"] = flat_settings
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if local is not None:
            __query["local"] = local
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "HEAD",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.exists",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def exists_alias(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> HeadApiResponse:
        """
        .. raw:: html

          <p>Check aliases.</p>
          <p>Check if one or more data stream or index aliases exist.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-exists-alias>`_

        :param name: Comma-separated list of aliases to check. Supports wildcards (`*`).
        :param index: Comma-separated list of data streams or indices used to limit the
            request. Supports wildcards (`*`). To target all data streams and indices,
            omit this parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, requests that include a missing data stream
            or index in the target indices or data streams return an error.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH and name not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index), "name": _quote(name)}
            __path = f'/{__path_parts["index"]}/_alias/{__path_parts["name"]}'
        elif name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_alias/{__path_parts["name"]}'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "HEAD",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.exists_alias",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def exists_index_template(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> HeadApiResponse:
        """
        .. raw:: html

          <p>Check index templates.</p>
          <p>Check whether index templates exist.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-exists-index-template>`_

        :param name: Comma-separated list of index template names used to limit the request.
            Wildcard (*) expressions are supported.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_index_template/{__path_parts["name"]}'
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
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "HEAD",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.exists_index_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def explain_data_lifecycle(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get the status for a data stream lifecycle.
          Get information about an index or data stream's current data stream lifecycle status, such as time since index creation, time since rollover, the lifecycle configuration managing the index, or any errors encountered during lifecycle execution.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-explain-data-lifecycle>`_

        :param index: The name of the index to explain
        :param include_defaults: indicates if the API should return the default values
            the system uses for the index's lifecycle
        :param master_timeout: Specify timeout for connection to master
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_lifecycle/explain'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.explain_data_lifecycle",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        features: t.Optional[
            t.Union[
                t.Sequence[t.Union[str, t.Literal["aliases", "mappings", "settings"]]],
                t.Union[str, t.Literal["aliases", "mappings", "settings"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get index information.
          Get information about one or more indices. For data streams, the API returns information about the
          stream’s backing indices.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get>`_

        :param index: Comma-separated list of data streams, indices, and index aliases
            used to limit the request. Wildcard expressions (*) are supported.
        :param allow_no_indices: If false, the request returns an error if any wildcard
            expression, index alias, or _all value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting foo*,bar* returns an error if an index starts
            with foo but no index starts with bar.
        :param expand_wildcards: Type of index that wildcard expressions can match. If
            the request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as open,hidden.
        :param features: Return only information on specified index features
        :param flat_settings: If true, returns settings in flat format.
        :param ignore_unavailable: If false, requests that target a missing index return
            an error.
        :param include_defaults: If true, return all default settings in the response.
        :param local: If true, the request retrieves information from the local node
            only. Defaults to false, which means information is retrieved from the master
            node.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if features is not None:
            __query["features"] = features
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if flat_settings is not None:
            __query["flat_settings"] = flat_settings
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_alias(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get aliases.
          Retrieves information for one or more data stream or index aliases.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-alias>`_

        :param index: Comma-separated list of data streams or indices used to limit the
            request. Supports wildcards (`*`). To target all data streams and indices,
            omit this parameter or use `*` or `_all`.
        :param name: Comma-separated list of aliases to retrieve. Supports wildcards
            (`*`). To retrieve all aliases, omit this parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH and name not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index), "name": _quote(name)}
            __path = f'/{__path_parts["index"]}/_alias/{__path_parts["name"]}'
        elif index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_alias'
        elif name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_alias/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_alias"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get_alias",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_data_lifecycle(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get data stream lifecycles.</p>
          <p>Get the data stream lifecycle configuration of one or more data streams.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-data-lifecycle>`_

        :param name: Comma-separated list of data streams to limit the request. Supports
            wildcards (`*`). To target all data streams, omit this parameter or use `*`
            or `_all`.
        :param expand_wildcards: Type of data stream that wildcard patterns can match.
            Supports comma-separated values, such as `open,hidden`. Valid values are:
            `all`, `open`, `closed`, `hidden`, `none`.
        :param include_defaults: If `true`, return all default settings in the response.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_data_stream/{__path_parts["name"]}/_lifecycle'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get_data_lifecycle",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_data_stream(
        self,
        *,
        name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        verbose: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get data streams.</p>
          <p>Get information about one or more data streams.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-data-stream>`_

        :param name: Comma-separated list of data stream names used to limit the request.
            Wildcard (`*`) expressions are supported. If omitted, all data streams are
            returned.
        :param expand_wildcards: Type of data stream that wildcard patterns can match.
            Supports comma-separated values, such as `open,hidden`.
        :param include_defaults: If true, returns all relevant default configurations
            for the index template.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param verbose: Whether the maximum timestamp for each data stream should be
            calculated and returned.
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_data_stream/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_data_stream"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if verbose is not None:
            __query["verbose"] = verbose
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get_data_stream",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_index_template(
        self,
        *,
        name: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get index templates.
          Get information about one or more index templates.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-index-template>`_

        :param name: Comma-separated list of index template names used to limit the request.
            Wildcard (*) expressions are supported.
        :param flat_settings: If true, returns settings in flat format.
        :param include_defaults: If true, returns all relevant default configurations
            for the index template.
        :param local: If true, the request retrieves information from the local node
            only. Defaults to false, which means information is retrieved from the master
            node.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_index_template/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_index_template"
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
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get_index_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_mapping(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get mapping definitions.
          For data streams, the API retrieves mappings for the stream’s backing indices.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-mapping>`_

        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (`*`). To target all data streams
            and indices, omit this parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param local: If `true`, the request retrieves information from the local node
            only.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_mapping'
        else:
            __path_parts = {}
            __path = "/_mapping"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get_mapping",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def get_settings(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        name: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Get index settings.
          Get setting information for one or more indices.
          For data streams, it returns setting information for the stream's backing indices.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-get-settings>`_

        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (`*`). To target all data streams
            and indices, omit this parameter or use `*` or `_all`.
        :param name: Comma-separated list or wildcard expression of settings to retrieve.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with foo but no index starts with `bar`.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`.
        :param flat_settings: If `true`, returns settings in flat format.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param include_defaults: If `true`, return all default settings in the response.
        :param local: If `true`, the request retrieves information from the local node
            only. If `false`, information is retrieved from the master node.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH and name not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index), "name": _quote(name)}
            __path = f'/{__path_parts["index"]}/_settings/{__path_parts["name"]}'
        elif index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_settings'
        elif name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_settings/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_settings"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if flat_settings is not None:
            __query["flat_settings"] = flat_settings
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.get_settings",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def migrate_to_data_stream(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Convert an index alias to a data stream.
          Converts an index alias to a data stream.
          You must have a matching index template that is data stream enabled.
          The alias must meet the following criteria:
          The alias must have a write index;
          All indices for the alias must have a <code>@timestamp</code> field mapping of a <code>date</code> or <code>date_nanos</code> field type;
          The alias must not have any filters;
          The alias must not use custom routing.
          If successful, the request removes the alias and creates a data stream with the same name.
          The indices for the alias become hidden backing indices for the stream.
          The write index for the alias becomes the write index for the stream.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/data-streams.html>`_

        :param name: Name of the index alias to convert to a data stream.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_data_stream/_migrate/{__path_parts["name"]}'
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
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.migrate_to_data_stream",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("actions",),
    )
    async def modify_data_stream(
        self,
        *,
        actions: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update data streams.
          Performs one or more data stream modification actions in a single atomic operation.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/data-streams.html>`_

        :param actions: Actions to perform.
        """
        if actions is None and body is None:
            raise ValueError("Empty value passed for parameter 'actions'")
        __path_parts: t.Dict[str, str] = {}
        __path = "/_data_stream/_modify"
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
            if actions is not None:
                __body["actions"] = actions
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="indices.modify_data_stream",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "filter",
            "index_routing",
            "is_write_index",
            "routing",
            "search_routing",
        ),
    )
    async def put_alias(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        name: str,
        error_trace: t.Optional[bool] = None,
        filter: t.Optional[t.Mapping[str, t.Any]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        index_routing: t.Optional[str] = None,
        is_write_index: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        routing: t.Optional[str] = None,
        search_routing: t.Optional[str] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create or update an alias.
          Adds a data stream or index to an alias.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-aliases.html>`_

        :param index: Comma-separated list of data streams or indices to add. Supports
            wildcards (`*`). Wildcard patterns that match both data streams and indices
            return an error.
        :param name: Alias to update. If the alias doesn’t exist, the request creates
            it. Index alias names support date math.
        :param filter: Query used to limit documents the alias can access.
        :param index_routing: Value used to route indexing operations to a specific shard.
            If specified, this overwrites the `routing` value for indexing operations.
            Data stream aliases don’t support this parameter.
        :param is_write_index: If `true`, sets the write index or data stream for the
            alias. If an alias points to multiple indices or data streams and `is_write_index`
            isn’t set, the alias rejects write requests. If an index alias points to
            one index and `is_write_index` isn’t set, the index automatically acts as
            the write index. Data stream aliases don’t automatically set a write data
            stream, even if the alias points to one data stream.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param routing: Value used to route indexing and search operations to a specific
            shard. Data stream aliases don’t support this parameter.
        :param search_routing: Value used to route search operations to a specific shard.
            If specified, this overwrites the `routing` value for search operations.
            Data stream aliases don’t support this parameter.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index), "name": _quote(name)}
        __path = f'/{__path_parts["index"]}/_alias/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
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
        if not __body:
            if filter is not None:
                __body["filter"] = filter
            if index_routing is not None:
                __body["index_routing"] = index_routing
            if is_write_index is not None:
                __body["is_write_index"] = is_write_index
            if routing is not None:
                __body["routing"] = routing
            if search_routing is not None:
                __body["search_routing"] = search_routing
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
            endpoint_id="indices.put_alias",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("data_retention", "downsampling", "enabled"),
    )
    async def put_data_lifecycle(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
        data_retention: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        downsampling: t.Optional[t.Mapping[str, t.Any]] = None,
        enabled: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update data stream lifecycles.
          Update the data stream lifecycle of the specified data streams.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/data-streams-put-lifecycle.html>`_

        :param name: Comma-separated list of data streams used to limit the request.
            Supports wildcards (`*`). To target all data streams use `*` or `_all`.
        :param data_retention: If defined, every document added to this data stream will
            be stored at least for this time frame. Any time after this duration the
            document could be deleted. When empty, every document in this data stream
            will be stored indefinitely.
        :param downsampling: The downsampling configuration to execute for the managed
            backing index after rollover.
        :param enabled: If defined, it turns data stream lifecycle on/off (`true`/`false`)
            for this data stream. A data stream lifecycle that's disabled (enabled: `false`)
            will have no effect on the data stream.
        :param expand_wildcards: Type of data stream that wildcard patterns can match.
            Supports comma-separated values, such as `open,hidden`. Valid values are:
            `all`, `hidden`, `open`, `closed`, `none`.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_data_stream/{__path_parts["name"]}/_lifecycle'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
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
        if not __body:
            if data_retention is not None:
                __body["data_retention"] = data_retention
            if downsampling is not None:
                __body["downsampling"] = downsampling
            if enabled is not None:
                __body["enabled"] = enabled
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
            endpoint_id="indices.put_data_lifecycle",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "allow_auto_create",
            "composed_of",
            "data_stream",
            "deprecated",
            "ignore_missing_component_templates",
            "index_patterns",
            "meta",
            "priority",
            "template",
            "version",
        ),
        parameter_aliases={"_meta": "meta"},
    )
    async def put_index_template(
        self,
        *,
        name: str,
        allow_auto_create: t.Optional[bool] = None,
        cause: t.Optional[str] = None,
        composed_of: t.Optional[t.Sequence[str]] = None,
        create: t.Optional[bool] = None,
        data_stream: t.Optional[t.Mapping[str, t.Any]] = None,
        deprecated: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_missing_component_templates: t.Optional[t.Sequence[str]] = None,
        index_patterns: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        meta: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        priority: t.Optional[int] = None,
        template: t.Optional[t.Mapping[str, t.Any]] = None,
        version: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create or update an index template.
          Index templates define settings, mappings, and aliases that can be applied automatically to new indices.</p>
          <p>Elasticsearch applies templates to new indices based on an wildcard pattern that matches the index name.
          Index templates are applied during data stream or index creation.
          For data streams, these settings and mappings are applied when the stream's backing indices are created.
          Settings and mappings specified in a create index API request override any settings or mappings specified in an index template.
          Changes to index templates do not affect existing indices, including the existing backing indices of a data stream.</p>
          <p>You can use C-style <code>/* *\\/</code> block comments in index templates.
          You can include comments anywhere in the request body, except before the opening curly bracket.</p>
          <p><strong>Multiple matching templates</strong></p>
          <p>If multiple index templates match the name of a new index or data stream, the template with the highest priority is used.</p>
          <p>Multiple templates with overlapping index patterns at the same priority are not allowed and an error will be thrown when attempting to create a template matching an existing index template at identical priorities.</p>
          <p><strong>Composing aliases, mappings, and settings</strong></p>
          <p>When multiple component templates are specified in the <code>composed_of</code> field for an index template, they are merged in the order specified, meaning that later component templates override earlier component templates.
          Any mappings, settings, or aliases from the parent index template are merged in next.
          Finally, any configuration on the index request itself is merged.
          Mapping definitions are merged recursively, which means that later mapping components can introduce new field mappings and update the mapping configuration.
          If a field mapping is already contained in an earlier component, its definition will be completely overwritten by the later one.
          This recursive merging strategy applies not only to field mappings, but also root options like <code>dynamic_templates</code> and <code>meta</code>.
          If an earlier component contains a <code>dynamic_templates</code> block, then by default new <code>dynamic_templates</code> entries are appended onto the end.
          If an entry already exists with the same key, then it is overwritten by the new definition.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-put-template.html>`_

        :param name: Index or template name
        :param allow_auto_create: This setting overrides the value of the `action.auto_create_index`
            cluster setting. If set to `true` in a template, then indices can be automatically
            created using that template even if auto-creation of indices is disabled
            via `actions.auto_create_index`. If set to `false`, then indices or data
            streams matching the template must always be explicitly created, and may
            never be automatically created.
        :param cause: User defined reason for creating/updating the index template
        :param composed_of: An ordered list of component template names. Component templates
            are merged in the order specified, meaning that the last component template
            specified has the highest precedence.
        :param create: If `true`, this request cannot replace or update existing index
            templates.
        :param data_stream: If this object is included, the template is used to create
            data streams and their backing indices. Supports an empty object. Data streams
            require a matching index template with a `data_stream` object.
        :param deprecated: Marks this index template as deprecated. When creating or
            updating a non-deprecated index template that uses deprecated components,
            Elasticsearch will emit a deprecation warning.
        :param ignore_missing_component_templates: The configuration option ignore_missing_component_templates
            can be used when an index template references a component template that might
            not exist
        :param index_patterns: Name of the index template to create.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param meta: Optional user metadata about the index template. It may have any
            contents. It is not automatically generated or used by Elasticsearch. This
            user-defined object is stored in the cluster state, so keeping it short is
            preferable To unset the metadata, replace the template without specifying
            it.
        :param priority: Priority to determine index template precedence when a new data
            stream or index is created. The index template with the highest priority
            is chosen. If no priority is specified the template is treated as though
            it is of priority 0 (lowest priority). This number is not automatically generated
            by Elasticsearch.
        :param template: Template to be applied. It may optionally include an `aliases`,
            `mappings`, or `settings` configuration.
        :param version: Version number used to manage index templates externally. This
            number is not automatically generated by Elasticsearch. External systems
            can use these version numbers to simplify template management. To unset a
            version, replace the template without specifying one.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_index_template/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if cause is not None:
            __query["cause"] = cause
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
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_auto_create is not None:
                __body["allow_auto_create"] = allow_auto_create
            if composed_of is not None:
                __body["composed_of"] = composed_of
            if data_stream is not None:
                __body["data_stream"] = data_stream
            if deprecated is not None:
                __body["deprecated"] = deprecated
            if ignore_missing_component_templates is not None:
                __body["ignore_missing_component_templates"] = (
                    ignore_missing_component_templates
                )
            if index_patterns is not None:
                __body["index_patterns"] = index_patterns
            if meta is not None:
                __body["_meta"] = meta
            if priority is not None:
                __body["priority"] = priority
            if template is not None:
                __body["template"] = template
            if version is not None:
                __body["version"] = version
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="indices.put_index_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "date_detection",
            "dynamic",
            "dynamic_date_formats",
            "dynamic_templates",
            "field_names",
            "meta",
            "numeric_detection",
            "properties",
            "routing",
            "runtime",
            "source",
        ),
        parameter_aliases={
            "_field_names": "field_names",
            "_meta": "meta",
            "_routing": "routing",
            "_source": "source",
        },
    )
    async def put_mapping(
        self,
        *,
        index: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        date_detection: t.Optional[bool] = None,
        dynamic: t.Optional[
            t.Union[str, t.Literal["false", "runtime", "strict", "true"]]
        ] = None,
        dynamic_date_formats: t.Optional[t.Sequence[str]] = None,
        dynamic_templates: t.Optional[
            t.Sequence[t.Mapping[str, t.Mapping[str, t.Any]]]
        ] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        field_names: t.Optional[t.Mapping[str, t.Any]] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        meta: t.Optional[t.Mapping[str, t.Any]] = None,
        numeric_detection: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        properties: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        routing: t.Optional[t.Mapping[str, t.Any]] = None,
        runtime: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        source: t.Optional[t.Mapping[str, t.Any]] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        write_index_only: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update field mappings.
          Add new fields to an existing data stream or index.
          You can also use this API to change the search settings of existing fields and add new properties to existing object fields.
          For data streams, these changes are applied to all backing indices by default.</p>
          <p><strong>Add multi-fields to an existing field</strong></p>
          <p>Multi-fields let you index the same field in different ways.
          You can use this API to update the fields mapping parameter and enable multi-fields for an existing field.
          WARNING: If an index (or data stream) contains documents when you add a multi-field, those documents will not have values for the new multi-field.
          You can populate the new multi-field with the update by query API.</p>
          <p><strong>Change supported mapping parameters for an existing field</strong></p>
          <p>The documentation for each mapping parameter indicates whether you can update it for an existing field using this API.
          For example, you can use the update mapping API to update the <code>ignore_above</code> parameter.</p>
          <p><strong>Change the mapping of an existing field</strong></p>
          <p>Except for supported mapping parameters, you can't change the mapping or field type of an existing field.
          Changing an existing field could invalidate data that's already indexed.</p>
          <p>If you need to change the mapping of a field in a data stream's backing indices, refer to documentation about modifying data streams.
          If you need to change the mapping of a field in other indices, create a new index with the correct mapping and reindex your data into that index.</p>
          <p><strong>Rename a field</strong></p>
          <p>Renaming a field would invalidate data already indexed under the old field name.
          Instead, add an alias field to create an alternate field name.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-mapping>`_

        :param index: A comma-separated list of index names the mapping should be added
            to (supports wildcards); use `_all` or omit to add the mapping on all indices.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param date_detection: Controls whether dynamic date detection is enabled.
        :param dynamic: Controls whether new fields are added dynamically.
        :param dynamic_date_formats: If date detection is enabled then new string fields
            are checked against 'dynamic_date_formats' and if the value matches then
            a new date field is added instead of string.
        :param dynamic_templates: Specify dynamic templates for the mapping.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param field_names: Control whether field names are enabled for the index.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param meta: A mapping type can have custom meta data associated with it. These
            are not used at all by Elasticsearch, but can be used to store application-specific
            metadata.
        :param numeric_detection: Automatically map strings into numeric data types for
            all fields.
        :param properties: Mapping for a field. For new fields, this mapping can include:
            - Field name - Field data type - Mapping parameters
        :param routing: Enable making a routing value required on indexed documents.
        :param runtime: Mapping of runtime fields for the index.
        :param source: Control whether the _source field is enabled on the index.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        :param write_index_only: If `true`, the mappings are applied only to the current
            write index for the target.
        """
        if index in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'index'")
        __path_parts: t.Dict[str, str] = {"index": _quote(index)}
        __path = f'/{__path_parts["index"]}/_mapping'
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        if write_index_only is not None:
            __query["write_index_only"] = write_index_only
        if not __body:
            if date_detection is not None:
                __body["date_detection"] = date_detection
            if dynamic is not None:
                __body["dynamic"] = dynamic
            if dynamic_date_formats is not None:
                __body["dynamic_date_formats"] = dynamic_date_formats
            if dynamic_templates is not None:
                __body["dynamic_templates"] = dynamic_templates
            if field_names is not None:
                __body["_field_names"] = field_names
            if meta is not None:
                __body["_meta"] = meta
            if numeric_detection is not None:
                __body["numeric_detection"] = numeric_detection
            if properties is not None:
                __body["properties"] = properties
            if routing is not None:
                __body["_routing"] = routing
            if runtime is not None:
                __body["runtime"] = runtime
            if source is not None:
                __body["_source"] = source
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="indices.put_mapping",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_name="settings",
    )
    async def put_settings(
        self,
        *,
        settings: t.Optional[t.Mapping[str, t.Any]] = None,
        body: t.Optional[t.Mapping[str, t.Any]] = None,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        flat_settings: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        preserve_existing: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Update index settings.
          Changes dynamic index settings in real time.
          For data streams, index setting changes are applied to all backing indices by default.</p>
          <p>To revert a setting to the default value, use a null value.
          The list of per-index settings that can be updated dynamically on live indices can be found in index module documentation.
          To preserve existing settings from being updated, set the <code>preserve_existing</code> parameter to <code>true</code>.</p>
          <p>NOTE: You can only define new analyzers on closed indices.
          To add an analyzer, you must close the index, define the analyzer, and reopen the index.
          You cannot close the write index of a data stream.
          To update the analyzer for a data stream's write index and future backing indices, update the analyzer in the index template used by the stream.
          Then roll over the data stream to apply the new analyzer to the stream's write index and future backing indices.
          This affects searches and any new data added to the stream after the rollover.
          However, it does not affect the data stream's backing indices or their existing data.
          To change the analyzer for existing backing indices, you must create a new data stream and reindex your data into it.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-put-settings>`_

        :param settings:
        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (`*`). To target all data streams
            and indices, omit this parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`.
        :param flat_settings: If `true`, returns settings in flat format.
        :param ignore_unavailable: If `true`, returns settings in flat format.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param preserve_existing: If `true`, existing index settings remain unchanged.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        if settings is None and body is None:
            raise ValueError(
                "Empty value passed for parameters 'settings' and 'body', one of them should be set."
            )
        elif settings is not None and body is not None:
            raise ValueError("Cannot set both 'settings' and 'body'")
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_settings'
        else:
            __path_parts = {}
            __path = "/_settings"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if flat_settings is not None:
            __query["flat_settings"] = flat_settings
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if preserve_existing is not None:
            __query["preserve_existing"] = preserve_existing
        if pretty is not None:
            __query["pretty"] = pretty
        if timeout is not None:
            __query["timeout"] = timeout
        __body = settings if settings is not None else body
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "PUT",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="indices.put_settings",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def refresh(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Refresh an index.
          A refresh makes recent operations performed on one or more indices available for search.
          For data streams, the API runs the refresh operation on the stream’s backing indices.</p>
          <p>By default, Elasticsearch periodically refreshes indices every second, but only on indices that have received one search request or more in the last 30 seconds.
          You can change this default interval with the <code>index.refresh_interval</code> setting.</p>
          <p>Refresh requests are synchronous and do not return a response until the refresh operation completes.</p>
          <p>Refreshes are resource-intensive.
          To ensure good cluster performance, it's recommended to wait for Elasticsearch's periodic refresh rather than performing an explicit refresh when possible.</p>
          <p>If your application workflow indexes documents and then runs a search to retrieve the indexed document, it's recommended to use the index API's <code>refresh=wait_for</code> query parameter option.
          This option ensures the indexing operation waits for a periodic refresh before running the search.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-refresh>`_

        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (`*`). To target all data streams
            and indices, omit this parameter or use `*` or `_all`.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_refresh'
        else:
            __path_parts = {}
            __path = "/_refresh"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.refresh",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def resolve_index(
        self,
        *,
        name: t.Union[str, t.Sequence[str]],
        allow_no_indices: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Resolve indices.
          Resolve the names and/or index patterns for indices, aliases, and data streams.
          Multiple patterns and remote clusters are supported.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-resolve-index>`_

        :param name: Comma-separated name(s) or index pattern(s) of the indices, aliases,
            and data streams to resolve. Resources on remote clusters can be specified
            using the `<cluster>`:`<name>` syntax.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices. For
            example, a request targeting `foo*,bar*` returns an error if an index starts
            with `foo` but no index starts with `bar`.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_resolve/index/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.resolve_index",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("aliases", "conditions", "mappings", "settings"),
    )
    async def rollover(
        self,
        *,
        alias: str,
        new_index: t.Optional[str] = None,
        aliases: t.Optional[t.Mapping[str, t.Mapping[str, t.Any]]] = None,
        conditions: t.Optional[t.Mapping[str, t.Any]] = None,
        dry_run: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        mappings: t.Optional[t.Mapping[str, t.Any]] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        settings: t.Optional[t.Mapping[str, t.Any]] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        wait_for_active_shards: t.Optional[
            t.Union[int, t.Union[str, t.Literal["all", "index-setting"]]]
        ] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Roll over to a new index.
          TIP: It is recommended to use the index lifecycle rollover action to automate rollovers.</p>
          <p>The rollover API creates a new index for a data stream or index alias.
          The API behavior depends on the rollover target.</p>
          <p><strong>Roll over a data stream</strong></p>
          <p>If you roll over a data stream, the API creates a new write index for the stream.
          The stream's previous write index becomes a regular backing index.
          A rollover also increments the data stream's generation.</p>
          <p><strong>Roll over an index alias with a write index</strong></p>
          <p>TIP: Prior to Elasticsearch 7.9, you'd typically use an index alias with a write index to manage time series data.
          Data streams replace this functionality, require less maintenance, and automatically integrate with data tiers.</p>
          <p>If an index alias points to multiple indices, one of the indices must be a write index.
          The rollover API creates a new write index for the alias with <code>is_write_index</code> set to <code>true</code>.
          The API also <code>sets is_write_index</code> to <code>false</code> for the previous write index.</p>
          <p><strong>Roll over an index alias with one index</strong></p>
          <p>If you roll over an index alias that points to only one index, the API creates a new index for the alias and removes the original index from the alias.</p>
          <p>NOTE: A rollover creates a new index and is subject to the <code>wait_for_active_shards</code> setting.</p>
          <p><strong>Increment index names for an alias</strong></p>
          <p>When you roll over an index alias, you can specify a name for the new index.
          If you don't specify a name and the current index ends with <code>-</code> and a number, such as <code>my-index-000001</code> or <code>my-index-3</code>, the new index name increments that number.
          For example, if you roll over an alias with a current index of <code>my-index-000001</code>, the rollover creates a new index named <code>my-index-000002</code>.
          This number is always six characters and zero-padded, regardless of the previous index's name.</p>
          <p>If you use an index alias for time series data, you can use date math in the index name to track the rollover date.
          For example, you can create an alias that points to an index named <code>&lt;my-index-{now/d}-000001&gt;</code>.
          If you create the index on May 6, 2099, the index's name is <code>my-index-2099.05.06-000001</code>.
          If you roll over the alias on May 7, 2099, the new index's name is <code>my-index-2099.05.07-000002</code>.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-rollover>`_

        :param alias: Name of the data stream or index alias to roll over.
        :param new_index: Name of the index to create. Supports date math. Data streams
            do not support this parameter.
        :param aliases: Aliases for the target index. Data streams do not support this
            parameter.
        :param conditions: Conditions for the rollover. If specified, Elasticsearch only
            performs the rollover if the current index satisfies these conditions. If
            this parameter is not specified, Elasticsearch performs the rollover unconditionally.
            If conditions are specified, at least one of them must be a `max_*` condition.
            The index will rollover if any `max_*` condition is satisfied and all `min_*`
            conditions are satisfied.
        :param dry_run: If `true`, checks whether the current index satisfies the specified
            conditions but does not perform a rollover.
        :param mappings: Mapping for fields in the index. If specified, this mapping
            can include field names, field data types, and mapping paramaters.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param settings: Configuration options for the index. Data streams do not support
            this parameter.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        :param wait_for_active_shards: The number of shard copies that must be active
            before proceeding with the operation. Set to all or any positive integer
            up to the total number of shards in the index (`number_of_replicas+1`).
        """
        if alias in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'alias'")
        __path_parts: t.Dict[str, str]
        if alias not in SKIP_IN_PATH and new_index not in SKIP_IN_PATH:
            __path_parts = {"alias": _quote(alias), "new_index": _quote(new_index)}
            __path = f'/{__path_parts["alias"]}/_rollover/{__path_parts["new_index"]}'
        elif alias not in SKIP_IN_PATH:
            __path_parts = {"alias": _quote(alias)}
            __path = f'/{__path_parts["alias"]}/_rollover'
        else:
            raise ValueError("Couldn't find a path for the given parameters")
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if dry_run is not None:
            __query["dry_run"] = dry_run
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
        if wait_for_active_shards is not None:
            __query["wait_for_active_shards"] = wait_for_active_shards
        if not __body:
            if aliases is not None:
                __body["aliases"] = aliases
            if conditions is not None:
                __body["conditions"] = conditions
            if mappings is not None:
                __body["mappings"] = mappings
            if settings is not None:
                __body["settings"] = settings
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
            endpoint_id="indices.rollover",
            path_parts=__path_parts,
        )

    @_rewrite_parameters()
    async def simulate_index_template(
        self,
        *,
        name: str,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        include_defaults: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Simulate an index.
          Get the index configuration that would be applied to the specified index from an existing index template.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-simulate-index-template>`_

        :param name: Name of the index to simulate
        :param include_defaults: If true, returns all relevant default configurations
            for the index template.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        """
        if name in SKIP_IN_PATH:
            raise ValueError("Empty value passed for parameter 'name'")
        __path_parts: t.Dict[str, str] = {"name": _quote(name)}
        __path = f'/_index_template/_simulate_index/{__path_parts["name"]}'
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        __headers = {"accept": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            endpoint_id="indices.simulate_index_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=(
            "allow_auto_create",
            "composed_of",
            "data_stream",
            "deprecated",
            "ignore_missing_component_templates",
            "index_patterns",
            "meta",
            "priority",
            "template",
            "version",
        ),
        parameter_aliases={"_meta": "meta"},
    )
    async def simulate_template(
        self,
        *,
        name: t.Optional[str] = None,
        allow_auto_create: t.Optional[bool] = None,
        composed_of: t.Optional[t.Sequence[str]] = None,
        create: t.Optional[bool] = None,
        data_stream: t.Optional[t.Mapping[str, t.Any]] = None,
        deprecated: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_missing_component_templates: t.Optional[t.Sequence[str]] = None,
        include_defaults: t.Optional[bool] = None,
        index_patterns: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        meta: t.Optional[t.Mapping[str, t.Any]] = None,
        pretty: t.Optional[bool] = None,
        priority: t.Optional[int] = None,
        template: t.Optional[t.Mapping[str, t.Any]] = None,
        version: t.Optional[int] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Simulate an index template.
          Get the index configuration that would be applied by a particular index template.</p>


        `<https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-simulate-template>`_

        :param name: Name of the index template to simulate. To test a template configuration
            before you add it to the cluster, omit this parameter and specify the template
            configuration in the request body.
        :param allow_auto_create: This setting overrides the value of the `action.auto_create_index`
            cluster setting. If set to `true` in a template, then indices can be automatically
            created using that template even if auto-creation of indices is disabled
            via `actions.auto_create_index`. If set to `false`, then indices or data
            streams matching the template must always be explicitly created, and may
            never be automatically created.
        :param composed_of: An ordered list of component template names. Component templates
            are merged in the order specified, meaning that the last component template
            specified has the highest precedence.
        :param create: If true, the template passed in the body is only used if no existing
            templates match the same index patterns. If false, the simulation uses the
            template with the highest priority. Note that the template is not permanently
            added or updated in either case; it is only used for the simulation.
        :param data_stream: If this object is included, the template is used to create
            data streams and their backing indices. Supports an empty object. Data streams
            require a matching index template with a `data_stream` object.
        :param deprecated: Marks this index template as deprecated. When creating or
            updating a non-deprecated index template that uses deprecated components,
            Elasticsearch will emit a deprecation warning.
        :param ignore_missing_component_templates: The configuration option ignore_missing_component_templates
            can be used when an index template references a component template that might
            not exist
        :param include_defaults: If true, returns all relevant default configurations
            for the index template.
        :param index_patterns: Array of wildcard (`*`) expressions used to match the
            names of data streams and indices during creation.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param meta: Optional user metadata about the index template. May have any contents.
            This map is not automatically generated by Elasticsearch.
        :param priority: Priority to determine index template precedence when a new data
            stream or index is created. The index template with the highest priority
            is chosen. If no priority is specified the template is treated as though
            it is of priority 0 (lowest priority). This number is not automatically generated
            by Elasticsearch.
        :param template: Template to be applied. It may optionally include an `aliases`,
            `mappings`, or `settings` configuration.
        :param version: Version number used to manage index templates externally. This
            number is not automatically generated by Elasticsearch.
        """
        __path_parts: t.Dict[str, str]
        if name not in SKIP_IN_PATH:
            __path_parts = {"name": _quote(name)}
            __path = f'/_index_template/_simulate/{__path_parts["name"]}'
        else:
            __path_parts = {}
            __path = "/_index_template/_simulate"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if create is not None:
            __query["create"] = create
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if include_defaults is not None:
            __query["include_defaults"] = include_defaults
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if not __body:
            if allow_auto_create is not None:
                __body["allow_auto_create"] = allow_auto_create
            if composed_of is not None:
                __body["composed_of"] = composed_of
            if data_stream is not None:
                __body["data_stream"] = data_stream
            if deprecated is not None:
                __body["deprecated"] = deprecated
            if ignore_missing_component_templates is not None:
                __body["ignore_missing_component_templates"] = (
                    ignore_missing_component_templates
                )
            if index_patterns is not None:
                __body["index_patterns"] = index_patterns
            if meta is not None:
                __body["_meta"] = meta
            if priority is not None:
                __body["priority"] = priority
            if template is not None:
                __body["template"] = template
            if version is not None:
                __body["version"] = version
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
            endpoint_id="indices.simulate_template",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("actions",),
    )
    async def update_aliases(
        self,
        *,
        actions: t.Optional[t.Sequence[t.Mapping[str, t.Any]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        master_timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        pretty: t.Optional[bool] = None,
        timeout: t.Optional[t.Union[str, t.Literal[-1], t.Literal[0]]] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Create or update an alias.
          Adds a data stream or index to an alias.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/indices-aliases.html>`_

        :param actions: Actions to perform.
        :param master_timeout: Period to wait for a connection to the master node. If
            no response is received before the timeout expires, the request fails and
            returns an error.
        :param timeout: Period to wait for a response. If no response is received before
            the timeout expires, the request fails and returns an error.
        """
        __path_parts: t.Dict[str, str] = {}
        __path = "/_aliases"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
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
        if not __body:
            if actions is not None:
                __body["actions"] = actions
        __headers = {"accept": "application/json", "content-type": "application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "POST",
            __path,
            params=__query,
            headers=__headers,
            body=__body,
            endpoint_id="indices.update_aliases",
            path_parts=__path_parts,
        )

    @_rewrite_parameters(
        body_fields=("query",),
    )
    async def validate_query(
        self,
        *,
        index: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        all_shards: t.Optional[bool] = None,
        allow_no_indices: t.Optional[bool] = None,
        analyze_wildcard: t.Optional[bool] = None,
        analyzer: t.Optional[str] = None,
        default_operator: t.Optional[t.Union[str, t.Literal["and", "or"]]] = None,
        df: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Sequence[
                    t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]]
                ],
                t.Union[str, t.Literal["all", "closed", "hidden", "none", "open"]],
            ]
        ] = None,
        explain: t.Optional[bool] = None,
        filter_path: t.Optional[t.Union[str, t.Sequence[str]]] = None,
        human: t.Optional[bool] = None,
        ignore_unavailable: t.Optional[bool] = None,
        lenient: t.Optional[bool] = None,
        pretty: t.Optional[bool] = None,
        q: t.Optional[str] = None,
        query: t.Optional[t.Mapping[str, t.Any]] = None,
        rewrite: t.Optional[bool] = None,
        body: t.Optional[t.Dict[str, t.Any]] = None,
    ) -> ObjectApiResponse[t.Any]:
        """
        .. raw:: html

          <p>Validate a query.
          Validates a query without running it.</p>


        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/search-validate.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases to search.
            Supports wildcards (`*`). To search all data streams or indices, omit this
            parameter or use `*` or `_all`.
        :param all_shards: If `true`, the validation is executed on all shards instead
            of one random shard per index.
        :param allow_no_indices: If `false`, the request returns an error if any wildcard
            expression, index alias, or `_all` value targets only missing or closed indices.
            This behavior applies even if the request targets other open indices.
        :param analyze_wildcard: If `true`, wildcard and prefix queries are analyzed.
        :param analyzer: Analyzer to use for the query string. This parameter can only
            be used when the `q` query string parameter is specified.
        :param default_operator: The default operator for query string query: `AND` or
            `OR`.
        :param df: Field to use as default where no field prefix is given in the query
            string. This parameter can only be used when the `q` query string parameter
            is specified.
        :param expand_wildcards: Type of index that wildcard patterns can match. If the
            request can target data streams, this argument determines whether wildcard
            expressions match hidden data streams. Supports comma-separated values, such
            as `open,hidden`. Valid values are: `all`, `open`, `closed`, `hidden`, `none`.
        :param explain: If `true`, the response returns detailed information if an error
            has occurred.
        :param ignore_unavailable: If `false`, the request returns an error if it targets
            a missing or closed index.
        :param lenient: If `true`, format-based query failures (such as providing text
            to a numeric field) in the query string will be ignored.
        :param q: Query in the Lucene query string syntax.
        :param query: Query in the Lucene query string syntax.
        :param rewrite: If `true`, returns a more detailed explanation showing the actual
            Lucene query that will be executed.
        """
        __path_parts: t.Dict[str, str]
        if index not in SKIP_IN_PATH:
            __path_parts = {"index": _quote(index)}
            __path = f'/{__path_parts["index"]}/_validate/query'
        else:
            __path_parts = {}
            __path = "/_validate/query"
        __query: t.Dict[str, t.Any] = {}
        __body: t.Dict[str, t.Any] = body if body is not None else {}
        if all_shards is not None:
            __query["all_shards"] = all_shards
        if allow_no_indices is not None:
            __query["allow_no_indices"] = allow_no_indices
        if analyze_wildcard is not None:
            __query["analyze_wildcard"] = analyze_wildcard
        if analyzer is not None:
            __query["analyzer"] = analyzer
        if default_operator is not None:
            __query["default_operator"] = default_operator
        if df is not None:
            __query["df"] = df
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if explain is not None:
            __query["explain"] = explain
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if human is not None:
            __query["human"] = human
        if ignore_unavailable is not None:
            __query["ignore_unavailable"] = ignore_unavailable
        if lenient is not None:
            __query["lenient"] = lenient
        if pretty is not None:
            __query["pretty"] = pretty
        if q is not None:
            __query["q"] = q
        if rewrite is not None:
            __query["rewrite"] = rewrite
        if not __body:
            if query is not None:
                __body["query"] = query
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
            endpoint_id="indices.validate_query",
            path_parts=__path_parts,
        )
