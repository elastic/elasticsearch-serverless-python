Elasticsearch Serverless Python Client
======================================

.. image:: https://img.shields.io/pypi/v/elasticsearch-serverless
   :target: https://pypi.org/project/elasticsearch-serverless

.. image:: https://img.shields.io/conda/vn/conda-forge/elasticsearch-serverless?color=blue
   :target: https://anaconda.org/conda-forge/elasticsearch-serverless

.. image:: https://static.pepy.tech/badge/elasticsearch-serverless
   :target: https://pepy.tech/project/elasticsearch-serverless?versions=*

.. image:: https://clients-ci.elastic.co/job/elastic+elasticsearch-serverless-python+main/badge/icon
   :target: https://clients-ci.elastic.co/job/elastic+elasticsearch-serverless-python+main

.. image:: https://readthedocs.org/projects/elasticsearch-serverless-python/badge/?version=latest&style=flat
   :target: https://elasticsearch-serverless-python.readthedocs.io

*The official Python client for Elasticsearch Serverless.*


Features
--------

* Translating basic Python data types to and from JSON
* Configurable automatic discovery of cluster nodes
* Persistent connections
* Load balancing (with pluggable selection strategy) across available nodes
* Failed connection penalization (time based - failed connections won't be
  retried until a timeout is reached)
* Support for TLS and HTTP authentication
* Thread safety across requests
* Pluggable architecture
* Helper functions for idiomatically using APIs together


Installation
------------

Install the ``elasticsearch-serverless`` package with `pip
<https://pypi.org/project/elasticsearch-serverless>`_::

    $ python -m pip install elasticsearch-serverless

If your application uses async/await in Python you can install with
the ``async`` extra::

    $ python -m pip install elasticsearch-serverless[async]

Read more about `how to use asyncio with this project <https://elasticsearch-serverless-python.readthedocs.io/en/latest/async.html>`_.


Compatibility
-------------

TODO


Documentation
-------------

Documentation for the client is `available on elastic.co`_ and `Read the Docs`_.

.. _available on elastic.co: https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html
.. _Read the Docs: https://elasticsearch-serverless-python.readthedocs.io

Quick Start
-----------

.. code-block:: python

    # Import the client from the 'elasticsearch' module
    >>> from elasticsearch_serverless import Elasticsearch

    # Instantiate a client instance
    >>> client = Elasticsearch("http://localhost:9200")

    # Call an API, in this example `info()`
    >>> resp = client.info()

    # View the result
    >>> resp
    {
      "name" : "instance-name",
      "cluster_name" : "cluster-name",
      "cluster_uuid" : "cluster-uuid",
      "version" : {
        "number" : "7.14.0",
        ...
      },
      "tagline" : "You know, for Search"
    }


You can read more about `configuring the client`_ in the documentation.

.. _configuring the client: https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/connecting.html


License
-------

Copyright 2023 Elasticsearch B.V. Licensed under the Apache License, Version 2.0.
