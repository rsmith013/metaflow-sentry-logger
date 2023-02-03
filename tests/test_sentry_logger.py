import os
import random
import string
import subprocess
from pathlib import Path

import pytest
from metaflow import namespace


def get_id(size=6, chars=string.ascii_uppercase + string.digits):
    return "".join(random.choice(chars) for _ in range(size))


def test_calling_without_dsn_raises(env_vars):
    """
    Check that when we call a flow without setting the METAFLOW_SENTRY_DSN env
    var, we get a flow error. The flow makes use of the sentry step decorator.

    This basic check demonstrates that the sentry plugin is being loaded
    as expected.
    """

    flow_fpath = os.path.join(
        os.path.abspath(Path(__file__).parent.parent), "examples/sample_flow.py"
    )
    namespace(f"user:{env_vars['USERNAME']}")

    cmd = ["python", flow_fpath, "run", "--tag={random_tag}"]

    # Check that we are raising an exception
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(cmd, env=env_vars)

    # Inspect the flow output for expected issue
    try:
        subprocess.check_output(cmd, env=env_vars, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        assert b"without setting the METAFLOW_SENTRY_DSN" in e.output


def test_calling_cli_with_without_dsn_raises(env_vars):
    """
    Check that when we call a flow without setting the METAFLOW_SENTRY_DSN env
    var, we get a flow error. This flow makes use of the --with cli argument to
    decorate all steps with the Sentry step decorator.

    This basic check demonstrates that the sentry plugin is being loaded
    as expected.
    """
    flow_fpath = os.path.join(
        os.path.abspath(Path(__file__).parent.parent), "examples/sample_flow_with.py"
    )
    namespace(f"user:{env_vars['USERNAME']}")

    cmd = ["python", flow_fpath, "run", "--with=sentry"]

    # Check that we are raising an exception
    with pytest.raises(subprocess.CalledProcessError):
        subprocess.check_call(cmd, env=env_vars)

    # Inspect the flow output for expected issue
    try:
        subprocess.check_output(cmd, env=env_vars, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as e:
        assert b"without setting the METAFLOW_SENTRY_DSN" in e.output
