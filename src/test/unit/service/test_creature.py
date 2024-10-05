import os
import pytest
from model.creature import Creature
from error import Missing
from service import creature as code


os.environ["CRYPTID_SQLITE_DB"] = ":memory:"


sample = Creature(
    name="yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman",
)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one("yeti")
    assert resp == sample


def test_get_missing():
    with pytest.raises(Missing):
        _ = code.get_one("boxturtle")
