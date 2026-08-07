import hashlib


class MerkleTree:

    def __init__(self):
        self.leaves = []

    def add_leaf(self, commitment: str):
        self.leaves.append(commitment)

    def get_root(self) -> str:

        if not self.leaves:
            return ""

        level = self.leaves[:]

        while len(level) > 1:

            if len(level) % 2:
                level.append(level[-1])

            next_level = []

            for i in range(0, len(level), 2):
                data = level[i] + level[i + 1]
                node = hashlib.sha256(data.encode()).hexdigest()
                next_level.append(node)

            level = next_level

        return level[0]

    def contains(self, commitment: str) -> bool:
        return commitment in self.leaves