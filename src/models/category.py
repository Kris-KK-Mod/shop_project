from src.models.product import Product


class Category:
    """Класс для представления категории товаров."""

    category_count = 0
    product_count = 0


    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация категории.

        :param name: Название категории
        :param description: Описание категории
        :param products: Список товаров (объектов Product)
        """
        self.name = name
        self.description = description
        self.__products = products  # Приватный атрибут
        Category.category_count += 1
        Category.product_count += len(products)


    def __iter__(self):
        """Возвращает итератор для перебора товаров категории"""
        return iter(self.__products)  # Используем встроенный iter()


    def __str__(self):
        """Строковое представление категории"""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."


    @property
    def products(self):
        """
        Геттер для вывода списка товаров в заданном формате.
        Возвращает строку с перечислением товаров.
        """
        return "\n".join(str(product) for product in self.__products)


    def add_product(self, product):
        """Добавление продукта с проверкой типа"""
        if not isinstance(product, Product):
            raise TypeError("Можно добавлять только объекты Product или его наследников")
        self.__products.append(product)
        Category.product_count += 1
