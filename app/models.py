import random
from pydantic import BaseModel


class User(BaseModel):
    id: int = random.randint(0, 125)
    name: str = "John Doe"
    age: int = 18
    is_adult: bool = True
