from metaflow import FlowSpec, sentry, step


class MyFlow(FlowSpec):
    @sentry
    @step
    def start(self):
        print("Start step")

        self.next(self.error)

    @sentry
    @step
    def error(self):
        self.div_0 = 1 / 0

        self.next(self.end)

    @sentry
    @step
    def end(self):
        print("final step")


if __name__ == "__main__":
    MyFlow()
