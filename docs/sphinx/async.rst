Using Asyncio with Elasticsearch
================================

 .. py:module:: elasticsearch

For Python 3.6+ the ``elasticsearch_serverless`` package supports async/await with
`Asyncio <https://docs.python.org/3/library/asyncio.html>`_ and `Aiohttp <https://docs.aiohttp.org>`_.
You can either install ``aiohttp`` directly or use the ``[async]`` extra:

 .. code-block:: bash

    $ python -m pip install elasticsearch_serverless>=7.8.0 aiohttp

    # - OR -

    $ python -m pip install elasticsearch_serverless[async]>=7.8.0

 .. note::
    Async functionality is a new feature of this library in v7.8.0+ so
    `please open an issue <https://github.com/elastic/elasticsearch-serverless-python/issues>`_
    if you find an issue or have a question about async support.

Getting Started with Async
--------------------------

After installation all async API endpoints are available via :class:`~elasticsearch_serverless.AsyncElasticsearch`
and are used in the same way as other APIs, just with an extra ``await``:

 .. code-block:: python

    import asyncio
    from elasticsearch_serverless import AsyncElasticsearch

    es = AsyncElasticsearch()

    async def main():
        resp = await es.search(
            index="documents",
            body={"query": {"match_all": {}}},
            size=20,
        )
        print(resp)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

All APIs that are available under the sync client are also available under the async client.

ASGI Applications and Elastic APM
---------------------------------

`ASGI <https://asgi.readthedocs.io>`_ (Asynchronous Server Gateway Interface) is a new way to
serve Python web applications making use of async I/O to achieve better performance.
Some examples of ASGI frameworks include FastAPI, Django 3.0+, and Starlette.
If you're using one of these frameworks along with Elasticsearch then you
should be using :py:class:`~elasticsearch_serverless.AsyncElasticsearch` to avoid blocking
the event loop with synchronous network calls for optimal performance.

`Elastic APM <https://www.elastic.co/guide/en/apm/agent/python/current/index.html>`_
also supports tracing of async Elasticsearch queries just the same as
synchronous queries. For an example on how to configure ``AsyncElasticsearch`` with
a popular ASGI framework `FastAPI <https://fastapi.tiangolo.com/>`_ and APM tracing
there is a `pre-built example <https://github.com/elastic/elasticsearch-serverless-python/tree/main/examples/fastapi-apm>`_
in the ``examples/fastapi-apm`` directory.

Frequently Asked Questions
--------------------------

NameError / ImportError when importing ``AsyncElasticsearch``?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If when trying to use ``AsyncElasticsearch`` and you're receiving a ``NameError`` or ``ImportError``
you should ensure that you're running Python 3.6+ (check with ``$ python --version``) and
that you have ``aiohttp`` installed in your environment (check with ``$ python -m pip freeze | grep aiohttp``).
If either of the above conditions is not met then async support won't be available.

What about the ``elasticsearch-async`` package?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Previously asyncio was supported separately via the `elasticsearch-async <https://github.com/elastic/elasticsearch-py-async>`_
package. The ``elasticsearch-async`` package has been deprecated in favor of
``AsyncElasticsearch`` provided by the ``elasticsearch`` package
in v7.8 and onwards.

Receiving 'Unclosed client session / connector' warning?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This warning is created by ``aiohttp`` when an open HTTP connection is
garbage collected. You'll typically run into this when closing your application.
To resolve the issue ensure that :meth:`~elasticsearch_serverless.AsyncElasticsearch.close`
is called before the :py:class:`~elasticsearch_serverless.AsyncElasticsearch` instance is garbage collected.

For example if using FastAPI that might look like this:

 .. code-block:: python

    from fastapi import FastAPI
    from elasticsearch_serverless import AsyncElasticsearch

    app = FastAPI()
    es = AsyncElasticsearch()

    # This gets called once the app is shutting down.
    @app.on_event("shutdown")
    async def app_shutdown():
        await es.close()


Async Helpers
-------------

Async variants of all helpers are available in ``elasticsearch_serverless.helpers``
and are all prefixed with ``async_*``. You'll notice that these APIs
are identical to the ones in the sync :ref:`helpers` documentation.

All async helpers that accept an iterator or generator also accept async iterators
and async generators.

 .. py:module:: elasticsearch_serverless.helpers

Bulk and Streaming Bulk
~~~~~~~~~~~~~~~~~~~~~~~

 .. autofunction:: async_bulk

 .. code-block:: python

    import asyncio
    from elasticsearch_serverless import AsyncElasticsearch
    from elasticsearch_serverless.helpers import async_bulk

    es = AsyncElasticsearch()

    async def gendata():
        mywords = ['foo', 'bar', 'baz']
        for word in mywords:
            yield {
                "_index": "mywords",
                "doc": {"word": word},
            }

    async def main():
        await async_bulk(es, gendata())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

 .. autofunction:: async_streaming_bulk

 .. code-block:: python

    import asyncio
    from elasticsearch_serverless import AsyncElasticsearch
    from elasticsearch_serverless.helpers import async_streaming_bulk

    es = AsyncElasticsearch()

    async def gendata():
        mywords = ['foo', 'bar', 'baz']
        for word in mywords:
            yield {
                "_index": "mywords",
                "word": word,
            }

    async def main():
        async for ok, result in async_streaming_bulk(es, gendata()):
            action, result = result.popitem()
            if not ok:
                print("failed to %s document %s" % ())

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

Scan
~~~~

 .. autofunction:: async_scan

 .. code-block:: python

    import asyncio
    from elasticsearch_serverless import AsyncElasticsearch
    from elasticsearch_serverless.helpers import async_scan

    es = AsyncElasticsearch()

    async def main():
        async for doc in async_scan(
            client=es,
            query={"query": {"match": {"title": "python"}}},
            index="orders-*"
        ):
            print(doc)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

Reindex
~~~~~~~

 .. autofunction:: async_reindex


API Reference
-------------

 .. py:module:: elasticsearch_serverless

The API of :class:`~elasticsearch_serverless.AsyncElasticsearch` is nearly identical
to the API of :class:`~elasticsearch_serverless.Elasticsearch` with the exception that
every API call like :py:func:`~elasticsearch_serverless.AsyncElasticsearch.search` is
an ``async`` function and requires an ``await`` to properly return the response
body.

AsyncElasticsearch
~~~~~~~~~~~~~~~~~~

 .. note::

    To reference Elasticsearch APIs that are namespaced like ``.indices.create()``
    refer to the sync API reference. These APIs are identical between sync and async.

 .. autoclass:: AsyncElasticsearch
   :members:
