from typing import TYPE_CHECKING, Iterator

from src.models.product import Product

if TYPE_CHECKING:
    from src.models.category import Category


class CategoryIterator:
    """Итератор для перебора товаров категории"""

    def __init__(self, category: "Category") -> None:
        self._category = category
        self._index = 0

    def __iter__(self) -> Iterator[Product]:
        return self

    def __next__(self) -> Product:
        """Получаем следующий продукт в категории"""
        products = self._get_products()
        if self._index < len(products):
            product = products[self._index]
            self._index += 1
            return product
        raise StopIteration

    def _get_products(self) -> list[Product]:
        """Безопасный доступ к списку продуктов категории"""
        # Используем публичный интерфейс Category
        if hasattr(self._category, "products"):
            return list(self._category)  # Используем итератор категории
        raise AttributeError("Category has no products list")
