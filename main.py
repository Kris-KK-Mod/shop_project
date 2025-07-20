from src.models.product import Product
from src.models.category import Category

if __name__ == "__main__":
    # Создаем товары
    p1 = Product("iPhone", "128GB", 80000, 10)
    p2 = Product("Galaxy", "256GB", 70000, 5)

    # Демонстрация сложения
    print(f"Общая стоимость: {p1 + p2} руб.")  # 80000*10 + 70000*5

    # Создаем категорию
    category = Category("Смартфоны", "Флагманы", [p1, p2])

    # Демонстрация итератора
    print("\nТовары в категории:")
    for product in category:
        print(product)
