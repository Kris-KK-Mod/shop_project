import pytest
from unittest.mock import patch
from src.models.product import Product


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


@patch('builtins.input', return_value='n')
def test_price_decrease_rejected(mock_input, capsys):
    """Проверка отмены понижения цены."""
    product = Product("Телефон", "Смартфон", 15000, 5)
    product.price = 14000

    # Проверяем, что input был вызван
    mock_input.assert_called_once()

    captured = capsys.readouterr()
    assert "Изменение цены отменено" in captured.out
    assert product.price == 15000


@patch('builtins.input', return_value='y')
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
    assert p1 + p2 == 100*2 + 200*3


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