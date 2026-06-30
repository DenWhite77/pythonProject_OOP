from src.base_model import BaseModel
from src.exceptions import ZeroQuantityError
from src.product import Product


class Category(BaseModel):
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products[:] if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        if not self.__products:
            return "Нет товаров в категории."
        return "\n".join([f"{p.name}, {p.price} руб. Остаток: {p.quantity} шт." for p in self.__products])

    def add_product(self, product):
        try:
            if not isinstance(product, Product):
                raise TypeError("Можно добавлять только объекты класса Product или его наследников")
            if product.quantity <= 0:
                raise ZeroQuantityError("Товар с нулевым количеством не может быть добавлен в категорию")
            self.__products.append(product)
            Category.product_count += 1
            print("Товар добавлен")
        except TypeError as e:
            print(f"Ошибка типа: {e}")
        except ZeroQuantityError as e:
            print(f"Ошибка: {e}")
        finally:
            print("Обработка добавления товара завершена")

    def middle_price(self):
        """Возвращает среднюю цену всех товаров в категории."""
        try:
            total = sum(product.price for product in self.__products)
            return total / len(self.__products)
        except ZeroDivisionError:
            return 0

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __repr__(self):
        return f"Category(name='{self.name}', products={len(self.__products)})"
