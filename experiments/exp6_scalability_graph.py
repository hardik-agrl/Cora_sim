import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("results/scalability.csv")

    plt.figure(figsize=(8, 5))

    plt.plot(
        df["Transactions"],
        df["AverageLatency"],
        marker="o",
        linewidth=2
    )

    plt.xlabel("Number of Transactions")
    plt.ylabel("Average Latency (ms)")
    plt.title("CoRA Scalability Evaluation")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("results/scalability.png", dpi=300)
    plt.show()


if __name__ == "__main__":
    main()