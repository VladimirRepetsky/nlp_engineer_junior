# Импортируем модуль csv.
# Он нужен для работы с файлами формата CSV.
#
# CSV — это табличный формат, где значения обычно разделены запятыми.
# Например:
# name,price,category
# Laptop,1200,electronics
import csv

# Импортируем Path для удобной работы с путями.
from pathlib import Path


# Получаем папку, в которой лежит текущий файл products_csv.py.
BASE_DIR = Path(__file__).resolve().parent

# Путь к CSV-файлу, который будем создавать и читать.
CSV_FILE = BASE_DIR / "products.csv"


# Исходные данные.
# Это такой же список словарей, как в основной практике.
products = [
    {
        "name": "Laptop",
        "price": 1200,
        "category": "electronics"
    },
    {
        "name": "Headphones",
        "price": 150,
        "category": "electronics"
    },
    {
        "name": "Notebook",
        "price": 5,
        "category": "stationery"
    },
    {
        "name": "Coffee Mug",
        "price": 12,
        "category": "kitchen"
    },
    {
        "name": "Smartphone",
        "price": 800,
        "category": "electronics"
    }
]


# Функция для сохранения товаров в CSV-файл.
def save_products_csv(products, file_path):
    """
    Сохраняет список товаров в CSV-файл.

    Параметры:
        products: список словарей с данными о товарах.
        file_path: путь к CSV-файлу.
    """

    # Если список товаров пустой, тогда нет смысла создавать CSV.
    if not products:
        print("Список товаров пустой. CSV-файл не создан.")
        return

    # Берём названия колонок из ключей первого словаря.
    #
    # Например, если первый товар такой:
    # {
    #     "name": "Laptop",
    #     "price": 1200,
    #     "category": "electronics"
    # }
    #
    # То fieldnames будет:
    # ["name", "price", "category"]
    fieldnames = list(products[0].keys())

    # Открываем CSV-файл для записи.
    #
    # mode="w" означает запись.
    # encoding="utf-8" — кодировка.
    # newline="" важно при работе с csv в Windows,
    # чтобы не появлялись лишние пустые строки.
    with open(file_path, mode="w", encoding="utf-8", newline="") as file:

        # csv.DictWriter умеет записывать словари в CSV.
        # Он использует fieldnames как заголовки колонок.
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        # Записываем заголовки:
        # name,price,category
        writer.writeheader()

        # Записываем все товары.
        # Каждый словарь станет одной строкой в CSV.
        writer.writerows(products)


# Функция для чтения товаров из CSV-файла.
def load_products_csv(file_path):
    """
    Читает список товаров из CSV-файла.

    Параметры:
        file_path: путь к CSV-файлу.

    Возвращает:
        Список словарей с данными о товарах.
    """

    # Создаём пустой список, куда будем складывать прочитанные товары.
    products_from_csv = []

    # Открываем CSV-файл для чтения.
    with open(file_path, mode="r", encoding="utf-8", newline="") as file:

        # csv.DictReader читает CSV и превращает каждую строку в словарь.
        # Заголовки колонок становятся ключами.
        reader = csv.DictReader(file)

        # Проходимся по каждой строке CSV.
        for row in reader:

            # Важный момент:
            # CSV хранит все значения как строки.
            #
            # Поэтому price после чтения будет строкой, например "1200",
            # а не числом 1200.
            #
            # Чтобы потом можно было фильтровать товары по цене,
            # превращаем price в число с плавающей точкой.
            row["price"] = float(row["price"])

            # Добавляем обработанную строку в список товаров.
            products_from_csv.append(row)

    # Возвращаем список товаров.
    return products_from_csv


# Функция для фильтрации товаров по цене.
def filter_products_by_price(products, max_price):
    """
    Возвращает товары, цена которых меньше или равна max_price.

    Параметры:
        products: список словарей с товарами.
        max_price: максимальная цена.

    Возвращает:
        Отфильтрованный список товаров.
    """

    # Пустой список для результата.
    filtered_products = []

    # Проходим по каждому товару.
    for product in products:

        # Проверяем цену.
        if product["price"] <= max_price:
            filtered_products.append(product)

    # Возвращаем результат.
    return filtered_products


# Функция для красивого вывода товаров.
def print_products(products, title):
    """
    Печатает список товаров в удобном виде.

    Параметры:
        products: список словарей с товарами.
        title: заголовок.
    """

    print(title)

    # Если товаров нет, выводим сообщение.
    if not products:
        print("Ничего не найдено.")
        print()
        return

    # Печатаем каждый товар.
    for product in products:
        print(
            f"Название: {product['name']} | "
            f"Цена: {product['price']} | "
            f"Категория: {product['category']}"
        )

    print()


# Главная функция для CSV-практики.
def main():
    """
    Главная функция CSV-практики.
    Здесь мы:
    1. Сохраняем товары в CSV.
    2. Читаем товары из CSV.
    3. Фильтруем товары по цене.
    """

    # Сохраняем товары в CSV-файл.
    save_products_csv(products, CSV_FILE)

    # Сообщаем, что файл сохранён.
    print(f"Товары сохранены в CSV-файл: {CSV_FILE}")
    print()

    # Читаем товары из CSV.
    loaded_products = load_products_csv(CSV_FILE)

    # Печатаем все товары из CSV.
    print_products(loaded_products, "Все товары из CSV:")

    # Фильтруем товары по цене.
    cheap_products = filter_products_by_price(loaded_products, 100)

    # Печатаем дешёвые товары.
    print_products(cheap_products, "Товары с ценой меньше или равной 100:")


# Запускаем главную функцию только если файл запустили напрямую.
if __name__ == "__main__":
    main()