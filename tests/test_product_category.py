import pytest
from unittest.mock import patch
import sys
from pathlib import Path

# Добавляем путь к корневой папке проекта, чтобы импортировать модули из src
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from product_category import Product, Category  # noqa: E402


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
