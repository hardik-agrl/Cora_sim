import csv
import os

from simulation.driver import SimulationDriver


WORKLOADS = [100, 500, 1000, 5000]


def main():

    os.makedirs("results", exist_ok=True)

    with open("results/scalability.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Transactions",
            "SuccessRate",
            "AverageLatency"
        ])

        for workload in WORKLOADS:

            print(f"\nRunning {workload} transactions...\n")

            driver = SimulationDriver()

            metrics = driver.run(workload)

            writer.writerow([
                workload,
                round(metrics.success_rate() * 100, 2),
                round(metrics.average_latency(), 2),
            ])

    print("\nScalability results saved to results/scalability.csv")


if __name__ == "__main__":
    main()