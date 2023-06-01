# How to use this template

This is the template structure for an Elasticsearch Serverless Client.
It can be used to start a new repository for a specific client (e.g. elasticsearch-serverless-php).

## Parameters

When you create a new repository using this template you have to customize the
contents according to the programming language of the client.

We offered an automatic tool to search and replace occurrences of `<<[lang]>>` and
`<<[LANG]>>` in all the files.

The `<<[lang]>>` is the placeholder for the repository name `elasticsearch-serverless-<<[lang]>>`.
For instance, if `<<[lang]>> = "php"` then the repository will be `elasticsearch-serverless-php`.

The `<<[LANG]>>` is the placeholder for the language name. For instance, `<<[LANG]>> = "PHP"`.
This is typically used in README or documentation files.

## How to customize the files

You can customize the files replacing the parameters using the following command:

```bash
customize.sh <<[lang]>>
```

where `<<[lang]>>` is the language specific client to use (e.g. `customize.sh php`).
This will search & replace all the occurrencies of `<<[lang]>>` and `<<[LANG]>>` in some files
(e.g. README, CONTRIBUTING, etc). 

## Choose the correct LICENSE

You need to choose the LICENSE for your custom client. Remember to change the `LICENSE` file.