from abc import ABC

import pytest

from src.models.order import Order
from src.models.product import Product


def test_order_creation():
    """Проверка создания заказа"""
    p = Product("Test", "Test", 100, 10)
    order = Order(p, 3)
    assert order.product == p
    assert order.quantity == 3
    assert order.total_cost == 300


def test_order_str():
    """Проверка строкового представления заказа"""
    p = Product("Test", "Test", 100, 10)
    order = Order(p, 2)
    assert str(order) == "Order: Test x2 = 200 руб."


def test_invalid_quantity():
    """Проверка обработки недопустимого количества"""
    p = Product("Test", "Test", 100, 10)
    with pytest.raises(ValueError):
        Order(p, 0)
    with pytest.raises(ValueError):
        Order(p, -1)


def test_base_order_category_abstract():
    """Проверка абстрактности BaseOrderCategory"""
    from src.models.base_order_category import BaseOrderCategory

    with pytest.raises(TypeError):

        class InvalidOrder(BaseOrderCategory, ABC):
            pass

        p = Product("Test", "Test", 100, 10)
        InvalidOrder(p, 1)
