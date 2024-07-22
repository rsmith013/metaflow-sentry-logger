"""
Metaflow configuration over-rides.

Use `metaflow.metaflow_config_funcs.from_conf` to set values with the
following prioritisation order: 1) System environment variable 2) Your
Metaflow profile (JSONconfig) 3) The value passed to `from_conf`
"""
from metaflow.metaflow_config_funcs import from_conf

# Path to the client cache
SENTRY_DSN = from_conf("SENTRY_DSN", None)
