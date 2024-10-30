from model.signature import Signature
from data.init import curs


curs.execute(
    """
    create table if not exists signature(
        filename text primary key,
        msrn text,
        certificate_expiration_date text,
        key_expiration_date text,
        filepath text
    )
    """
)


def row_to_model(row: tuple) -> Signature:
    filename, msrn, certificate_expiration_date, key_expiration_date, filepath = row
    return Signature(filename=filename, msrn=msrn, certificate_expiration_date=certificate_expiration_date, key_expiration_date=key_expiration_date, filepath=filepath)


def model_to_dict(signature: Signature) -> dict:
    return signature.model_dump()


def get_one(filename: str) -> Signature:
    qry = "select * from signature where filename=:filename"
    params = {"name": filename}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[Signature]:
    qry = "select * from signature"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(signature: Signature):
    qry = """insert into signature values
    (:filename, :msrn, :certificate_expiration_date, :key_expiration_date, :filepath)"""
    params = model_to_dict(signature)
    curs.execute(qry, params)
    return signature


def modify(signature: Signature):
    return signature


def replace(signature: Signature):
    return signature


def delete(signature: Signature):
    qry = "delete from signature where filename = :filename"
    params = {"filename": signature.filename}
    curs.execute(qry, params)
