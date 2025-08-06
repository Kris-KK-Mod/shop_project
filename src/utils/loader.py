import json
from pathlib import Path
from typing import List

from ..models.category import Category
from ..models.product import Product


def load_data_from_json(file_path: str) -> List[Category]:
    """
    Загружает данные о категориях и товарах из JSON-файла
    """
    try:
        abs_path = Path(__file__).parent.parent / file_path
        if not abs_path.exists():
            raise FileNotFoundError(f"Файл {abs_path} не найден")

        with open(abs_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        categories = []
        for category_data in data.get("categories", []):
            products = []
            for product_data in category_data.get("products", []):
                try:
                    product = Product(
                        name=product_data["name"],
                        description=product_data["description"],
                        price=float(product_data["price"]),
                        quantity=int(product_data["quantity"]),
                    )
                    products.append(product)
                except (KeyError, ValueError) as e:
                    print(f"Ошибка при создании товара: {e}")
                    continue

            try:
                category = Category(
                    name=category_data["name"],
                    description=category_data["description"],
                    products=products,
                )
                categories.append(category)
            except KeyError as e:
                print(f"Ошибка при создании категории: {e}")
                continue

        return categories
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Ошибка парсинга JSON: {e}", e.doc, e.pos)
