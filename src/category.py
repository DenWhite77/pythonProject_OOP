class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products=None):
        self.name = name
        self.description = description
        self.__products = products[:] if products else []
        Category.category_count += 1
        Category.product_count += len(self.__products)

    @property
    def products(self):
        if not self.__products:
            return "Нет товаров в категории."
        lines = [f"{prod.name}, {prod.price} руб. Остаток: {prod.quantity} шт." for prod in self.__products]
        return "\n".join(lines)

    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    def __str__(self):
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    @property
    def products_list(self):
        """Возвращает список товаров (для итератора)."""
        return self.__products


class CategoryIterator:
    """Итератор для перебора товаров в категории."""

    def __init__(self, category):
        self._products = category.products_list
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration
