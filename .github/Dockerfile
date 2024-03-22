ARG PYTHON_VERSION=3.9
FROM python:${PYTHON_VERSION}

WORKDIR /code/elasticsearch-serverless-python
RUN mkdir -p /code/elasticsearch-serverless-python/build

COPY pyproject.toml README.rst .
RUN python -m pip install \
    -U --no-cache-dir \
    --disable-pip-version-check \
    .[dev]

COPY . .
