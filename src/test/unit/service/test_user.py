from model.user import User
from service import user as code


sample = User(
    email="random@example.com",
    name="random",
    password="supersecretpassword"
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("random")
    assert resp == sample


def test_get_missing():
    resp = code.get_one("noexample")
    assert resp is None
