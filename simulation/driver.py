import random

from config import NUM_TRANSACTIONS
from crypto.commitment import Commitment
from protocol.owner import Owner
from protocol.relay import Relay
from shard.shard import Shard
from simulation.metrics import Metrics


class SimulationDriver:

    def __init__(self):
        self.source = Shard(0)
        self.destination = Shard(1)

        self.owner = Owner("owner-secret")
        self.relay = Relay()
        self.metrics = Metrics()

    def run(self, num_transactions=100):

        for _ in range(num_transactions):

            value = random.randint(1, 1000)

            randomness = Commitment.generate_randomness()

            commitment = Commitment.create(
                value,
                randomness,
            )

            self.source.add_commitment(commitment)

            tx = self.owner.create_migration(
                value=value,
                old_randomness=randomness,
                source_shard=0,
                destination_shard=1,
            )

            success = self.relay.execute(
                tx,
                self.source,
                self.destination,
                "owner-secret",
            )

            latency = random.randint(90, 150)

            if success:
                self.metrics.add_success(latency)
            else:
                self.metrics.add_failure()

        self.print_results()

    def print_results(self):

        print("\n========== Simulation ==========")
        print(f"Transactions : {self.metrics.total}")
        print(f"Successful   : {self.metrics.success}")
        print(f"Failed       : {self.metrics.failed}")
        print(f"Success Rate : {self.metrics.success_rate():.2%}")
        print(f"Avg Latency  : {self.metrics.average_latency():.2f} ms")

        self.metrics.save_csv()
        print("\nResults saved to results/simulation.csv")