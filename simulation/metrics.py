class Metrics:

    def __init__(self):
        self.total = 0
        self.success = 0
        self.failed = 0

        self.latencies = []

    def add_success(self, latency):
        self.total += 1
        self.success += 1
        self.latencies.append(latency)

    def add_failure(self):
        self.total += 1
        self.failed += 1

    def average_latency(self):

        if not self.latencies:
            return 0

        return sum(self.latencies) / len(self.latencies)

    def success_rate(self):

        if self.total == 0:
            return 0

        return self.success / self.total