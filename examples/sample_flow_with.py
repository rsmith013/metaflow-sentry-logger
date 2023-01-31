from metaflow import FlowSpec, step


class MyFlow(FlowSpec):
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
    MyFlow()
