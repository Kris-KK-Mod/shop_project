import pytest
from src.models.product import Product


def test_product_initialization():
    """Проверяет корректность инициализации товара."""
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    assert product.name == "Телефон"
    assert product.description == "Смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_product_default_values():
    """Проверяет, что атрибуты имеют правильные типы."""
    product = Product("Ноутбук", "Игровой", 100000.0, 5)

    assert isinstance(product.name, str)
    assert isinstance(product.description, str)
    assert isinstance(product.price, float)
    assert isinstance(product.quantity, int)
