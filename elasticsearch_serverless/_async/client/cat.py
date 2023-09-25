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

from elastic_transport import ObjectApiResponse, TextApiResponse

from ._base import NamespacedClient
from .utils import SKIP_IN_PATH, _quote, _rewrite_parameters


class CatClient(NamespacedClient):
    @_rewrite_parameters()
    async def aliases(
        self,
        *,
        name: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['all', 'closed', 'hidden', 'none', 'open']", str
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['all', 'closed', 'hidden', 'none', 'open']", str
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Shows information about currently configured aliases to indices including filter
        and routing infos.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-alias.html>`_

        :param name: A comma-separated list of aliases to retrieve. Supports wildcards
            (`*`). To retrieve all aliases, omit this parameter or use `*` or `_all`.
        :param expand_wildcards: Whether to expand wildcard expression to concrete indices
            that are open, closed or both.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: List of columns to appear in the response. Supports simple wildcards.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: List of columns that determine how the table should be sorted. Sorting
            defaults to ascending and can be changed by setting `:asc` or `:desc` as
            a suffix to the column name.
        :param v: When set to `true` will enable verbose output.
        """
        if name not in SKIP_IN_PATH:
            __path = f"/_cat/aliases/{_quote(name)}"
        else:
            __path = "/_cat/aliases"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def component_templates(
        self,
        *,
        name: t.Optional[str] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Returns information about existing component_templates templates.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-component-templates.html>`_

        :param name: The name of the component template. Accepts wildcard expressions.
            If omitted, all component templates are returned.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: List of columns to appear in the response. Supports simple wildcards.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: List of columns that determine how the table should be sorted. Sorting
            defaults to ascending and can be changed by setting `:asc` or `:desc` as
            a suffix to the column name.
        :param v: When set to `true` will enable verbose output.
        """
        if name not in SKIP_IN_PATH:
            __path = f"/_cat/component_templates/{_quote(name)}"
        else:
            __path = "/_cat/component_templates"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def count(
        self,
        *,
        index: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Provides quick access to the document count of the entire cluster, or individual
        indices.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-count.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (`*`). To target all data streams
            and indices, omit this parameter or use `*` or `_all`.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: List of columns to appear in the response. Supports simple wildcards.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: List of columns that determine how the table should be sorted. Sorting
            defaults to ascending and can be changed by setting `:asc` or `:desc` as
            a suffix to the column name.
        :param v: When set to `true` will enable verbose output.
        """
        if index not in SKIP_IN_PATH:
            __path = f"/_cat/count/{_quote(index)}"
        else:
            __path = "/_cat/count"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def help(
        self,
        *,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        v: t.Optional[bool] = None,
    ) -> TextApiResponse:
        """
        Returns help for the Cat APIs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat.html>`_

        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: List of columns to appear in the response. Supports simple wildcards.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: List of columns that determine how the table should be sorted. Sorting
            defaults to ascending and can be changed by setting `:asc` or `:desc` as
            a suffix to the column name.
        :param v: When set to `true` will enable verbose output.
        """
        __path = "/_cat"
        __query: t.Dict[str, t.Any] = {}
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def indices(
        self,
        *,
        index: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        bytes: t.Optional[
            t.Union["t.Literal['b', 'gb', 'kb', 'mb', 'pb', 'tb']", str]
        ] = None,
        error_trace: t.Optional[bool] = None,
        expand_wildcards: t.Optional[
            t.Union[
                t.Union["t.Literal['all', 'closed', 'hidden', 'none', 'open']", str],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['all', 'closed', 'hidden', 'none', 'open']", str
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['all', 'closed', 'hidden', 'none', 'open']", str
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        health: t.Optional[t.Union["t.Literal['green', 'red', 'yellow']", str]] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        include_unloaded_segments: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        pri: t.Optional[bool] = None,
        s: t.Optional[t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]] = None,
        time: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Returns information about indices: number of primaries and replicas, document
        counts, disk size, ...

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-indices.html>`_

        :param index: Comma-separated list of data streams, indices, and aliases used
            to limit the request. Supports wildcards (`*`). To target all data streams
            and indices, omit this parameter or use `*` or `_all`.
        :param bytes: The unit used to display byte values.
        :param expand_wildcards: The type of index that wildcard patterns can match.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: List of columns to appear in the response. Supports simple wildcards.
        :param health: The health status used to limit returned indices. By default,
            the response includes indices of any health status.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param include_unloaded_segments: If true, the response includes information
            from segments that are not loaded into memory.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param pri: If true, the response only includes information from primary shards.
        :param s: List of columns that determine how the table should be sorted. Sorting
            defaults to ascending and can be changed by setting `:asc` or `:desc` as
            a suffix to the column name.
        :param time: The unit used to display time values.
        :param v: When set to `true` will enable verbose output.
        """
        if index not in SKIP_IN_PATH:
            __path = f"/_cat/indices/{_quote(index)}"
        else:
            __path = "/_cat/indices"
        __query: t.Dict[str, t.Any] = {}
        if bytes is not None:
            __query["bytes"] = bytes
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if expand_wildcards is not None:
            __query["expand_wildcards"] = expand_wildcards
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if health is not None:
            __query["health"] = health
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if include_unloaded_segments is not None:
            __query["include_unloaded_segments"] = include_unloaded_segments
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if pri is not None:
            __query["pri"] = pri
        if s is not None:
            __query["s"] = s
        if time is not None:
            __query["time"] = time
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def ml_data_frame_analytics(
        self,
        *,
        id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        bytes: t.Optional[
            t.Union["t.Literal['b', 'gb', 'kb', 'mb', 'pb', 'tb']", str]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['assignment_explanation', 'create_time', 'description', 'dest_index', 'failure_reason', 'id', 'model_memory_limit', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'progress', 'source_index', 'state', 'type', 'version']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['assignment_explanation', 'create_time', 'description', 'dest_index', 'failure_reason', 'id', 'model_memory_limit', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'progress', 'source_index', 'state', 'type', 'version']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['assignment_explanation', 'create_time', 'description', 'dest_index', 'failure_reason', 'id', 'model_memory_limit', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'progress', 'source_index', 'state', 'type', 'version']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['assignment_explanation', 'create_time', 'description', 'dest_index', 'failure_reason', 'id', 'model_memory_limit', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'progress', 'source_index', 'state', 'type', 'version']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['assignment_explanation', 'create_time', 'description', 'dest_index', 'failure_reason', 'id', 'model_memory_limit', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'progress', 'source_index', 'state', 'type', 'version']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['assignment_explanation', 'create_time', 'description', 'dest_index', 'failure_reason', 'id', 'model_memory_limit', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'progress', 'source_index', 'state', 'type', 'version']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        time: t.Optional[t.Union["t.Literal[-1]", "t.Literal[0]", str]] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Gets configuration and usage information about data frame analytics jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-dfanalytics.html>`_

        :param id: The ID of the data frame analytics to fetch
        :param allow_no_match: Whether to ignore if a wildcard expression matches no
            configs. (This includes `_all` string or when no configs have been specified)
        :param bytes: The unit in which to display byte values
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: Comma-separated list of column names to display.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: Comma-separated list of column names or column aliases used to sort
            the response.
        :param time: Unit used to display time values.
        :param v: When set to `true` will enable verbose output.
        """
        if id not in SKIP_IN_PATH:
            __path = f"/_cat/ml/data_frame/analytics/{_quote(id)}"
        else:
            __path = "/_cat/ml/data_frame/analytics"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if bytes is not None:
            __query["bytes"] = bytes
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if time is not None:
            __query["time"] = time
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def ml_datafeeds(
        self,
        *,
        datafeed_id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['ae', 'bc', 'id', 'na', 'ne', 'ni', 'nn', 's', 'sba', 'sc', 'seah', 'st']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['ae', 'bc', 'id', 'na', 'ne', 'ni', 'nn', 's', 'sba', 'sc', 'seah', 'st']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['ae', 'bc', 'id', 'na', 'ne', 'ni', 'nn', 's', 'sba', 'sc', 'seah', 'st']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['ae', 'bc', 'id', 'na', 'ne', 'ni', 'nn', 's', 'sba', 'sc', 'seah', 'st']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['ae', 'bc', 'id', 'na', 'ne', 'ni', 'nn', 's', 'sba', 'sc', 'seah', 'st']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['ae', 'bc', 'id', 'na', 'ne', 'ni', 'nn', 's', 'sba', 'sc', 'seah', 'st']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        time: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Gets configuration and usage information about datafeeds.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-datafeeds.html>`_

        :param datafeed_id: A numerical character string that uniquely identifies the
            datafeed.
        :param allow_no_match: Specifies what to do when the request: * Contains wildcard
            expressions and there are no datafeeds that match. * Contains the `_all`
            string or no identifiers and there are no matches. * Contains wildcard expressions
            and there are only partial matches. If `true`, the API returns an empty datafeeds
            array when there are no matches and the subset of results when there are
            partial matches. If `false`, the API returns a 404 status code when there
            are no matches or only partial matches.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: Comma-separated list of column names to display.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: Comma-separated list of column names or column aliases used to sort
            the response.
        :param time: The unit used to display time values.
        :param v: When set to `true` will enable verbose output.
        """
        if datafeed_id not in SKIP_IN_PATH:
            __path = f"/_cat/ml/datafeeds/{_quote(datafeed_id)}"
        else:
            __path = "/_cat/ml/datafeeds"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if time is not None:
            __query["time"] = time
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters()
    async def ml_jobs(
        self,
        *,
        job_id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        bytes: t.Optional[
            t.Union["t.Literal['b', 'gb', 'kb', 'mb', 'pb', 'tb']", str]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        h: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['assignment_explanation', 'buckets.count', 'buckets.time.exp_avg', 'buckets.time.exp_avg_hour', 'buckets.time.max', 'buckets.time.min', 'buckets.time.total', 'data.buckets', 'data.earliest_record', 'data.empty_buckets', 'data.input_bytes', 'data.input_fields', 'data.input_records', 'data.invalid_dates', 'data.last', 'data.last_empty_bucket', 'data.last_sparse_bucket', 'data.latest_record', 'data.missing_fields', 'data.out_of_order_timestamps', 'data.processed_fields', 'data.processed_records', 'data.sparse_buckets', 'forecasts.memory.avg', 'forecasts.memory.max', 'forecasts.memory.min', 'forecasts.memory.total', 'forecasts.records.avg', 'forecasts.records.max', 'forecasts.records.min', 'forecasts.records.total', 'forecasts.time.avg', 'forecasts.time.max', 'forecasts.time.min', 'forecasts.time.total', 'forecasts.total', 'id', 'model.bucket_allocation_failures', 'model.by_fields', 'model.bytes', 'model.bytes_exceeded', 'model.categorization_status', 'model.categorized_doc_count', 'model.dead_category_count', 'model.failed_category_count', 'model.frequent_category_count', 'model.log_time', 'model.memory_limit', 'model.memory_status', 'model.over_fields', 'model.partition_fields', 'model.rare_category_count', 'model.timestamp', 'model.total_category_count', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'opened_time', 'state']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['assignment_explanation', 'buckets.count', 'buckets.time.exp_avg', 'buckets.time.exp_avg_hour', 'buckets.time.max', 'buckets.time.min', 'buckets.time.total', 'data.buckets', 'data.earliest_record', 'data.empty_buckets', 'data.input_bytes', 'data.input_fields', 'data.input_records', 'data.invalid_dates', 'data.last', 'data.last_empty_bucket', 'data.last_sparse_bucket', 'data.latest_record', 'data.missing_fields', 'data.out_of_order_timestamps', 'data.processed_fields', 'data.processed_records', 'data.sparse_buckets', 'forecasts.memory.avg', 'forecasts.memory.max', 'forecasts.memory.min', 'forecasts.memory.total', 'forecasts.records.avg', 'forecasts.records.max', 'forecasts.records.min', 'forecasts.records.total', 'forecasts.time.avg', 'forecasts.time.max', 'forecasts.time.min', 'forecasts.time.total', 'forecasts.total', 'id', 'model.bucket_allocation_failures', 'model.by_fields', 'model.bytes', 'model.bytes_exceeded', 'model.categorization_status', 'model.categorized_doc_count', 'model.dead_category_count', 'model.failed_category_count', 'model.frequent_category_count', 'model.log_time', 'model.memory_limit', 'model.memory_status', 'model.over_fields', 'model.partition_fields', 'model.rare_category_count', 'model.timestamp', 'model.total_category_count', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'opened_time', 'state']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['assignment_explanation', 'buckets.count', 'buckets.time.exp_avg', 'buckets.time.exp_avg_hour', 'buckets.time.max', 'buckets.time.min', 'buckets.time.total', 'data.buckets', 'data.earliest_record', 'data.empty_buckets', 'data.input_bytes', 'data.input_fields', 'data.input_records', 'data.invalid_dates', 'data.last', 'data.last_empty_bucket', 'data.last_sparse_bucket', 'data.latest_record', 'data.missing_fields', 'data.out_of_order_timestamps', 'data.processed_fields', 'data.processed_records', 'data.sparse_buckets', 'forecasts.memory.avg', 'forecasts.memory.max', 'forecasts.memory.min', 'forecasts.memory.total', 'forecasts.records.avg', 'forecasts.records.max', 'forecasts.records.min', 'forecasts.records.total', 'forecasts.time.avg', 'forecasts.time.max', 'forecasts.time.min', 'forecasts.time.total', 'forecasts.total', 'id', 'model.bucket_allocation_failures', 'model.by_fields', 'model.bytes', 'model.bytes_exceeded', 'model.categorization_status', 'model.categorized_doc_count', 'model.dead_category_count', 'model.failed_category_count', 'model.frequent_category_count', 'model.log_time', 'model.memory_limit', 'model.memory_status', 'model.over_fields', 'model.partition_fields', 'model.rare_category_count', 'model.timestamp', 'model.total_category_count', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'opened_time', 'state']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['assignment_explanation', 'buckets.count', 'buckets.time.exp_avg', 'buckets.time.exp_avg_hour', 'buckets.time.max', 'buckets.time.min', 'buckets.time.total', 'data.buckets', 'data.earliest_record', 'data.empty_buckets', 'data.input_bytes', 'data.input_fields', 'data.input_records', 'data.invalid_dates', 'data.last', 'data.last_empty_bucket', 'data.last_sparse_bucket', 'data.latest_record', 'data.missing_fields', 'data.out_of_order_timestamps', 'data.processed_fields', 'data.processed_records', 'data.sparse_buckets', 'forecasts.memory.avg', 'forecasts.memory.max', 'forecasts.memory.min', 'forecasts.memory.total', 'forecasts.records.avg', 'forecasts.records.max', 'forecasts.records.min', 'forecasts.records.total', 'forecasts.time.avg', 'forecasts.time.max', 'forecasts.time.min', 'forecasts.time.total', 'forecasts.total', 'id', 'model.bucket_allocation_failures', 'model.by_fields', 'model.bytes', 'model.bytes_exceeded', 'model.categorization_status', 'model.categorized_doc_count', 'model.dead_category_count', 'model.failed_category_count', 'model.frequent_category_count', 'model.log_time', 'model.memory_limit', 'model.memory_status', 'model.over_fields', 'model.partition_fields', 'model.rare_category_count', 'model.timestamp', 'model.total_category_count', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'opened_time', 'state']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['assignment_explanation', 'buckets.count', 'buckets.time.exp_avg', 'buckets.time.exp_avg_hour', 'buckets.time.max', 'buckets.time.min', 'buckets.time.total', 'data.buckets', 'data.earliest_record', 'data.empty_buckets', 'data.input_bytes', 'data.input_fields', 'data.input_records', 'data.invalid_dates', 'data.last', 'data.last_empty_bucket', 'data.last_sparse_bucket', 'data.latest_record', 'data.missing_fields', 'data.out_of_order_timestamps', 'data.processed_fields', 'data.processed_records', 'data.sparse_buckets', 'forecasts.memory.avg', 'forecasts.memory.max', 'forecasts.memory.min', 'forecasts.memory.total', 'forecasts.records.avg', 'forecasts.records.max', 'forecasts.records.min', 'forecasts.records.total', 'forecasts.time.avg', 'forecasts.time.max', 'forecasts.time.min', 'forecasts.time.total', 'forecasts.total', 'id', 'model.bucket_allocation_failures', 'model.by_fields', 'model.bytes', 'model.bytes_exceeded', 'model.categorization_status', 'model.categorized_doc_count', 'model.dead_category_count', 'model.failed_category_count', 'model.frequent_category_count', 'model.log_time', 'model.memory_limit', 'model.memory_status', 'model.over_fields', 'model.partition_fields', 'model.rare_category_count', 'model.timestamp', 'model.total_category_count', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'opened_time', 'state']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['assignment_explanation', 'buckets.count', 'buckets.time.exp_avg', 'buckets.time.exp_avg_hour', 'buckets.time.max', 'buckets.time.min', 'buckets.time.total', 'data.buckets', 'data.earliest_record', 'data.empty_buckets', 'data.input_bytes', 'data.input_fields', 'data.input_records', 'data.invalid_dates', 'data.last', 'data.last_empty_bucket', 'data.last_sparse_bucket', 'data.latest_record', 'data.missing_fields', 'data.out_of_order_timestamps', 'data.processed_fields', 'data.processed_records', 'data.sparse_buckets', 'forecasts.memory.avg', 'forecasts.memory.max', 'forecasts.memory.min', 'forecasts.memory.total', 'forecasts.records.avg', 'forecasts.records.max', 'forecasts.records.min', 'forecasts.records.total', 'forecasts.time.avg', 'forecasts.time.max', 'forecasts.time.min', 'forecasts.time.total', 'forecasts.total', 'id', 'model.bucket_allocation_failures', 'model.by_fields', 'model.bytes', 'model.bytes_exceeded', 'model.categorization_status', 'model.categorized_doc_count', 'model.dead_category_count', 'model.failed_category_count', 'model.frequent_category_count', 'model.log_time', 'model.memory_limit', 'model.memory_status', 'model.over_fields', 'model.partition_fields', 'model.rare_category_count', 'model.timestamp', 'model.total_category_count', 'node.address', 'node.ephemeral_id', 'node.id', 'node.name', 'opened_time', 'state']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        time: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Gets configuration and usage information about anomaly detection jobs.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-anomaly-detectors.html>`_

        :param job_id: Identifier for the anomaly detection job.
        :param allow_no_match: Specifies what to do when the request: * Contains wildcard
            expressions and there are no jobs that match. * Contains the `_all` string
            or no identifiers and there are no matches. * Contains wildcard expressions
            and there are only partial matches. If `true`, the API returns an empty jobs
            array when there are no matches and the subset of results when there are
            partial matches. If `false`, the API returns a 404 status code when there
            are no matches or only partial matches.
        :param bytes: The unit used to display byte values.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param h: Comma-separated list of column names to display.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: Comma-separated list of column names or column aliases used to sort
            the response.
        :param time: The unit used to display time values.
        :param v: When set to `true` will enable verbose output.
        """
        if job_id not in SKIP_IN_PATH:
            __path = f"/_cat/ml/anomaly_detectors/{_quote(job_id)}"
        else:
            __path = "/_cat/ml/anomaly_detectors"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if bytes is not None:
            __query["bytes"] = bytes
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if time is not None:
            __query["time"] = time
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    async def ml_trained_models(
        self,
        *,
        model_id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        bytes: t.Optional[
            t.Union["t.Literal['b', 'gb', 'kb', 'mb', 'pb', 'tb']", str]
        ] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        from_: t.Optional[int] = None,
        h: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['create_time', 'created_by', 'data_frame_analytics_id', 'description', 'heap_size', 'id', 'ingest.count', 'ingest.current', 'ingest.failed', 'ingest.pipelines', 'ingest.time', 'license', 'operations', 'version']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['create_time', 'created_by', 'data_frame_analytics_id', 'description', 'heap_size', 'id', 'ingest.count', 'ingest.current', 'ingest.failed', 'ingest.pipelines', 'ingest.time', 'license', 'operations', 'version']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['create_time', 'created_by', 'data_frame_analytics_id', 'description', 'heap_size', 'id', 'ingest.count', 'ingest.current', 'ingest.failed', 'ingest.pipelines', 'ingest.time', 'license', 'operations', 'version']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['create_time', 'created_by', 'data_frame_analytics_id', 'description', 'heap_size', 'id', 'ingest.count', 'ingest.current', 'ingest.failed', 'ingest.pipelines', 'ingest.time', 'license', 'operations', 'version']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['create_time', 'created_by', 'data_frame_analytics_id', 'description', 'heap_size', 'id', 'ingest.count', 'ingest.current', 'ingest.failed', 'ingest.pipelines', 'ingest.time', 'license', 'operations', 'version']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['create_time', 'created_by', 'data_frame_analytics_id', 'description', 'heap_size', 'id', 'ingest.count', 'ingest.current', 'ingest.failed', 'ingest.pipelines', 'ingest.time', 'license', 'operations', 'version']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        size: t.Optional[int] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Gets configuration and usage information about inference trained models.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-trained-model.html>`_

        :param model_id: A unique identifier for the trained model.
        :param allow_no_match: Specifies what to do when the request: contains wildcard
            expressions and there are no models that match; contains the `_all` string
            or no identifiers and there are no matches; contains wildcard expressions
            and there are only partial matches. If `true`, the API returns an empty array
            when there are no matches and the subset of results when there are partial
            matches. If `false`, the API returns a 404 status code when there are no
            matches or only partial matches.
        :param bytes: The unit used to display byte values.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param from_: Skips the specified number of transforms.
        :param h: A comma-separated list of column names to display.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: A comma-separated list of column names or aliases used to sort the
            response.
        :param size: The maximum number of transforms to display.
        :param v: When set to `true` will enable verbose output.
        """
        if model_id not in SKIP_IN_PATH:
            __path = f"/_cat/ml/trained_models/{_quote(model_id)}"
        else:
            __path = "/_cat/ml/trained_models"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if bytes is not None:
            __query["bytes"] = bytes
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if from_ is not None:
            __query["from"] = from_
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if size is not None:
            __query["size"] = size
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )

    @_rewrite_parameters(
        parameter_aliases={"from": "from_"},
    )
    async def transforms(
        self,
        *,
        transform_id: t.Optional[str] = None,
        allow_no_match: t.Optional[bool] = None,
        error_trace: t.Optional[bool] = None,
        filter_path: t.Optional[
            t.Union[str, t.Union[t.List[str], t.Tuple[str, ...]]]
        ] = None,
        format: t.Optional[str] = None,
        from_: t.Optional[int] = None,
        h: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['changes_last_detection_time', 'checkpoint', 'checkpoint_duration_time_exp_avg', 'checkpoint_progress', 'create_time', 'delete_time', 'description', 'dest_index', 'docs_per_second', 'documents_deleted', 'documents_indexed', 'documents_processed', 'frequency', 'id', 'index_failure', 'index_time', 'index_total', 'indexed_documents_exp_avg', 'last_search_time', 'max_page_search_size', 'pages_processed', 'pipeline', 'processed_documents_exp_avg', 'processing_time', 'reason', 'search_failure', 'search_time', 'search_total', 'source_index', 'state', 'transform_type', 'trigger_count', 'version']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['changes_last_detection_time', 'checkpoint', 'checkpoint_duration_time_exp_avg', 'checkpoint_progress', 'create_time', 'delete_time', 'description', 'dest_index', 'docs_per_second', 'documents_deleted', 'documents_indexed', 'documents_processed', 'frequency', 'id', 'index_failure', 'index_time', 'index_total', 'indexed_documents_exp_avg', 'last_search_time', 'max_page_search_size', 'pages_processed', 'pipeline', 'processed_documents_exp_avg', 'processing_time', 'reason', 'search_failure', 'search_time', 'search_total', 'source_index', 'state', 'transform_type', 'trigger_count', 'version']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['changes_last_detection_time', 'checkpoint', 'checkpoint_duration_time_exp_avg', 'checkpoint_progress', 'create_time', 'delete_time', 'description', 'dest_index', 'docs_per_second', 'documents_deleted', 'documents_indexed', 'documents_processed', 'frequency', 'id', 'index_failure', 'index_time', 'index_total', 'indexed_documents_exp_avg', 'last_search_time', 'max_page_search_size', 'pages_processed', 'pipeline', 'processed_documents_exp_avg', 'processing_time', 'reason', 'search_failure', 'search_time', 'search_total', 'source_index', 'state', 'transform_type', 'trigger_count', 'version']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        help: t.Optional[bool] = None,
        human: t.Optional[bool] = None,
        local: t.Optional[bool] = None,
        master_timeout: t.Optional[
            t.Union["t.Literal[-1]", "t.Literal[0]", str]
        ] = None,
        pretty: t.Optional[bool] = None,
        s: t.Optional[
            t.Union[
                t.Union[
                    "t.Literal['changes_last_detection_time', 'checkpoint', 'checkpoint_duration_time_exp_avg', 'checkpoint_progress', 'create_time', 'delete_time', 'description', 'dest_index', 'docs_per_second', 'documents_deleted', 'documents_indexed', 'documents_processed', 'frequency', 'id', 'index_failure', 'index_time', 'index_total', 'indexed_documents_exp_avg', 'last_search_time', 'max_page_search_size', 'pages_processed', 'pipeline', 'processed_documents_exp_avg', 'processing_time', 'reason', 'search_failure', 'search_time', 'search_total', 'source_index', 'state', 'transform_type', 'trigger_count', 'version']",
                    str,
                ],
                t.Union[
                    t.List[
                        t.Union[
                            "t.Literal['changes_last_detection_time', 'checkpoint', 'checkpoint_duration_time_exp_avg', 'checkpoint_progress', 'create_time', 'delete_time', 'description', 'dest_index', 'docs_per_second', 'documents_deleted', 'documents_indexed', 'documents_processed', 'frequency', 'id', 'index_failure', 'index_time', 'index_total', 'indexed_documents_exp_avg', 'last_search_time', 'max_page_search_size', 'pages_processed', 'pipeline', 'processed_documents_exp_avg', 'processing_time', 'reason', 'search_failure', 'search_time', 'search_total', 'source_index', 'state', 'transform_type', 'trigger_count', 'version']",
                            str,
                        ]
                    ],
                    t.Tuple[
                        t.Union[
                            "t.Literal['changes_last_detection_time', 'checkpoint', 'checkpoint_duration_time_exp_avg', 'checkpoint_progress', 'create_time', 'delete_time', 'description', 'dest_index', 'docs_per_second', 'documents_deleted', 'documents_indexed', 'documents_processed', 'frequency', 'id', 'index_failure', 'index_time', 'index_total', 'indexed_documents_exp_avg', 'last_search_time', 'max_page_search_size', 'pages_processed', 'pipeline', 'processed_documents_exp_avg', 'processing_time', 'reason', 'search_failure', 'search_time', 'search_total', 'source_index', 'state', 'transform_type', 'trigger_count', 'version']",
                            str,
                        ],
                        ...,
                    ],
                ],
            ]
        ] = None,
        size: t.Optional[int] = None,
        time: t.Optional[
            t.Union["t.Literal['d', 'h', 'm', 'micros', 'ms', 'nanos', 's']", str]
        ] = None,
        v: t.Optional[bool] = None,
    ) -> t.Union[ObjectApiResponse[t.Any], TextApiResponse]:
        """
        Gets configuration and usage information about transforms.

        `<https://www.elastic.co/guide/en/elasticsearch/reference/master/cat-transforms.html>`_

        :param transform_id: A transform identifier or a wildcard expression. If you
            do not specify one of these options, the API returns information for all
            transforms.
        :param allow_no_match: Specifies what to do when the request: contains wildcard
            expressions and there are no transforms that match; contains the `_all` string
            or no identifiers and there are no matches; contains wildcard expressions
            and there are only partial matches. If `true`, it returns an empty transforms
            array when there are no matches and the subset of results when there are
            partial matches. If `false`, the request returns a 404 status code when there
            are no matches or only partial matches.
        :param format: Specifies the format to return the columnar data in, can be set
            to `text`, `json`, `cbor`, `yaml`, or `smile`.
        :param from_: Skips the specified number of transforms.
        :param h: Comma-separated list of column names to display.
        :param help: When set to `true` will output available columns. This option can't
            be combined with any other query string option.
        :param local: If `true`, the request computes the list of selected nodes from
            the local cluster state. If `false` the list of selected nodes are computed
            from the cluster state of the master node. In both cases the coordinating
            node will send requests for further information to each selected node.
        :param master_timeout: Period to wait for a connection to the master node.
        :param s: Comma-separated list of column names or column aliases used to sort
            the response.
        :param size: The maximum number of transforms to obtain.
        :param time: The unit used to display time values.
        :param v: When set to `true` will enable verbose output.
        """
        if transform_id not in SKIP_IN_PATH:
            __path = f"/_cat/transforms/{_quote(transform_id)}"
        else:
            __path = "/_cat/transforms"
        __query: t.Dict[str, t.Any] = {}
        if allow_no_match is not None:
            __query["allow_no_match"] = allow_no_match
        if error_trace is not None:
            __query["error_trace"] = error_trace
        if filter_path is not None:
            __query["filter_path"] = filter_path
        if format is not None:
            __query["format"] = format
        if from_ is not None:
            __query["from"] = from_
        if h is not None:
            __query["h"] = h
        if help is not None:
            __query["help"] = help
        if human is not None:
            __query["human"] = human
        if local is not None:
            __query["local"] = local
        if master_timeout is not None:
            __query["master_timeout"] = master_timeout
        if pretty is not None:
            __query["pretty"] = pretty
        if s is not None:
            __query["s"] = s
        if size is not None:
            __query["size"] = size
        if time is not None:
            __query["time"] = time
        if v is not None:
            __query["v"] = v
        __headers = {"accept": "text/plain,application/json"}
        return await self.perform_request(  # type: ignore[return-value]
            "GET", __path, params=__query, headers=__headers
        )
