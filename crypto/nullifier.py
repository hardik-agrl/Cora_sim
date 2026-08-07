import hashlib


class Nullifier:

    @staticmethod
    def generate(commitment: str, secret_key: str) -> str:
        data = f"{commitment}:{secret_key}"
        return hashlib.sha256(data.encode()).hexdigest()