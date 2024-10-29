from datetime import datetime
from pydantic import BaseModel


class Employeer(BaseModel):
    surname: str
    name: str
    patronymic: str
    passport_serial: str
    passport_number: str
    birth_date: datetime
