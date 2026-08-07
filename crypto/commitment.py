import hashlib
import secrets


class Commitment:

    @staticmethod
    def generate_randomness() -> str:
        return secrets.token_hex(16)

    @staticmethod
    def create(value: int, randomness: str) -> str:
        data = f"{value}:{randomness}"
        return hashlib.sha256(data.encode()).hexdigest()

    @staticmethod
    def rerandomize(value: int):
        randomness = Commitment.generate_randomness()
        commitment = Commitment.create(value, randomness)
        return commitment, randomness