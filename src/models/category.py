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


    @property
    def products(self):
        """
        Геттер для вывода списка товаров в заданном формате.
        Возвращает строку с перечислением товаров.
        """
        products_list = []
        for product in self.__products:
            products_list.append(
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт."
            )
        return "\n".join(products_list)


    def add_product(self, product):
        """
        Добавляет товар в категорию.

        :param product: Объект класса Product
        """
        self.__products.append(product)
        Category.product_count += 1
