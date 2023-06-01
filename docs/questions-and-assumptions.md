# Questions and assumptions

## Initial questions

### Do we have a specification?
Not yet. For now we've decided to extract 3 APIs from the Elasticsearch spec and generate code based on that.

### How do we test against a running server?
Initially I tested the code with Stack Elasticsearch and API Key authentication. But I've now tested it with a Cloud instance of Serverless in our QA Cloud and it's working there too.

### YAML Tests

The Elasticsearch team is working on YAML tests. Enrico proposed we could maintain our own set of lighter YAML tests for Serverless clients since the API will be smaller. This way we wouldn't need to worry about the cleanup phase and all the errors it produces, and we wouldn't need to be on top of the changes in the Java code to understand how to run our integration tests.

### What Namespace should I use?

Some of the namespaces we use in our Ruby clients:
- `Elastic::EnterpriseSearch`
- `Elastic::EnterpriseSearch::AppSearch`
- `Elastic::EnterpriseSearch::WorkplaceSearch`
- `Elasticsearch::Client`

For this client I'm using `ElasticsearchServerless::Client` since I think it's the simplest one. I think something like `Elasticsearch::Serverless::Client` would just be more confusing to differentiate the Stack client from the Serverless client.

## Docs

One of the outcomes of this work is coordinating with the docs team to create doc books for this client and tie that up together with the docs infra.

## Assumptions

### Assumption: Regarding implementation of libraries:

In the Elasticsearch Ruby Client, `elasticsearch` and `elasticsearch-api` are two separate libraries. The whole client is `elasticsearch`, which requires `elasticsearch-api` (the generated API code). But you can also use `elasticsearch-api` as a library on its own in your code. Josh told me in JS it's all just one package. I see why it could make sense when it was built to have these separated in the Ruby client, but for Serverless, I'm going to assume we want to have just the one library which includes the client and the API generated code. At least that's how I'll build the prototype now and we can refactor for a different approach in the future.

## Notes

### Code generation

The code for the current APIs `info`, `bulk` and `search` was taken from the Elasticsearch client's code for this prototype, but there'll be further work with code generation. As such, a lot of the code used in `elasticsearch-api` is being duplicated here. I need to look more into that, see what stuff can be shared in `elastic-transport` or if it deserves to be another library. My initial thought is maybe there could be a namespace for utils in transport, such as `api/utils` and `api/response` (which is also being duplicated in Enterprise Search Ruby).
