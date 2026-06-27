from unittest.mock import patch
import sys
from pathlib import Path

# Добавляем путь к корневой папке проекта, чтобы импортировать модули из src
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from product import Product
from category import Category

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
    # Дополнительно можно проверить, что приватный список содержит товары
    assert len(cat._Category__products) == 2


def test_product_count_multiple_categories():
    Category.category_count = 0
    Category.product_count = 0
    p1 = Product("A", "", 10, 1)
    p2 = Product("B", "", 20, 1)
    p3 = Product("C", "", 30, 1)
    cat1 = Category("C1", "", [p1, p2])
    assert cat1.name == "C1"               # используем cat1
    assert Category.product_count == 2
    cat2 = Category("C2", "", [p3])
    assert cat2.name == "C2"               # используем cat2
    assert Category.product_count == 3


def test_category_count_only_on_creation():
    Category.category_count = 0
    Category.product_count = 0
    cat1 = Category("C1", "", [])
    assert cat1.name == "C1"               # используем cat1
    assert Category.category_count == 1
    cat2 = Category("C2", "", [])
    assert cat2.name == "C2"               # используем cat2
    assert Category.category_count == 2


def test_empty_category_does_not_increase_product_count():
    Category.category_count = 0
    Category.product_count = 0
    cat = Category("Пустая", "Нет товаров", [])
    assert cat.name == "Пустая"            # используем cat
    assert Category.product_count == 0
    assert Category.category_count == 1


def test_product_price_setter_negative():
    p = Product("Test", "Desc", 100, 10)
    p.price = -50
    assert p.price == 100  # цена не изменилась

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
    assert len(cat._Category__products) == 1   # доступ к приватному атрибуту (для теста)

# ===================== НОВЫЕ ТЕСТЫ ДЛЯ ДЗ 15.1 =====================
def test_product_str_format():
    """Тест строкового представления продукта (ДЗ 15.1)."""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."
    assert str(product) == expected


def test_category_str_format():
    """Тест строкового представления категории с подсчётом общего количества (ДЗ 15.1)."""
    p1 = Product("Product1", "Desc1", 100.0, 5)
    p2 = Product("Product2", "Desc2", 200.0, 3)
    p3 = Product("Product3", "Desc3", 300.0, 7)
    category = Category("Electronics", "Electronic devices", [p1, p2, p3])
    expected = "Electronics, количество продуктов: 15 шт."
    assert str(category) == expected


def test_category_str_empty():
    """Тест строкового представления пустой категории (ДЗ 15.1)."""
    category = Category("Empty", "Empty category", [])
    expected = "Empty, количество продуктов: 0 шт."
    assert str(category) == expected


def test_category_products_uses_str():
    """Тест, что геттер products использует __str__ продукта (ДЗ 15.1)."""
    p1 = Product("Samsung", "Desc", 180000.0, 5)
    p2 = Product("Iphone", "Desc", 210000.0, 8)
    category = Category("Смартфоны", "Описание", [p1, p2])

    expected = (
        "Samsung, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone, 210000.0 руб. Остаток: 8 шт."
    )
    assert category.products == expected


def test_product_str_after_price_change():
    """Тест, что __str__ обновляется после изменения цены (ДЗ 15.1)."""
    product = Product("Test", "Desc", 100.0, 10)
    assert str(product) == "Test, 100.0 руб. Остаток: 10 шт."

    # Меняем цену (для теста используем прямое изменение, чтобы обойти сеттер)
    product._Product__price = 150.0
    assert str(product) == "Test, 150.0 руб. Остаток: 10 шт."