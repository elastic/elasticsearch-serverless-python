.. _api:

Elasticsearch API Reference
===========================

All the API calls map the raw REST API as closely as possible, including the
distinction between required and optional arguments to the calls. Keyword
arguments are required for all 

.. note::

   Some API parameters in Elasticsearch are reserved keywords in Python.
   For example the ``from`` query parameter for pagination would be
   aliased as ``from_``.



.. toctree::
   :maxdepth: 1

   api/elasticsearch
   api/async-search
   api/cat
   api/cluster
   api/connector
   api/enrich-policies
   api/eql
   api/esql
   api/indices
   api/inference
   api/ingest-pipelines
   api/license
   api/logstash
   api/ml
   api/query-rules
   api/search-application
   api/security
   api/sql
   api/synonyms
   api/tasks
   api/transforms
