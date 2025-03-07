#  Licensed to Elasticsearch B.V. under one or more contributor
#  license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright
#  ownership. Elasticsearch B.V. licenses this file to you under
#  the Apache License, Version 2.0 (the "License"); you may
#  not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
# 	http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing,
#  software distributed under the License is distributed on an
#  "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#  KIND, either express or implied.  See the License for the
#  specific language governing permissions and limitations
#  under the License.

import os

import nox

SOURCE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE_FILES = (
    "docs/sphinx/conf.py",
    "noxfile.py",
    "elasticsearch_serverless/",
    "test_elasticsearch_serverless/",
    "utils/",
)
# Allow building aiohttp when no wheels are available (eg. for recent Python versions)
INSTALL_ENV = {"AIOHTTP_NO_EXTENSIONS": "1"}


def pytest_argv():
    junit_xml = os.path.join(
        SOURCE_DIR, "junit", "elasticsearch-serverless-python-junit.xml"
    )
    return [
        "pytest",
        "--cov-report=term-missing",
        "--cov=elasticsearch_serverless",
        "--cov-config=setup.cfg",
        f"--junitxml={junit_xml}",
        "--log-level=debug",
        "-vv",
        "--cache-clear",
    ]


@nox.session(python=["3.9", "3.10", "3.11", "3.12", "3.13"])
def test(session):
    session.install(".[dev]", env=INSTALL_ENV)

    session.run(*pytest_argv(), *(session.posargs))


@nox.session(python=["3.9", "3.13"])
def test_otel(session):
    session.install(".[dev]", env=INSTALL_ENV)
    session.install("opentelemetry-api", "opentelemetry-sdk")

    argv = pytest_argv() + ["-m", "otel"]
    session.run(*argv, *(session.posargs), env={"TEST_WITH_OTEL": "1"})


@nox.session()
def format(session):
    session.install("black~=24.0", "isort", "flynt", "unasync", "setuptools")

    session.run("python", "utils/run-unasync.py")
    session.run("isort", "--profile=black", *SOURCE_FILES)
    session.run("flynt", *SOURCE_FILES)
    session.run("black", *SOURCE_FILES)
    session.run("python", "utils/license-headers.py", "fix", *SOURCE_FILES)

    lint(session)


@nox.session()
def lint(session):
    session.install(
        "flake8", "black~=24.0", "mypy", "isort", "types-requests", "opentelemetry-api"
    )

    session.run("isort", "--check", "--profile=black", *SOURCE_FILES)
    session.run("black", "--check", *SOURCE_FILES)
    session.run("flake8", *SOURCE_FILES)
    session.run("python", "utils/license-headers.py", "check", *SOURCE_FILES)

    session.install(".[dev]", env=INSTALL_ENV)

    # Run mypy on the package and then the type examples separately for
    # the two different mypy use-cases, ourselves and our users.
    session.run("mypy", "--strict", "--show-error-codes", "elasticsearch_serverless/")
    session.run(
        "mypy",
        "--strict",
        "--show-error-codes",
        "test_elasticsearch_serverless/test_types/sync_types.py",
    )
    session.run(
        "mypy",
        "--strict",
        "--show-error-codes",
        "test_elasticsearch_serverless/test_types/async_types.py",
    )

    # Make sure we don't require aiohttp to be installed for users to
    # receive type hint information from mypy.
    session.run("python", "-m", "pip", "uninstall", "--yes", "aiohttp")
    session.run("mypy", "--strict", "--show-error-codes", "elasticsearch_serverless/")
    session.run(
        "mypy",
        "--strict",
        "--show-error-codes",
        "test_elasticsearch_serverless/test_types/sync_types.py",
    )


@nox.session()
def docs(session):
    session.install(".[docs,orjson]")
    session.run("sphinx-build", "docs/sphinx/", "docs/sphinx/_build", "-b", "html")
