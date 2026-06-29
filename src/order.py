from src.base_model import BaseModel
from src.product import Product


class Order(BaseModel):
    """Класс для представления заказа."""

    def __init__(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("Товар должен быть объектом класса Product или его наследников")
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным числом")
        if quantity > product.quantity:
            raise ValueError(f"Недостаточно товара на складе. Доступно: {product.quantity}")

        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        return f"Заказ: {self.product.name}, {self.quantity} шт., итого: {self.total_price} руб."

    def __repr__(self):
        return f"Order(product={self.product.name!r}, quantity={self.quantity}, total_price={self.total_price})"
