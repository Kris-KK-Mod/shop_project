from src.models.category import Category
from src.models.products.lawn_grass import LawnGrass
from src.models.products.smartphone import Smartphone


if __name__ == "__main__":
    # Создаем продукты разных типов
    phone = Smartphone("iPhone", "Cool", 100000, 5, "A15", "13", 128, "black")
    grass = LawnGrass("Grass", "Green", 500, 10, "Russia", "2 weeks", "green")

    # Пытаемся сложить разные типы
    try:
        total = phone + grass  # Вызовет TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")

    # Работа с категорией
    category = Category("Electronics", "Devices", [])
    category.add_product(phone)

    # Пытаемся добавить не продукт
    try:
        category.add_product("Not a product")  # Вызовет TypeError
    except TypeError as e:
        print(f"Ошибка: {e}")
