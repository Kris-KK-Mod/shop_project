class Product:
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity


    def __add__(self, other):
        """Сложение с проверкой типов"""
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты Product")
        if type(self) != type(other):
            raise TypeError("Нельзя складывать товары разных классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."


    @property
    def price(self):
        """Геттер для цены."""
        return self.__price


    @price.setter
    def price(self, new_price):
        """
        Сеттер для цены с проверками.

        :param new_price: Новая цена
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if new_price < self.__price:
            # Дополнительное задание: подтверждение понижения цены
            answer = input(f"Вы уверены, что хотите понизить цену с {self.__price} до {new_price}? (y/n): ")
            if answer.lower() != 'y':
                print("Изменение цены отменено")
                return

        self.__price = new_price


    @classmethod
    def new_product(cls, product_data: dict, products_list: list = None):
        """
        Создает новый товар или обновляет существующий.

        :param product_data: Словарь с данными товара
        :param products_list: Список существующих товаров
        :return: Объект Product
        """
        name = product_data['name']
        description = product_data['description']
        price = float(product_data['price'])
        quantity = int(product_data['quantity'])

        if products_list:
            for existing_product in products_list:
                if existing_product.name.lower() == name.lower():
                    # Обновляем существующий товар
                    existing_product.quantity += quantity
                    existing_product.price = max(existing_product.price, price)
                    existing_product.description = description  # <- Вот ключевая строка
                    return existing_product

        return cls(name, description, price, quantity)


    def merge_with(self, other_product: 'Product', update_description: bool = True):
        """Объединяет данные с другим товаром"""
        self.quantity += other_product.quantity
        self.price = max(self.price, other_product.price)
        if update_description:
            self.description = other_product.description


    def __repr__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."
