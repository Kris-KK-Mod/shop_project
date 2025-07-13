from src.models.category import Category
from src.models.product import Product


def test_products_property_format():
    """Проверка формата вывода геттера products"""
    product1 = Product("Телефон", "Смартфон", 15000, 3)
    product2 = Product("Ноутбук", "Игровой", 50000, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    result = category.products
    expected = (
        "Телефон, 15000 руб. Остаток: 3 шт.\n"
        "Ноутбук, 50000 руб. Остаток: 5 шт."
    )

    assert result == expected
    assert "Телефон, 15000 руб. Остаток: 3 шт." in result
    assert "Ноутбук, 50000 руб. Остаток: 5 шт." in result


def test_empty_products_list():
    """Проверка вывода пустого списка товаров"""
    category = Category("Пустая", "Категория", [])
    assert category.products == ""
