from pydantic import BaseModel


class Employeer(BaseModel):
    surname: str
    name: str
    patronymic: str
