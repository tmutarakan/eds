from pydantic import BaseModel


class Signature(BaseModel):
    msrn: str # the main state registration number
