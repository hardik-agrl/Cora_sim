class NullifierSet:

    def __init__(self):
        self.nullifiers = set()

    def add(self, nullifier: str):
        self.nullifiers.add(nullifier)

    def exists(self, nullifier: str) -> bool:
        return nullifier in self.nullifiers

    def __len__(self):
        return len(self.nullifiers)