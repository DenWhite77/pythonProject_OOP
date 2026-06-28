class Product:
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

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
