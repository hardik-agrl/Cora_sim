import pandas as pd
import matplotlib.pyplot as plt

def main():
    df = pd.read_csv("results/simulation.csv")

    df = df.head(100)

    plt.figure(figsize=(8, 5))

    plt.plot(
        df["transaction"],
        df["latency"],
        linewidth=2,
    )

    plt.title("Migration Latency per Transaction")
    plt.xlabel("Transaction Number")
    plt.ylabel("Latency (ms)")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("results/latency.png", dpi=300)
    plt.show()

if __name__ == "__main__":
    main()