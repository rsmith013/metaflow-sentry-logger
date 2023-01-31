"""
Define extensions for metaflow to import.
"""
from typing import List

from .sentry_logging_step_decorator import SentryLoggingStepDecorator

FLOW_DECORATORS = []
STEP_DECORATORS = [SentryLoggingStepDecorator]
ENVIRONMENTS = []
METADATA_PROVIDERS = []
SIDECARS = {}
LOGGING_SIDECARS = {}
MONITOR_SIDECARS = {}


def get_plugin_cli() -> List:
    """
    Return list of click multi-commands to extend metaflow CLI.
    """
    return []
