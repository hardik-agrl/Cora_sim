from crypto.commitment import Commitment
from protocol.owner import Owner

owner = Owner("owner-secret")

randomness = Commitment.generate_randomness()

tx = owner.create_migration(
    value=100,
    old_randomness=randomness,
    source_shard=0,
    destination_shard=1,
)

print(tx)