from product import Product

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
        return f"Категория: {self.name}, товаров: {len(self.__products)}"
    