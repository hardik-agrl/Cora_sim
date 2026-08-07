from dataclasses import dataclass

from crypto.commitment import Commitment
from crypto.nullifier import Nullifier
from crypto.proof import ProofSystem


@dataclass
class MigrationTransaction:
    source_shard: int
    destination_shard: int

    old_commitment: str
    new_commitment: str

    nullifier: str

    proof: object


class Owner:

    def __init__(self, secret_key: str):
        self.secret_key = secret_key

    def create_migration(
        self,
        value: int,
        old_randomness: str,
        source_shard: int,
        destination_shard: int,
    ) -> MigrationTransaction:

        old_commitment = Commitment.create(value, old_randomness)

        new_commitment, _ = Commitment.rerandomize(value)

        nullifier = Nullifier.generate(
            old_commitment,
            self.secret_key,
        )

        proof = ProofSystem.generate(
            old_commitment,
            new_commitment,
            self.secret_key,
        )

        return MigrationTransaction(
            source_shard=source_shard,
            destination_shard=destination_shard,
            old_commitment=old_commitment,
            new_commitment=new_commitment,
            nullifier=nullifier,
            proof=proof,
        )