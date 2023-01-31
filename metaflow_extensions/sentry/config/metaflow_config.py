"""
Metaflow configuration over-rides.

Use `metaflow.from_conf` to set values with the following prioritisation
order: 1) System environment variable 2) Your Metaflow profile (JSON
config) 3) The value passed to `from_conf`
"""
from metaflow.metaflow_config import from_conf

# Path to the client cache
SENTRY_DSN = from_conf("SENTRY_DSN", None)
