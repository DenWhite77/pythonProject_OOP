# OOP-14.1 Homework: Product and Category

## Описание
Проект реализует классы `Product` и `Category` для управления товарами и 
категориями, а также функцию загрузки данных из JSON.

## Установка и запуск
1. Клонировать репозиторий:
   ```
   git clone https://github.com/твой_логин/pythonProject_OOP.git
   cd pythonProject_OOP
   
2. Создать виртуальное окружение и активировать:
   ```
   python -m venv .venv
   .venv\Scripts\activate   # Windows

3. Установить зависимости:
   ```
   pip install -r requirements.txt
   Запустить тесты:

4. Запустить тесты:
   ```
   pytest tests/ -v
   
5. Посмотреть отчёт о покрытии:
    ```
   pytest --cov=src --cov-report=html tests/
  ( # )затем открыть htmlcov/index.html
   
## Тестирование и покрытие
   ```
   Все тесты проходят.
   Покрытие кода: 100% (сгенерирован отчёт в папке htmlcov)

## Структура проекта
   
   src/product_category.py – классы Product и Category;

   tests/test_product_category.py – тесты.

   products.json – данные для загрузки.

   main.py – пример использования.

   requirements.txt – зависимости.

   .gitignore – игнорируемые файлы.
 