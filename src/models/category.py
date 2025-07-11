class Category:
    """Класс для представления категории товаров """

    category_count = 0  # Общее количество категорий
    product_count = 0  # Общее количество товаров во всех категориях

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Инициализация категории.

        :param name: Название категории.
        :param description: Описание категории.
        :param products: Список товаров (объектов Product).
        """
        self.name = name
        self.description = description
        self.products = products

        # Автоматическое обновление атрибутов класса
        Category.category_count += 1
        Category.product_count += len(products)
