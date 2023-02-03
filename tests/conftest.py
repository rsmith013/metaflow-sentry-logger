import os

import pytest

os.environ["USER"] = "pytest"
os.environ["USERNAME"] = "pytest"
os.environ["METAFLOW_DEFAULT_METADATA"] = "local"
os.environ["METAFLOW_DATASTORE_SYSROOT_LOCAL"] = "/tmp/metaflow"
os.environ["METAFLOW_DEFAULT_DATASTORE"] = "local"
os.environ["METAFLOW_PROFILE"] = "test"


@pytest.fixture(scope="session")
def env_vars():
    env_vars = os.environ.copy()
    return env_vars
