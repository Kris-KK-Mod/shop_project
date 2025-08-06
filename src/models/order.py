from abc import ABC, abstractmethod
from typing import TypeVar

from src.models.product import Product

T = TypeVar("T", bound=Product)


class BaseOrderCategory(ABC):
    """Абстрактный базовый класс для заказов и категорий"""

    @abstractmethod
    def __init__(self, product: T, quantity: int):
        self.product = product
        self.quantity = quantity

    @property
    @abstractmethod
    def total_cost(self) -> float:
        """Итоговая стоимость"""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Строковое представление"""
        pass


class Order(BaseOrderCategory):
    """Класс заказа"""

    def __init__(self, product: Product, quantity: int):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        super().__init__(product, quantity)

    @property
    def total_cost(self) -> float:
        return self.product.price * self.quantity

    def __str__(self) -> str:
        return f"Order: {self.product.name} x{self.quantity} = {self.total_cost} руб."
