from datetime import datetime
from pydantic import BaseModel


class Signature(BaseModel):
    filename: str
    msrn: str # the main state registration number
    certificate_expiration_date: datetime
    key_expiration_date: datetime
    filepath: str
