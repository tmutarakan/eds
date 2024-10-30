from model.user import User
import data.user as data


def get_all() -> list[User]:
    return data.get_all()


def get_one(name: str) -> User | None:
    return data.get_one(name)


def create(user: User) -> User:
    return data.create(user)


def replace(user_id: int, user: User) -> User:
    return data.replace(user_id, user)


def modify(user_id: int, user: User) -> User:
    return data.modify(user_id, user)


def delete(user_id: int, user: User) -> bool:
    return data.delete(user_id)
