from typing import Iterator, List

from src.models.base_order_category import BaseOrderCategory
from src.models.product import Product


class Category(BaseOrderCategory):
    """Класс категории товаров"""

    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: List[Product]) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += sum(p.quantity for p in products)

    def __iter__(self) -> Iterator[Product]:
        return iter(self.__products)

    def __str__(self) -> str:
        total_quantity = sum(p.quantity for p in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def total_cost(self) -> float:
        return sum(p.price * p.quantity for p in self.__products)

    @property
    def products(self) -> str:
        return "\n".join(str(product) for product in self.__products)

    def add_product(self, product: Product) -> None:
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты Product или его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1
