# Elasticsearch Serverless Python Client

<p align="center">
  <a href="https://pypi.org/project/elasticsearch-serverless/"><img alt="PyPI Version" src="https://img.shields.io/pypi/v/elasticsearch-serverless" /></a>
  <a href="https://pypi.org/project/elasticsearch-serverless/"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/elasticsearch-serverless" /></a>
  <a href="https://pepy.tech/project/elasticsearch-serverless?versions=*"><img alt="Downloads" src="https://static.pepy.tech/badge/elasticsearch-serverless" /></a>
  <a href="https://elasticsearch-serverless-python.readthedocs.io/"><img alt="Documentation Status" src="https://readthedocs.org/projects/elasticsearch-serverless-python/badge/?version=latest" /></a>
</p>

> [!WARNING]
> Starting with the release of the Elastic Stack 9.0.0, this client will be discontinued. Instead, you can use the latest version of the [Elasticsearch Python Client](https://github.com/elastic/elasticsearch-py) to build your Elasticsearch Serverless Python applications.

## Features

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

## Quick Start


```python
# Import the client from the 'elasticsearch' module
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
```

## License

This software is licensed under the [Apache License 2.0](./LICENSE). See [NOTICE](./NOTICE).
