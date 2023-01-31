[![PyPI version](https://badge.fury.io/py/metaflow-sentry-logger.svg)](https://badge.fury.io/py/metaflow-sentry-logger)

# Sentry Logging Plugin for Metaflow

Enabling the use of [Sentry](https://sentry.io/) with [Metaflow](https://metaflow.org/)


- [Sentry Logging Plugin for Metaflow](#sentry-logging-plugin-for-metaflow)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Configuration](#configuration)
  - [Examples](#examples)
    - [Using the step decorator](#using-the-step-decorator)
    - [Calling using the `--with` command line argument](#calling-using-the---with-command-line-argument)

## Installation

Install the plugin using pip.

```bash
pip install metaflow-sentry-logger
```

For development 

```bash
pip install metaflow-sentry-logger[dev]
```

## Usage

The sentry plugin can be called using either the `--with sentry` command line argument or through the step decorator `@sentry`.

## Configuration

Only basic configuration is currently supported using environment variables.

| Name                  | Description                                       | Required | Location                                 |
| --------------------- | ------------------------------------------------- | -------- | ---------------------------------------- |
| `METAFLOW_SENTRY_DSN` | The DSN for the target sentry project             | `True`   | `Environment Variable` `Metaflow Config` |
| `METAFLOW_PROFILE`    | Used by this plugin to determine the environment. | `False`  | `Environment Variable`                   |

## Examples

See the (examples)[examples] directory for some example flows or see the code snippets below

### Using the step decorator

```python
# examples/sample_flow.py 

from metaflow import FlowSpec, step, sentry


class MyFlow(FlowSpec):

    @step
    @sentry
    def start(self):
        print("Start step")

    @step
    @sentry
    def error(self):
        self.div_0 = 1/0

    @step
    @sentry
    def end(self):
        print("final step")
```

### Calling using the `--with` command line argument

```bash
python examples/sample_flow_with.py run --with sentry
```


