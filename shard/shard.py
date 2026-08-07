from config import ROOT_RETENTION
from shard.merkle_tree import MerkleTree
from shard.nullifier_set import NullifierSet
from shard.root_window import RootWindow


class Shard:

    def __init__(self, shard_id: int):
        self.shard_id = shard_id
        self.tree = MerkleTree()
        self.nullifiers = NullifierSet()
        self.root_window = RootWindow(ROOT_RETENTION)

    def add_commitment(self, commitment: str):
        self.tree.add_leaf(commitment)
        self.root_window.add(self.tree.get_root())

    def spend(self, nullifier: str):
        self.nullifiers.add(nullifier)

    def commitment_exists(self, commitment: str) -> bool:
        return self.tree.contains(commitment)

    def nullifier_exists(self, nullifier: str) -> bool:
        return self.nullifiers.exists(nullifier)

    def current_root(self):
        return self.tree.get_root()