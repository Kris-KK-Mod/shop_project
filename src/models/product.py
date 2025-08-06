from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, TypeVar

T = TypeVar("T", bound="BaseProduct")  # Изменено с Product на BaseProduct


class LogCreationMixin:
    """Миксин для логирования создания объектов."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Инициализация с логированием параметров."""
        super().__init__(*args, **kwargs)
        print(f"Создан объект {self.__class__.__name__} с параметрами:")
        print(f"Класс: {self.__class__.__name__}")
        print(f"Параметры: {self._repr_params()}")

    def _repr_params(self) -> str:
        """Вспомогательный метод для формирования параметров repr."""
        params = []
        for k, v in vars(self).items():
            if k.startswith("_Product__price"):
                params.append(f"price={v}")
            elif not k.startswith("_"):
                params.append(f"{k}={v!r}")
        return ", ".join(params)

    def __repr__(self) -> str:
        """Официальное строковое представление объекта."""
        return f"{self.__class__.__name__}({self._repr_params()})"


class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.quantity = quantity
        self.price = price
        self.description = description
        self.name = name

    @abstractmethod
    def __str__(self) -> str:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> float:
        pass

    @property
    @abstractmethod
    def price(self) -> float:
        pass

    @price.setter
    @abstractmethod
    def price(self, value: float) -> None:
        pass

    @classmethod
    @abstractmethod
    def new_product(
        cls: type[T],
        product_data: Dict[str, Any],
        products_list: Optional[List[T]] = None,
    ) -> T:
        pass


class Product(LogCreationMixin, BaseProduct):
    """Класс продукта с миксином для логирования."""

    def __init__(
        self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.quantity = quantity
        self.__price = price  # Сначала устанавливаем цену
        super().__init__(name, description, price, quantity)  # Затем вызываем миксин

    def __add__(self, other: Any) -> float:
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if not isinstance(self, type(other)):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if hasattr(self, "_Product__price") and new_price < self.__price:
            answer = input(
                f"Вы уверены, что хотите понизить цену с {
                    self.__price} до {new_price}? (y/n): "
            )
            if answer.lower() != "y":
                print("Изменение цены отменено")
                return

        self.__price = new_price

    @classmethod
    def new_product(
        cls: type["Product"],
        product_data: Dict[str, Any],
        products_list: Optional[List["Product"]] = None,
    ) -> "Product":
        name = product_data["name"]
        description = product_data["description"]
        price = float(product_data["price"])
        quantity = int(product_data["quantity"])

        if products_list:
            for existing_product in products_list:
                if existing_product.name.lower() == name.lower():
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    existing_product.description = description
                    return existing_product

        return cls(name, description, price, quantity)

    def merge_with(
        self, other_product: "Product", update_description: bool = True
    ) -> None:
        self.quantity += other_product.quantity
        self.price = max(self.price, other_product.price)
        if update_description:
            self.description = other_product.description
