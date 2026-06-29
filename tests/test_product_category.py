"""Тест: добавление смартфона в категорию работает."""
from unittest.mock import patch

import pytest

from src.category import Category
from src.lawn_grass import LawnGrass
from src.log_mixin import LogMixin
# Импорты с абсолютным путём (указываем src.)
from src.product import BaseProduct, Product
from src.smartphone import Smartphone


# ===== СТАРЫЕ ТЕСТЫ (из прошлых ДЗ) =====
def test_product_initialization():
    p = Product("Ноутбук", "Игровой", 150000.0, 3)
    assert p.name == "Ноутбук"
    assert p.description == "Игровой"
    assert p.price == 150000.0
    assert p.quantity == 3


def test_category_initialization():
    Category.category_count = 0
    Category.product_count = 0
    p1 = Product("Товар1", "Описание1", 100, 1)
    p2 = Product("Товар2", "Описание2", 200, 2)
    cat = Category("Электроника", "Техника", [p1, p2])
    assert cat.name == "Электроника"
    assert cat.description == "Техника"
    products_str = cat.products
    assert "Товар1, 100 руб. Остаток: 1 шт." in products_str
    assert "Товар2, 200 руб. Остаток: 2 шт." in products_str
    assert len(cat._Category__products) == 2


def test_product_count_multiple_categories():
    Category.category_count = 0
    Category.product_count = 0
    p1 = Product("A", "", 10, 1)
    p2 = Product("B", "", 20, 1)
    p3 = Product("C", "", 30, 1)
    cat1 = Category("C1", "", [p1, p2])
    assert cat1.name == "C1"
    assert Category.product_count == 2
    cat2 = Category("C2", "", [p3])
    assert cat2.name == "C2"
    assert Category.product_count == 3


def test_category_count_only_on_creation():
    Category.category_count = 0
    Category.product_count = 0
    cat1 = Category("C1", "", [])
    assert cat1.name == "C1"
    assert Category.category_count == 1
    cat2 = Category("C2", "", [])
    assert cat2.name == "C2"
    assert Category.category_count == 2


def test_empty_category_does_not_increase_product_count():
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Пустая", "Нет товаров", [])
    assert cat.name == "Пустая"
    assert Category.product_count == 0
    assert Category.category_count == 1


def test_product_price_setter_negative():
    p = Product("Test", "Desc", 100, 10)
    p.price = -50
    assert p.price == 100


def test_product_price_setter_lower_with_confirmation_yes():
    p = Product("Test", "Desc", 100, 10)
    with patch('builtins.input', return_value='y'):
        p.price = 80
    assert p.price == 80


def test_product_price_setter_lower_with_confirmation_no():
    p = Product("Test", "Desc", 100, 10)
    with patch('builtins.input', return_value='n'):
        p.price = 80
    assert p.price == 100


def test_product_new_product_creates_instance():
    data = {"name": "A", "description": "B", "price": 10, "quantity": 2}
    p = Product.new_product(data)
    assert p.name == "A"
    assert p.price == 10


def test_category_products_property_returns_string():
    p = Product("A", "", 10, 1)
    cat = Category("Cat", "", [p])
    result = cat.products
    assert "A, 10 руб. Остаток: 1 шт." in result
    assert isinstance(result, str)


def test_category_add_product_increases_product_count():
    cat = Category("Cat", "", [])
    p = Product("A", "", 10, 1)
    old_count = Category.product_count
    cat.add_product(p)
    assert Category.product_count == old_count + 1
    assert len(cat._Category__products) == 1


# ===== ТЕСТЫ ДЛЯ ДЗ 15.1 =====
def test_product_str_format():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product) == expected


def test_category_str_format():
    p1 = Product("Product1", "Desc1", 100.0, 5)
    p2 = Product("Product2", "Desc2", 200.0, 3)
    p3 = Product("Product3", "Desc3", 300.0, 7)
    category = Category("Electronics", "Electronic devices", [p1, p2, p3])
    expected = "Electronics, количество продуктов: 15 шт."
    assert str(category) == expected


def test_category_str_empty():
    category = Category("Empty", "Empty category", [])
    expected = "Empty, количество продуктов: 0 шт."
    assert str(category) == expected


def test_category_products_uses_str():
    p1 = Product("Samsung", "Desc", 180000.0, 5)
    p2 = Product("Iphone", "Desc", 210000.0, 8)
    category = Category("Смартфоны", "Описание", [p1, p2])
    expected = (
        "Samsung, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone, 210000.0 руб. Остаток: 8 шт."
    )
    assert category.products == expected


def test_product_str_after_price_change():
    product = Product("Test", "Desc", 100.0, 10)
    assert str(product) == "Test, 100.0 руб. Остаток: 10 шт."
    product._Product__price = 150.0
    assert str(product) == "Test, 150.0 руб. Остаток: 10 шт."


# ===== ТЕСТЫ ДЛЯ ДЗ 16 =====
def test_smartphone_creation():
    phone = Smartphone("Samsung", "Desc", 1000.0, 10, 95.5, "S23", 256, "Серый")
    assert phone.name == "Samsung"
    assert phone.price == 1000.0
    assert phone.quantity == 10
    assert phone.efficiency == 95.5
    assert phone.model == "S23"
    assert phone.memory == 256
    assert phone.color == "Серый"


def test_lawn_grass_creation():
    grass = LawnGrass("Трава", "Desc", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert grass.name == "Трава"
    assert grass.price == 500.0
    assert grass.quantity == 20
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"


def test_smartphone_is_product():
    phone = Smartphone("Samsung", "Desc", 1000.0, 10, 95.5, "S23", 256, "Серый")
    assert isinstance(phone, Product)
    assert issubclass(Smartphone, Product)


def test_lawn_grass_is_product():
    grass = LawnGrass("Трава", "Desc", 500.0, 20, "Россия", "7 дней", "Зеленый")
    assert isinstance(grass, Product)
    assert issubclass(LawnGrass, Product)


def test_add_same_class_smartphone():
    phone1 = Smartphone("Samsung", "Desc", 1000.0, 5, 95.5, "S23", 256, "Серый")
    phone2 = Smartphone("Iphone", "Desc", 2000.0, 3, 98.0, "15", 512, "Black")
    result = phone1 + phone2
    assert result == 1000 * 5 + 2000 * 3


def test_add_same_class_lawn_grass():
    grass1 = LawnGrass("Трава1", "Desc", 500.0, 10, "Россия", "7 дней", "Зеленый")
    grass2 = LawnGrass("Трава2", "Desc", 300.0, 5, "США", "5 дней", "Синий")
    result = grass1 + grass2
    assert result == 500 * 10 + 300 * 5


def test_add_different_classes_raises_type_error():
    phone = Smartphone("Samsung", "Desc", 1000.0, 5, 95.5, "S23", 256, "Серый")
    grass = LawnGrass("Трава", "Desc", 500.0, 10, "Россия", "7 дней", "Зеленый")
    with pytest.raises(TypeError, match="Нельзя складывать объекты разных классов"):
        _ = phone + grass


def test_add_product_raises_type_error():
    category = Category("Тест", "Описание", [])
    with pytest.raises(TypeError, match="Можно добавлять только объекты класса Product или его наследников"):
        category.add_product("Not a product")


def test_add_product_smartphone_to_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Смартфоны", "Описание", [])
    phone = Smartphone("Samsung", "Desc", 1000.0, 5, 95.5, "S23", 256, "Серый")
    category.add_product(phone)
    assert Category.product_count == 1
    assert "Samsung" in category.products


def test_add_product_lawn_grass_to_category():
    Category.category_count = 0
    Category.product_count = 0

    category = Category("Трава", "Описание", [])
    grass = LawnGrass("Трава", "Desc", 500.0, 10, "Россия", "7 дней", "Зеленый")
    category.add_product(grass)
    assert Category.product_count == 1
    assert "Трава" in category.products


def test_product_count_with_mixed_types():
    Category.category_count = 0
    Category.product_count = 0

    phone = Smartphone("Samsung", "Desc", 1000.0, 5, 95.5, "S23", 256, "Серый")
    grass = LawnGrass("Трава", "Desc", 500.0, 10, "Россия", "7 дней", "Зеленый")
    product = Product("Обычный", "Desc", 100.0, 2)

    cat = Category("Смешанная", "Описание", [phone, grass, product])
    assert cat.name == "Смешанная"
    assert Category.product_count == 3


# ===================== НОВЫЕ ТЕСТЫ ДЛЯ ДЗ 16.2 =====================
def test_base_product_cannot_be_instantiated():
    """Тест: нельзя создать объект абстрактного класса BaseProduct."""
    with pytest.raises(TypeError, match="Can't instantiate abstract class BaseProduct"):
        BaseProduct()  # Должен выбросить TypeError


def test_product_implements_abstract_methods():
    """Тест: Product реализует все абстрактные методы BaseProduct."""
    # Проверяем, что у Product есть метод get_total_price
    assert hasattr(Product, 'get_total_price'), "Product должен реализовывать get_total_price"
    assert hasattr(Product, '__str__'), "Product должен реализовывать __str__"

    # Проверяем, что методы работают
    product = Product("Test", "Desc", 100.0, 5)
    assert product.get_total_price() == 500.0
    assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."


def test_product_is_subclass_of_base_product():
    """Тест: Product является наследником BaseProduct."""
    assert issubclass(Product, BaseProduct), "Product должен наследовать BaseProduct"


def test_log_mixin_is_used_in_product():
    """Тест: Product использует LogMixin в цепочке наследования."""
    assert LogMixin in Product.__mro__, "LogMixin должен быть в цепочке наследования Product"


def test_log_mixin_prints_on_creation(capsys):
    """Тест: при создании Product вызывается LogMixin и печатает лог."""
    Product("Test", "Description", 100.0, 10)
    captured = capsys.readouterr()
    assert "!!! ЛОГИРУЕМ СОЗДАНИЕ ОБЪЕКТА !!!" in captured.out
    assert "Product('Test', 'Description', 100.0, 10)" in captured.out


def test_log_mixin_repr_format():
    """Тест: формат вывода LogMixin соответствует ожидаемому."""
    product = Product("TestProduct", "Test description", 150.0, 3)
    assert repr(product) == "Product(name='TestProduct', price=150.0, quantity=3)"


def test_log_mixin_with_multiple_products(capsys):
    """Тест: каждый новый продукт логируется отдельно."""
    p1 = Product("First", "Desc1", 100.0, 1)
    p2 = Product("Second", "Desc2", 200.0, 2)
    captured = capsys.readouterr()
    # Проверяем, что в выводе есть оба продукта
    assert "First" in captured.out
    assert "Second" in captured.out
    assert "100.0" in captured.out
    assert "200.0" in captured.out
    assert p1.name == "First"
    assert p2.name == "Second"
