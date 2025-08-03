import pytest
from src.models.products.smartphone import Smartphone


def test_smartphone_creation():
    phone = Smartphone("iPhone", "Cool", 100000, 5, "A15", "13", 128, "black")
    assert phone.name == "iPhone"
    assert phone.memory == 128
    assert phone.color == "black"


def test_smartphone_add():
    p1 = Smartphone("Phone1", "Desc", 1000, 2, "A", "M1", 64, "red")
    p2 = Smartphone("Phone2", "Desc", 2000, 3, "B", "M2", 128, "blue")
    assert p1 + p2 == 1000*2 + 2000*3


def test_smartphone_add_invalid():
    p1 = Smartphone("Phone", "Desc", 1000, 1, "A", "M", 64, "red")
    with pytest.raises(TypeError):
        p1 + "не телефон"
