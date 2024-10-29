from datetime import datetime
from pydantic import BaseModel


class Signature(BaseModel):
    msrn: str # the main state registration number
    certificate_expiration_date: datetime
    key_expiration_date: datetime
    file_path: str
