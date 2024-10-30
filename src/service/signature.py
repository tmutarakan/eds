from model.signature import Signature
import fake.signature as data


def get_all() -> list[Signature]:
    return data.get_all()


def get_one(filename: str) -> Signature | None:
    return data.get_one(filename)


def create(signature: Signature) -> Signature:
    return data.create(signature)


def replace(signature_id: int, signature: Signature) -> Signature:
    return data.replace(signature_id, signature)


def modify(signature_id: int, signature: Signature) -> Signature:
    return data.modify(signature_id, signature)


def delete(signature: Signature) -> bool:
    return data.delete(signature)
