from abc import ABC, abstractmethod
from typing import TypeVar

from src.models.product import Product

T = TypeVar("T", bound=Product)


class BaseOrderCategory(ABC):
    """Абстрактный базовый класс для заказов и категорий"""

    @abstractmethod
    def __init__(self, product: T, quantity: int) -> None:
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
