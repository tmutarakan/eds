from model.employeer import Employeer


_employeers = [
    Employeer(
        surname="Иванов",
        name="Иван",
        patronymic="Иванович",
        passport_serial="9299",
        passport_number="650586",
        birth_date="1995-08-07"
    ),
    Employeer(
        surname="Петров",
        name="Петр",
        patronymic="Петрович",
        passport_serial="9259",
        passport_number="518006",
        birth_date="1986-01-27"
    ),
]


def get_all() -> list[Employeer]:
    """Возврат всех исследователей"""
    return _employeers


def get_one(filename: str) -> Employeer | None:
    for _employeer in _employeers:
        if _employeer.filename == filename:
            return _employeer
    return None


def create(employeer: Employeer) -> Employeer:
    """Добавление исследователя"""
    return employeer


def modify(employeer: Employeer) -> Employeer:
    """Частичное изменение записи исследователя"""
    return employeer


def replace(employeer: Employeer) -> Employeer:
    """Полная замена записи исследователя"""
    return employeer


def delete(filename: str) -> None:
    """Удаление записи исследователя; возврат значения None,
    если запись существовала"""
    return None
