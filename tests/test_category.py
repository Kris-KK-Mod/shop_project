import pytest
from src.models.category import Category
from src.models.product import Product


@pytest.fixture
def sample_products():
    """Фикстура с примером товаров для тестов."""
    return [
        Product("Телефон", "Смартфон", 50000.0, 10),
        Product("Ноутбук", "Игровой", 100000.0, 5),
    ]


def test_category_initialization(sample_products):
    """Проверяет корректность инициализации категории."""
    category = Category("Электроника", "Техника", sample_products)

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2


def test_category_count(sample_products):
    """Проверяет подсчёт количества категорий."""
    initial_count = Category.category_count
    _ = Category("Электроника", "Техника", sample_products)

    assert Category.category_count == initial_count + 1


def test_product_count(sample_products):
    """Проверяет подсчёт количества товаров."""
    initial_count = Category.product_count
    _ = Category("Электроника", "Техника", sample_products)

    assert Category.product_count == initial_count + len(sample_products)


def test_empty_category():
    """Проверяет создание категории без товаров."""
    initial_products = Category.product_count
    _ = Category("Пустая категория", "Нет товаров", [])

    assert Category.product_count == initial_products  # Количество товаров не изменилось
