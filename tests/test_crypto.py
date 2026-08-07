from crypto.commitment import Commitment
from crypto.nullifier import Nullifier
from crypto.proof import ProofSystem


value = 100
secret_key = "owner123"

r1 = Commitment.generate_randomness()
c1 = Commitment.create(value, r1)

c2, r2 = Commitment.rerandomize(value)

nullifier = Nullifier.generate(c1, secret_key)

proof = ProofSystem.generate(c1, c2, secret_key)

print("Commitment:", c1)
print("New Commitment:", c2)
print("Nullifier:", nullifier)
print("Proof Valid:", ProofSystem.verify(proof, secret_key))