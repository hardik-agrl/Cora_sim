from crypto.proof import ProofSystem
from protocol.owner import MigrationTransaction
from shard.shard import Shard


class Relay:

    def execute(
        self,
        tx: MigrationTransaction,
        source: Shard,
        destination: Shard,
        secret_key: str,
    ) -> bool:

        tx.status = "PREPARE"

        if not source.commitment_exists(tx.old_commitment):
            tx.status = "ABORTED"
            return False

        if source.nullifier_exists(tx.nullifier):
            tx.status = "ABORTED"
            return False

        if not ProofSystem.verify(tx.proof, secret_key):
            tx.status = "ABORTED"
            return False

        tx.status = "COMMIT"

        source.spend(tx.nullifier)
        destination.add_commitment(tx.new_commitment)

        tx.status = "COMPLETED"

        return True