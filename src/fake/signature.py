from model.signature import Signature


_signatures = [
    Signature(
        filename="sbldvbs.000",
        msrn="16556156561",
        certificate_expiration_date="2025-08-08",
        key_expiration_date="2025-08-06",
        filepath="/srv/data/signature"
    ),
    Signature(
        filename="sbeeedx.001",
        msrn="16556100001",
        certificate_expiration_date="2025-08-28",
        key_expiration_date="2025-08-26",
        filepath="/srv/data/signature"
    ),
]


def get_all() -> list[Signature]:
    """Возврат всех исследователей"""
    return _signatures


def get_one(filename: str) -> Signature | None:
    for _signature in _signatures:
        if _signature.filename == filename:
            return _signature
    return None


def create(signature: Signature) -> Signature:
    """Добавление исследователя"""
    return signature


def modify(signature: Signature) -> Signature:
    """Частичное изменение записи исследователя"""
    return signature


def replace(signature: Signature) -> Signature:
    """Полная замена записи исследователя"""
    return signature


def delete(filename: str) -> None:
    """Удаление записи исследователя; возврат значения None,
    если запись существовала"""
    return None
