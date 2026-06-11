import json


class Product:
    """Класс для представления товара."""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.price} руб.) - осталось {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"


class Category:
    """Класс для представления категории товаров."""
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        self.name = name
        self.description = description
        self.products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        return f"Категория: {self.name}, товаров: {len(self.products)}"


def load_data_from_json(file_path: str):
    """Загружает данные из JSON-файла и возвращает список категорий.
       При ошибках (файл не найден, битый JSON) выводит сообщение и возвращает [].
    """
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
