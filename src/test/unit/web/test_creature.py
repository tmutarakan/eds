import os
import pytest
from fastapi import HTTPException
from model.creature import Creature
from web import creature
from error import Missing, Duplicate


os.environ["CRYPTID_UNIT_TEST"] = "true"


@pytest.fixture
def sample() -> Creature:
    return Creature(name="dragon",
        description="Wings! Fire!",
        country="*", area="*", aka="firedrake")


@pytest.fixture
def fakes() -> list[Creature]:
    return creature.get_all()


def assert_duplicate(exc):
    assert exc.value.status_code == 404
    assert "Duplicate" in exc.value.msg


def assert_missing(exc):
    assert exc.value.status_code == 404
    assert "Missing" in exc.value.msg


def test_create(sample):
    assert creature.create(sample) == sample


def test_create_duplicate(fakes):
    with pytest.raises(HTTPException) as exc:
        resp = creature.create(fakes[0])
        assert_duplicate(exc)


def test_get_one(fakes):
    assert creature.get_one(fakes[0].name) == fakes[0]


def test_get_one_missing():
    with pytest.raises(HTTPException) as exc:
        resp = creature.get_one("bobcat")
        assert_missing(exc)


def test_modify(fakes):
    assert creature.modify(fakes[0].name, fakes[0]) == fakes[0]


def test_modify_missing(sample):
    with pytest.raises(HTTPException) as exc:
        resp = creature.modify(sample.name, sample)
        assert_missing(exc)


def test_delete(fakes):
    assert creature.delete(fakes[0].name) is None


def test_delete_missing(sample):
    with pytest.raises(HTTPException) as exc:
        resp = creature.delete("emu")
        assert_missing(exc)
