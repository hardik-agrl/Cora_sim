import random

from config import NETWORK_DELAY


class Network:

    def __init__(self):
        self.delay = NETWORK_DELAY

    def latency(self) -> int:
        return random.randint(
            self.delay,
            self.delay + 50,
        )

    def should_drop(self, probability=0.0) -> bool:
        return random.random() < probability