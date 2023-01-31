import logging
import os

import sentry_sdk
from metaflow import decorators

logger = logging.getLogger(__name__)


class SentryLoggingStepDecorator(decorators.StepDecorator):

    name = "sentry"

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
        if not (sentry_dsn := os.environ.get("SENTRY_DSN")):
            msg = (
                "You have requested the sentry logging decorator "
                "without setting SENTRY_DSN environment variable"
            )
            raise ValueError(msg)

        sentry_sdk.init(
            dsn=sentry_dsn,
            environment=os.environ.get("METAFLOW_PROFILE"),
        )

    def task_exception(
        self, exception, step_name, flow, graph, retry_count, max_user_code_retries
    ):
        if retry_count == max_user_code_retries:
            logger.exception(exception)
