from abc import ABC, ABCMeta
from unittest.mock import patch

import pytest

from src.models.product import BaseProduct, Product


def test_log_mixin_output(capsys):
    """Проверка вывода информации при создании продукта"""
    p = Product("Test", "Test product", 100, 5)
    captured = capsys.readouterr()
    assert "price=100" in captured.out  # Теперь цена будет правильной


def test_log_mixin(capsys):
    """Проверка работы миксина логирования."""
    Product("Test", "Test", 100, 1)
    captured = capsys.readouterr()
    assert "price=100" in captured.out  # Теперь цена будет правильной


def test_base_product_abstract_methods():
    """Проверка, что BaseProduct требует реализации абстрактных методов"""
    with pytest.raises(TypeError):

        class InvalidProduct(BaseProduct, metaclass=ABCMeta):
            pass

        InvalidProduct("Test", "Test", 100, 1)


def test_product_repr():
    """Проверка строкового представления продукта"""
    p = Product("Test", "Test", 100, 1)
    assert repr(p) == "Product(name='Test', description='Test', quantity=1, price=100)"


def test_repr_method():
    """Проверка __repr__ для Product."""
    p = Product("Test", "Test", 100, 1)
    repr_str = repr(p)
    assert repr_str.startswith("Product(")
    assert "name='Test'" in repr_str
    assert "description='Test'" in repr_str
    assert "price=100" in repr_str
    assert "quantity=1" in repr_str


def test_base_product_is_abstract():
    """Проверка, что нельзя создать экземпляр BaseProduct."""
    with pytest.raises(TypeError):
        BaseProduct("Test", "Test", 100, 1)


def test_base_product_is_abc():
    """Проверка, что BaseProduct является абстрактным классом."""
    assert issubclass(BaseProduct, ABC)


def test_product_implements_base_product():
    """Проверка, что Product реализует BaseProduct."""
    assert issubclass(Product, BaseProduct)


def test_price_getter():
    """Проверка работы геттера цены."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    assert product.price == 15000


def test_negative_price_setter(capsys):
    """Проверка установки отрицательной цены."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    product.price = -100
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000


def test_zero_price_setter(capsys):
    """Проверка установки нулевой цены."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    product.price = 0
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
    assert product.price == 15000


@patch("builtins.input", return_value="n")
def test_price_decrease_rejected(mock_input, capsys):
    """Проверка отмены понижения цены."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    product.price = 14000

    # Проверяем, что input был вызван
    mock_input.assert_called_once()

    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product.price == 15000


@patch("builtins.input", return_value="y")
def test_price_decrease_accepted(mock_input, capsys):
    """Проверка подтверждения понижения цены."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    product.price = 14000

    # Проверяем, что input был вызван
    mock_input.assert_called_once()

    captured = capsys.readouterr()
    assert "Изменение цены отменено" not in captured.out
    assert product.price == 14000


def test_price_increase():
    """Проверка повышения цены без подтверждения."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    product.price = 16000
    assert product.price == 16000


def test_product_str():
    product = Product("Телефон", "Смартфон", 15000, 5)
    assert str(product) == "Телефон, 15000 руб. Остаток: 5 шт."


def test_product_add():
    p1 = Product("Товар1", "Описание", 100, 2)
    p2 = Product("Товар2", "Описание", 200, 3)
    assert p1 + p2 == 100 * 2 + 200 * 3


def test_product_add_invalid_type():
    p1 = Product("Товар", "Описание", 100, 1)
    with pytest.raises(TypeError):
        p1 + "не товар"


def test_product_addition():
    """Проверка сложения товаров"""
    p1 = Product("Товар1", "Описание", 100, 10)
    p2 = Product("Товар2", "Описание", 200, 2)
    assert p1 + p2 == 1400  # 100*10 + 200*2


def test_add_invalid_type():
    """Проверка сложения с неправильным типом"""
    p = Product("Товар", "Описание", 100, 1)
    with pytest.raises(TypeError):
        p + "не товар"
