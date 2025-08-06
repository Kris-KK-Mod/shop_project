from src.models.category import Category
from src.models.product import Product


def test_category_total_cost():
    """Проверка расчета общей стоимости категории"""
    p1 = Product("Test1", "Test", 100, 2)
    p2 = Product("Test2", "Test", 200, 3)
    category = Category("Test", "Test", [p1, p2])
    assert category.total_cost == 100 * 2 + 200 * 3


def test_category_inheritance():
    """Проверка наследования от BaseOrderCategory"""
    from src.models.base_order_category import BaseOrderCategory

    assert issubclass(Category, BaseOrderCategory)


def test_products_property_format():
    """Проверка формата вывода геттера products"""
    product1 = Product("Телефон", "Смартфон", 15000, 3)
    product2 = Product("Ноутбук", "Игровой", 50000, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    result = category.products
    expected = (
        "Телефон, 15000 руб. Остаток: 3 шт.\n" "Ноутбук, 50000 руб." " Остаток: 5 шт."
    )

    assert result == expected
    assert "Телефон, 15000 руб. Остаток: 3 шт." in result
    assert "Ноутбук, 50000 руб. Остаток: 5 шт." in result


def test_empty_products_list():
    """Проверка вывода пустого списка товаров"""
    category = Category("Пустая", "Категория", [])
    assert category.products == ""


def test_category_str():
    products = [
        Product("Товар1", "Описание", 100, 2),
        Product("Товар2", "Описание", 200, 3),
    ]
    category = Category("Категория", "Описание", products)
    assert str(category) == "Категория, количество продуктов: 5 шт."  # 2 + 3 = 5


def test_products_property():
    products = [
        Product("Товар1", "Описание", 100, 2),
        Product("Товар2", "Описание", 200, 3),
    ]
    category = Category("Категория", "Описание", products)
    assert "Товар1, 100 руб. Остаток: 2 шт." in category.products
    assert "Товар2, 200 руб. Остаток: 3 шт." in category.products


def test_category_iteration():
    """Проверка работы итератора категории"""
    products = [
        Product("Товар1", "Описание", 100, 2),
        Product("Товар2", "Описание", 200, 3),
    ]
    category = Category("Категория", "Описание", products)

    # Проверяем итерацию
    for i, product in enumerate(category):
        assert product == products[i]

    # Альтернативная проверка
    assert list(category) == products
