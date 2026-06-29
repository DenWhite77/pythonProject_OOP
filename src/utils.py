import json

from category import Category
from product import Product


def load_data_from_json(file_path: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Ошибка: файл {file_path} не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка: файл {file_path} содержит некорректный JSON.")
        return []

    categories = []
    for cat_data in data:
        products = []
        for prod_data in cat_data.get('products', []):
            product = Product(
                name=prod_data['name'],
                description=prod_data['description'],
                price=prod_data['price'],
                quantity=prod_data['quantity']
            )
            products.append(product)
        category = Category(
            name=cat_data['name'],
            description=cat_data['description'],
            products=products
        )
        categories.append(category)
    return categories
