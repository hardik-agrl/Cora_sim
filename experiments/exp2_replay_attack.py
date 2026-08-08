from crypto.commitment import Commitment
from protocol.owner import Owner
from protocol.relay import Relay
from shard.shard import Shard


owner = Owner("owner-secret")

source = Shard(0)
destination = Shard(1)

relay = Relay()

value = 100

randomness = Commitment.generate_randomness()

commitment = Commitment.create(value, randomness)

source.add_commitment(commitment)

tx = owner.create_migration(
    value=value,
    old_randomness=randomness,
    source_shard=0,
    destination_shard=1,
)

first = relay.execute(
    tx,
    source,
    destination,
    "owner-secret",
)

second = relay.execute(
    tx,
    source,
    destination,
    "owner-secret",
)

print("First Migration :", first)
print("Second Migration:", second)
print("Final Status    :", tx.status)