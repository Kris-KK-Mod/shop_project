from src.models.product import Product

if __name__ == "__main__":
    # Создаем товар
    product = Product("Ноутбук", "Игровой", 50000, 3)

    # Проверяем геттер
    print(f"Текущая цена: {product.price}")

    # Пытаемся установить отрицательную цену
    product.price = -100

    # Пытаемся понизить цену
    product.price = 45000

    # Увеличиваем цену
    product.price = 55000
    print(f"Новая цена: {product.price}")
