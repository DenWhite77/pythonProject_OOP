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
    assert cat.products == [p1, p2]
    assert Category.category_count == 1
    assert Category.product_count == 2


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
