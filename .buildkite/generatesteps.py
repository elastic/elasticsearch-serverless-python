import os

import yaml


def benchmark_to_steps(python, connection_class):
    return [
        {
            "label": f":elasticsearch: :python: ES Serverless ({python}/{connection_class})",
            "agents": {"provider": "gcp"},
            "env": {
                "PYTHON_VERSION": f"{python}",
                "PYTHON_CONNECTION_CLASS": f"{connection_class}",
                # TEMPORARY for 3.11
                # https://github.com/aio-libs/aiohttp/issues/6600
                "AIOHTTP_NO_EXTENSIONS": 1,
                # https://github.com/aio-libs/frozenlist/issues/285
                "FROZENLIST_NO_EXTENSIONS": 1,
                # https://github.com/aio-libs/yarl/issues/680
                "YARL_NO_EXTENSIONS": 1,
                "EC_REGISTER_BACKEND": "appex-qa-team-cluster",
                "EC_ENV": "qa",
                "EC_REGION": "aws-eu-west-1",
                "EC_PROJECT_PREFIX": f"esv-client-python-test-{python}-{connection_class}",
            },
            "command": "./.buildkite/run-tests",
            "artifact_paths": "junit/*-junit.xml",
            "retry": {"manual": False},
            "key": f"run_{python}_{connection_class}",
        },
        {
            "label": f":elasticsearch: :python: Teardown ES Serverless ({python}/{connection_class})",
            "command": "./.buildkite/run-tests",
            "command": f"bash .buildkite/ci.sh terminate_environment",
            "agents": {"provider": "gcp"},
            "env": {
                "PYTHON_VERSION": f"{python}",
                "PYTHON_CONNECTION_CLASS": f"{connection_class}",
                "EC_REGISTER_BACKEND": "appex-qa-team-cluster",
                "EC_ENV": "qa",
                "EC_REGION": "aws-eu-west-1",
                "EC_PROJECT_PREFIX": f"esv-client-python-test-{python}-{connection_class}",
            },
            "command": ".buildkite/teardown-tests",
            "depends_on": f"run_{python}_{connection_class}",
            "allow_dependency_failure": True,
        },
    ]


if __name__ == "__main__":
    steps = []
    for python in ["3.7", "3.8", "3.9", "3.10", "3.11"]:
        for connection_class in ["urllib3", "requests"]:
            steps.extend(benchmark_to_steps(python, connection_class))
    print(yaml.dump({"steps": steps}, Dumper=yaml.Dumper, sort_keys=False))
