import hashlib
from dataclasses import dataclass


@dataclass
class Proof:
    old_commitment: str
    new_commitment: str
    signature: str


class ProofSystem:

    @staticmethod
    def generate(old_commitment: str,
                 new_commitment: str,
                 secret_key: str) -> Proof:

        payload = old_commitment + new_commitment + secret_key
        signature = hashlib.sha256(payload.encode()).hexdigest()

        return Proof(
            old_commitment,
            new_commitment,
            signature
        )

    @staticmethod
    def verify(proof: Proof, secret_key: str) -> bool:

        payload = (
            proof.old_commitment +
            proof.new_commitment +
            secret_key
        )

        expected = hashlib.sha256(payload.encode()).hexdigest()

        return expected == proof.signature