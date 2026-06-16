import json
from itertools import product


class Product:
    """Класс для представления товара."""
    def __init__(self, name: str, description: str, price: float, quantity: int):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} ({self.price} руб.) - осталось {self.quantity} шт."

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

    @property
    def price(self):
        """Геттер возвращает цену."""
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        if value < self.__price:
            answer = input(f"Цена понижается с {self.__price} до {value}. Подтвердите (y/n): ").strip().lower()
            if answer == 'y':
                self.__price = value
            else:
                print("Изменение цены отменено")
        else:
            self.__price = value

    @classmethod
    def new_product(cls, product_dict: dict):
        """Создаёт продукт из словаря."""
        return cls(
            name=product_dict['name'],
            description=product_dict['description'],
            price=product_dict['price'],
            quantity=product_dict['quantity']
        )

class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products[:] if products else []   # приватный список
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        """Геттер возвращает строковое представление списка товаров."""
        if not self.__products:
            return "Нет товаров в категории."
        lines = [f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products]
        return "\n".join(lines)

    def add_product(self, product):
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        return f"Категория: {self.name}, товаров: {len(self.__products)}"


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
