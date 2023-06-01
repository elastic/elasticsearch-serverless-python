# Elasticsearch Serverless Client

[![main](https://github.com/elastic/elasticsearch-serverless-<<[lang]>>/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/elastic/elasticsearch-serverless-<<[lang]>>/actions/workflows/tests.yml)

This is the official Elastic client for the **Elasticsearch Serverless** service. If you're looking to develop your <<[LANG]>> application with the Elasticsearch Stack, you should look at the [Elasticsearch Client](https://github.com/elastic/elasticsearch-<<[lang]>>) instead. If you're looking to develop your <<[LANG]>> application with Elastic Enterprise Search, you should look at the [Enterprise Search Client](https://github.com/elastic/enterprise-search-<<[lang]>>/).

## Installation


### Instantiate a Client


### Using the API


Once you've instantiated a client with your API key and Elasticsearch endpoint, you can start ingesting documents into Elasticsearch Service. You can use the **Bulk API** for this. This API allows you to index, update and delete several documents in one request. You call the `bulk` API on the client with a body parameter, an Array of hashes that define the action and a document. Here's an example of indexing some classic books into the `books` index:

```<<[lang]>>
# First we build our data:
body = [
  { index: { _index: 'books', data: {name: "Snow Crash", "author": "Neal Stephenson", "release_date": "1992-06-01", "page_count": 470} } },
  { index: { _index: 'books', data: {name: "Revelation Space", "author": "Alastair Reynolds", "release_date": "2000-03-15", "page_count": 585} } },
  { index: { _index: 'books', data: {name: "1984", "author": "George Orwell", "release_date": "1985-06-01", "page_count": 328} } },
  { index: { _index: 'books', data: {name: "Fahrenheit 451", "author": "Ray Bradbury", "release_date": "1953-10-15", "page_count": 227} } },
  { index: { _index: 'books', data: {name: "Brave New World", "author": "Aldous Huxley", "release_date": "1932-06-01", "page_count": 268} } },
  { index: { _index: 'books', data: {name: "The Handmaid's Tale", "author": "Margaret Atwood", "release_date": "1985-06-01", "page_count": 311} } }
]
# Then we send the data via the bulk api:
> response = client.bulk(body: body)
# And we can check that the items were indexed and given an id in the response:
> response['items']
 =>
[{"index"=>{"_index"=>"books", "_id"=>"Pdink4cBmDx329iqhzM2", "_version"=>1, "result"=>"created", "_shards"=>{"total"=>2, "successful"=>1, "failed"=>0}, "_seq_no"=>0, "_primary_term"=>1, "status"=>201}},
 {"index"=>{"_index"=>"books", "_id"=>"Ptink4cBmDx329iqhzM2", "_version"=>1, "result"=>"created", "_shards"=>{"total"=>2, "successful"=>1, "failed"=>0}, "_seq_no"=>1, "_primary_term"=>1, "status"=>201}},
 {"index"=>{"_index"=>"books", "_id"=>"P9ink4cBmDx329iqhzM2", "_version"=>1, "result"=>"created", "_shards"=>{"total"=>2, "successful"=>1, "failed"=>0}, "_seq_no"=>2, "_primary_term"=>1, "status"=>201}},
 {"index"=>{"_index"=>"books", "_id"=>"QNink4cBmDx329iqhzM2", "_version"=>1, "result"=>"created", "_shards"=>{"total"=>2, "successful"=>1, "failed"=>0}, "_seq_no"=>3, "_primary_term"=>1, "status"=>201}},
 {"index"=>{"_index"=>"books", "_id"=>"Qdink4cBmDx329iqhzM2", "_version"=>1, "result"=>"created", "_shards"=>{"total"=>2, "successful"=>1, "failed"=>0}, "_seq_no"=>4, "_primary_term"=>1, "status"=>201}},
 {"index"=>{"_index"=>"books", "_id"=>"Qtink4cBmDx329iqhzM2", "_version"=>1, "result"=>"created", "_shards"=>{"total"=>2, "successful"=>1, "failed"=>0}, "_seq_no"=>5, "_primary_term"=>1, "status"=>201}}]

```

When you use the client to make a request to Elasticsearch, it will return an API Response object. You can see the HTTP return code by calling `status` and the HTTP headers by calling `headers` on the response object. The Response object behaves as a Hash too, so you can access the body values directly as seen on the previous example with `response['items']`.

Now that some data is available, you can search your documents using the **Search API**:

```<<[lang]>>
> response = client.search(index: 'books', q: 'snow')
> response['hits']['hits']
 => [{"_index"=>"books", "_id"=>"Pdink4cBmDx329iqhzM2", "_score"=>1.5904956, "_source"=>{"name"=>"Snow Crash", "author"=>"Neal Stephenson", "release_date"=>"1992-06-01", "page_count"=>470}}]
```

## Development

See [CONTRIBUTING](./CONTRIBUTING.md).

### Docs

Some questions, assumptions and general notes about this project can be found in [the docs directory](./docs/questions-and-assumptions.md).
