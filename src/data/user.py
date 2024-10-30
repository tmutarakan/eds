from model.user import User
from data.init import curs


curs.execute(
    """
    create table if not exists user(
        email text,
        name text primary key,
        password text
    )
    """
)


def row_to_model(row: tuple) -> User:
    email, name, password = row
    return User(email=email, name=name, password=password)


def model_to_dict(user: User) -> dict:
    return user.model_dump()


def get_one(name: str) -> User:
    qry = "select * from user where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    return row_to_model(row)


def get_all() -> list[User]:
    qry = "select * from user"
    curs.execute(qry)
    rows = list(curs.fetchall())
    return [row_to_model(row) for row in rows]


def create(user: User):
    qry = """insert into user values
    (:email, :name, :password)"""
    params = model_to_dict(user)
    curs.execute(qry, params)
    return user


def modify(user: User):
    return user


def replace(user: User):
    return user


def delete(user: User):
    qry = "delete from user where name = :name"
    params = {"name": user.name}
    curs.execute(qry, params)
