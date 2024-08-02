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


Elasticsearch
-------------

.. py:module:: elasticsearch_serverless

.. autoclass:: Elasticsearch
   :members:

.. py:module:: elasticsearch_serverless.client

Async Search
------------

.. autoclass:: AsyncSearchClient
   :members:

Cat
---

.. autoclass:: CatClient
   :members:

Cluster
-------

.. autoclass:: ClusterClient
   :members:

Connector
---------
.. py:module:: elasticsearch.client
   :noindex:

.. autoclass:: ConnectorClient
   :members:

Enrich Policies
---------------

.. autoclass:: EnrichClient
   :members:

Event Query Language (EQL)
--------------------------

.. autoclass:: EqlClient
   :members:


ES|QL
-----

.. autoclass:: EqlClient
   :members:

Graph Explore
-------------

.. autoclass:: GraphClient
   :members:

Indices
-------

.. autoclass:: IndicesClient
   :members:

Inference
---------

.. autoclass:: InferenceClient
   :members:

Ingest Pipelines
----------------

.. autoclass:: IngestClient
   :members:

License
-------

.. autoclass:: LicenseClient
   :members:

Logstash
--------

.. autoclass:: LogstashClient
   :members:

Machine Learning (ML)
---------------------

.. autoclass:: MlClient
   :members:

Monitoring
----------

.. autoclass:: MonitoringClient
   :members:

Security
--------

.. autoclass:: SecurityClient
   :members:

SQL
---

.. autoclass:: SqlClient
   :members:

Tasks
-----

.. autoclass:: TasksClient
   :members:

Transforms
----------

.. autoclass:: TransformClient
   :members:
