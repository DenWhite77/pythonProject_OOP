# 1. Импорты из модуля abc
from abc import ABC, abstractmethod

from src.base_model import BaseModel
from src.log_mixin import LogMixin  # импортируем миксин


# 2. Абстрактный базовый класс BaseProduct
class BaseProduct(ABC):
    """Абстрактный базовый класс для всех продуктов."""

    @abstractmethod
    def get_total_price(self) -> float:
        """Возвращает общую стоимость всех единиц товара."""
        pass

    @abstractmethod
    def __str__(self) -> str:
        """Возвращает строковое представление продукта."""
        pass


# 3. Класс Product (наследует BaseProduct)
class Product(LogMixin, BaseProduct, BaseModel):
    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)  # ← передаём параметры!
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def get_total_price(self) -> float:
        """Реализация абстрактного метода."""
        return self.price * self.quantity

    @property
    def price(self):
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
        return cls(
            name=product_dict['name'],
            description=product_dict['description'],
            price=product_dict['price'],
            quantity=product_dict['quantity']
        )

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product или его наследников")
        if type(self) is not type(other):
            raise TypeError(f"Нельзя складывать объекты разных классов: {type(self).__name__} и {type(other).__name__}")
        return self.price * self.quantity + other.price * other.quantity

    def __repr__(self):
        # Если атрибуты уже установлены — выводим их
        if hasattr(self, 'name'):
            return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
        # Если атрибутов ещё нет — используем параметры из LogMixin
        if hasattr(self, '_log_params'):
            args = self._log_params.get('args', ())
            kwargs = self._log_params.get('kwargs', {})
            params = ', '.join([repr(a) for a in args] + [f"{k}={v!r}" for k, v in kwargs.items()])
            return f"Product({params})"
        # Если ничего нет — возвращаем имя класса
        return "Product()"
