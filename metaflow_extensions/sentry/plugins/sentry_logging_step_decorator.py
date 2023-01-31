import logging
import os

import sentry_sdk
from metaflow import decorators
from metaflow_extensions.sentry.config.metaflow_config import SENTRY_DSN

logger = logging.getLogger(__name__)


class SentryLoggingStepDecorator(decorators.StepDecorator):

    name = "sentry"

    def step_init(
        self, flow, graph, step_name, decorators, environment, flow_datastore, logger
    ):
        if not SENTRY_DSN:
            msg = (
                "You have requested the sentry logging decorator "
                "without setting the METAFLOW_SENTRY_DSN configuration value."
            )
            raise ValueError(msg)

    def task_pre_step(
        self,
        step_name,
        task_datastore,
        metadata,
        run_id,
        task_id,
        flow,
        graph,
        retry_count,
        max_user_code_retries,
        ubf_context,
        inputs,
    ):

        sentry_sdk.init(
            dsn=SENTRY_DSN,
            environment=os.environ.get("METAFLOW_PROFILE"),
        )

    def task_exception(
        self, exception, step_name, flow, graph, retry_count, max_user_code_retries
    ):
        if retry_count == max_user_code_retries:
            logger.exception(exception)
