from model.user import User


_users = [
    User(
        email="something@example.com",
        name="something",
        password="qwerty"
    ),
    User(
        email="example@example.com",
        name="example",
        password="123456"
    ),
]


def get_all() -> list[User]:
    """Возврат всех исследователей"""
    return _users


def get_one(name: str) -> User | None:
    for _user in _users:
        if _user.name == name:
            return _user
    return None


def create(user: User) -> User:
    """Добавление исследователя"""
    return user


def modify(user: User) -> User:
    """Частичное изменение записи исследователя"""
    return user


def replace(user: User) -> User:
    """Полная замена записи исследователя"""
    return user


def delete(name: str) -> bool:
    """Удаление записи исследователя; возврат значения None,
    если запись существовала"""
    return None
