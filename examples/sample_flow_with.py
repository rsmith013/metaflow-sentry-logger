"""
Example metaflow flow which is intended to be used with the --with cli argument
to demonstrate sentry integration.
"""

from metaflow import FlowSpec, step


class MyFlowWith(FlowSpec):
    @step
    def start(self):
        print("Start step")

        self.next(self.error)

    @step
    def error(self):
        self.div_0 = 1 / 0

        self.next(self.end)

    @step
    def end(self):
        print("final step")


if __name__ == "__main__":
    MyFlowWith()
