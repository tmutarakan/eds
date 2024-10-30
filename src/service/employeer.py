from model.employeer import Employeer
import data.employeer as data


def get_all() -> list[Employeer]:
    return data.get_all()


def get_one(employeer_id: int) -> Employeer | None:
    return data.get(employeer_id)


def create(employeer: Employeer) -> Employeer:
    return data.create(employeer)


def replace(employeer_id: int, employeer: Employeer) -> Employeer:
    return data.replace(employeer_id, employeer)


def modify(employeer_id: int, employeer: Employeer) -> Employeer:
    return data.modify(employeer_id, employeer)


def delete(employeer: Employeer) -> bool:
    return data.delete(employeer)
