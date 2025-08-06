import pytest

from src.models.category import Category
from src.models.product import Product


def test_add_valid_product():
    category = Category("Test", "Test", [])
    product = Product("Test", "Test", 100, 1)
    category.add_product(product)
    assert len(category.products.split("\n")) == 1


def test_add_invalid_product():
    category = Category("Test", "Test", [])
    with pytest.raises(TypeError):
        category.add_product("не продукт")
