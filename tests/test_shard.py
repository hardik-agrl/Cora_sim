from crypto.commitment import Commitment
from shard.shard import Shard

shard = Shard(1)

c1 = Commitment.create(
    100,
    Commitment.generate_randomness()
)

c2 = Commitment.create(
    200,
    Commitment.generate_randomness()
)

shard.add_commitment(c1)
shard.add_commitment(c2)

print("Root:", shard.current_root())
print("Contains c1:", shard.commitment_exists(c1))
print("Contains c2:", shard.commitment_exists(c2))