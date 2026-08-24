import pandas as pd
from pathlib import Path


def print_section(title):
    """
    Небольшая вспомогательная функция, чтобы красиво выводить разделы.
    """
    print("\n" + "=" * 20 + f" {title} " + "=" * 20)


if __name__ == "__main__":
    # =========================================================
    # 1. Создаём Series из списка
    # =========================================================
    print_section("1. Series из списка")

    ratings = pd.Series([5, 2, 3, 4, 1], name="rating")

    print(ratings)
    print("Средний рейтинг:", ratings.mean())
    print("Максимальный рейтинг:", ratings.max())
    print("Минимальный рейтинг:", ratings.min())

    # =========================================================
    # 2. Создаём DataFrame из словаря
    # =========================================================
    print_section("2. DataFrame из словаря")

    data = {
        "id": [1, 2, 3, 4, 5],
        "review_text": [
            "Отличный товар рекомендую",
            "Так себе качество слабое",
            "Нормально за свою цену ок",
            "Очень понравилось буду заказывать ещё",
            "Ужасно не советую",
        ],
        "rating": [5, 2, 3, 4, 1],
        "author": ["Анна", "Иван", "Мария", "Олег", "Света"],
    }

    df = pd.DataFrame(data)

    print(df)

    # =========================================================
    # 3. Базовые атрибуты DataFrame
    # =========================================================
    print_section("3. Базовая информация о DataFrame")

    print("df.shape:", df.shape)
    print("df.columns:", list(df.columns))
    print("df.index:", list(df.index))

    print("\nТипы данных в колонках:")
    print(df.dtypes)

    print("\nПервые 3 строки:")
    print(df.head(3))

    print("\nИнформация о DataFrame:")
    df.info()

    print("\nСтатистика по числовым колонкам:")
    print(df.describe())

    print("\nСтатистика по всем колонкам:")
    print(df.describe(include="all"))

    # =========================================================
    # 4. Работа с отдельной колонкой
    # =========================================================
    print_section("4. Работа с колонкой rating")

    print(df["rating"])

    print("\nСредний рейтинг:", df["rating"].mean())
    print("Медианный рейтинг:", df["rating"].median())

    print("\nСколько отзывов с каждым рейтингом:")
    print(df["rating"].value_counts().sort_index())

    # =========================================================
    # 5. Сохраняем DataFrame в CSV
    # =========================================================
    print_section("5. Сохранение в CSV")

    csv_path = Path(__file__).resolve().parent / "reviews.csv"

    df.to_csv(csv_path, index=False, encoding="utf-8")

    print("CSV сохранён сюда:")
    print(csv_path)

    # =========================================================
    # 6. Загружаем CSV обратно в DataFrame
    # =========================================================
    print_section("6. Загрузка CSV в DataFrame")

    df_loaded = pd.read_csv(csv_path, encoding="utf-8")

    print(df_loaded.head())

    print("\ndf_loaded.shape:", df_loaded.shape)

    print("\nИнформация о загруженном DataFrame:")
    df_loaded.info()

    print("\nПервые 2 отзыва:")
    print(df_loaded["review_text"].head(2))

    # =========================================================
    # 7. Маленький мостик к Дню 4: фильтрация
    # =========================================================
    print_section("7. Простая фильтрация")

    positive_reviews = df_loaded[df_loaded["rating"] > 3]

    print("Отзывы с рейтингом больше 3:")
    print(positive_reviews)