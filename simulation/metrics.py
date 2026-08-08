import csv
import os


class Metrics:

    def __init__(self):
        self.total = 0
        self.success = 0
        self.failed = 0

        self.latencies = []
        self.records = []

    def add_success(self, latency):
        self.total += 1
        self.success += 1
        self.latencies.append(latency)

        self.records.append({
            "transaction": self.total,
            "latency": latency,
            "success": 1
        })

    def add_failure(self, latency=0):
        self.total += 1
        self.failed += 1

        self.records.append({
            "transaction": self.total,
            "latency": latency,
            "success": 0
        })

    def average_latency(self):
        if not self.latencies:
            return 0

        return sum(self.latencies) / len(self.latencies)

    def success_rate(self):
        if self.total == 0:
            return 0

        return self.success / self.total

    def save_csv(self, filename="results/simulation.csv"):

        os.makedirs("results", exist_ok=True)

        with open(filename, "w", newline="") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=[
                    "transaction",
                    "latency",
                    "success"
                ]
            )

            writer.writeheader()
            writer.writerows(self.records)