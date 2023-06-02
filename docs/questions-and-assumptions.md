# Questions and assumptions

## Initial questions

### Do we have a specification?

Not yet.
For now we've decided to extract a few APIs from the Elasticsearch spec and generate code based on that.

### How do we test against a running server?

We are testing it with a Cloud instance of Serverless in the QA environment.

### YAML Tests

The Elasticsearch team is working on YAML tests.
Enrico proposed we could maintain our own set of lighter YAML tests for Serverless clients since the API will be smaller.
This way we wouldn't need to worry about the cleanup phase and all the errors it produces, and we wouldn't need to be on top of the changes in the Java code to understand how to run our integration tests.

## Docs

One of the outcomes of this work is coordinating with the docs team to create doc books for this client and tie that up together with the docs infra.

## Assumptions

## Notes

### Code generation

The code for the current APIs was generated from the Elasticsearch client's code generator for this prototype, but there'll be further work with code generation.
As such, a lot of code used in `elasticsearch-py` is duplicated here.
