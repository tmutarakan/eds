from model.employeer import Employeer
from data.init import curs


curs.execute(
    """
    create table if not exists employeer(
        id int primary key,
        surname text,
        name text,
        patronymic text,
        passport_serial text,
        passport_number text,
        birth_date text
    )
    """
)


def row_to_model(row: tuple) -> Employeer:
    surname, name, patronymic, passport_serial, passport_number, birth_date = row
    return Employeer(surname=surname, name=name, patronymic=patronymic, passport_serial=passport_serial, passport_number=passport_number, birth_date=birth_date)


def model_to_dict(employeer: Employeer) -> dict:
    return employeer.model_dump()


def get_one(employeer_id: int) -> Employeer:
    qry = "select * from employeer where id=:id"
    params = {"id": employeer_id}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[Employeer]:
    qry = "select * from employeer"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(employeer: Employeer):
    qry = """insert into employeer values
    (:surname, :name, :patronymic, :passport_serial, :passport_number, :birth_date)"""
    params = model_to_dict(employeer)
    curs.execute(qry, params)
    return employeer


def modify(employeer: Employeer):
    return employeer


def replace(employeer: Employeer):
    return employeer


def delete(employeer: Employeer):
    qry = "delete from employeer where id = :id"
    params = {"id": employeer.id}
    curs.execute(qry, params)
