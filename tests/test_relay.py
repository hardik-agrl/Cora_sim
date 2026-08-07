from crypto.commitment import Commitment
from protocol.owner import Owner
from protocol.relay import Relay
from shard.shard import Shard

owner = Owner("owner-secret")

source = Shard(0)
destination = Shard(1)

value = 100

randomness = Commitment.generate_randomness()

old_commitment = Commitment.create(value, randomness)

source.add_commitment(old_commitment)

tx = owner.create_migration(
    value=value,
    old_randomness=randomness,
    source_shard=0,
    destination_shard=1,
)

relay = Relay()

success = relay.execute(
    tx,
    source,
    destination,
    "owner-secret",
)

print("Success:", success)
print("Status:", tx.status)

print("Source spent:", source.nullifier_exists(tx.nullifier))
print("Destination contains:",
      destination.commitment_exists(tx.new_commitment))