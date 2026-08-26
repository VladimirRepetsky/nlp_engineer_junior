import numpy as np
import pandas as pd
from pathlib import Path


def print_section(title):
    """
    Вспомогательная функция для красивого вывода разделов.
    """
    print("\n" + "=" * 20 + f" {title} " + "=" * 20)


def create_sample_dataframe():
    """
    Создаёт учебный DataFrame с отзывами,
    похожий на данные из Дня 3.
    """
    data = {
        "id": [1, 2, 3, 4, 5, 6],
        "review_text": [
            "Отличный товар рекомендую",
            "Так себе качество слабое",
            "Нормально за свою цену ок",
            "Очень понравилось буду заказывать ещё",
            "Ужасно не советую",
            "Супер качество доставка быстрая",
        ],
        "rating": [5, 2, 3, 4, 1, 5],
        "author": ["Анна", "Иван", "Мария", "Олег", "Света", "Петр"],
    }

    return pd.DataFrame(data)


if __name__ == "__main__":
    # Пытаемся использовать CSV из Дня 3
    day3_csv = Path(__file__).resolve().parents[1] / "day_3" / "reviews.csv"

    # Если его нет, создаём локальный CSV для Дня 5
    local_csv = Path(__file__).resolve().parent / "reviews.csv"

    if day3_csv.exists():
        csv_path = day3_csv
        print("Используем CSV из Дня 3:")
        print(csv_path)
    else:
        csv_path = local_csv

        if not csv_path.exists():
            df_to_save = create_sample_dataframe()
            df_to_save.to_csv(csv_path, index=False, encoding="utf-8")
            print("CSV из Дня 3 не найден.")
            print("Создан учебный CSV:")
            print(csv_path)
        else:
            print("Используем локальный CSV:")
            print(csv_path)

    # Загружаем DataFrame
    df = pd.read_csv(csv_path, encoding="utf-8")

    print_section("Исходный DataFrame")
    print(df)

    # =========================================================
    # 1. Одномерный массив из списка
    # =========================================================
    print_section("1. Одномерный массив")

    ratings_list = df["rating"].tolist()
    ratings_array = np.array(ratings_list)

    print("Список:")
    print(ratings_list)
    print("Тип списка:", type(ratings_list))

    print("\nМассив:")
    print(ratings_array)
    print("Тип массива:", type(ratings_array))

    print("\nАтрибуты одномерного массива:")
    print("shape:", ratings_array.shape)
    print("ndim:", ratings_array.ndim)
    print("dtype:", ratings_array.dtype)
    print("size:", ratings_array.size)

    # =========================================================
    # 2. Двумерный массив вручную
    # =========================================================
    print_section("2. Двумерный массив")

    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])

    print(matrix)

    print("\nАтрибуты двумерного массива:")
    print("shape:", matrix.shape)
    print("ndim:", matrix.ndim)
    print("dtype:", matrix.dtype)
    print("size:", matrix.size)

    # =========================================================
    # 3. Разница между списком и массивом
    # =========================================================
    print_section("3. Список против массива")

    print("Список + 10 через list comprehension:")
    list_result = [x + 10 for x in ratings_list]
    print(list_result)

    print("\nМассив + 10 одной строкой:")
    array_result = ratings_array + 10
    print(array_result)

    # =========================================================
    # 4. Операции над двумерным массивом
    # =========================================================
    print_section("4. Операции над массивом")

    print("Исходный массив:")
    print(matrix)

    print("\nПрибавить 10 ко всем элементам:")
    print(matrix + 10)

    print("\nУмножить все элементы на 2:")
    print(matrix * 2)

    print("\nСложить массив сам с собой:")
    print(matrix + matrix)

    # =========================================================
    # 5. Агрегация: сумма, среднее, максимум
    # =========================================================
    print_section("5. Агрегация")

    print("Сумма всех элементов:")
    print(matrix.sum())

    print("\nСумма по столбцам (axis=0):")
    print(matrix.sum(axis=0))

    print("\nСумма по строкам (axis=1):")
    print(matrix.sum(axis=1))

    print("\nСреднее по всем элементам:")
    print(matrix.mean())

    print("\nСреднее по столбцам (axis=0):")
    print(matrix.mean(axis=0))

    print("\nМаксимум по всем элементам:")
    print(matrix.max())

    # =========================================================
    # 6. DataFrame -> NumPy array
    # =========================================================
    print_section("6. DataFrame to NumPy")

    # Добавляем новый числовой признак
    df["text_length"] = df["review_text"].str.len()

    print("DataFrame с новым столбцом text_length:")
    print(df)

    # Создаём 2D-массив из двух числовых колонок
    feature_array = df[["rating", "text_length"]].to_numpy()

    print("\n2D-массив из колонок rating и text_length:")
    print(feature_array)

    print("\nАтрибуты этого массива:")
    print("shape:", feature_array.shape)
    print("ndim:", feature_array.ndim)
    print("dtype:", feature_array.dtype)
    print("size:", feature_array.size)

    # =========================================================
    # 7. Математические операции над массивом из DataFrame
    # =========================================================
    print_section("7. Математика над массивом из DataFrame")

    print("Исходный массив:")
    print(feature_array)

    print("\nПрибавить 1 ко всем элементам:")
    print(feature_array + 1)

    print("\nУмножить все элементы на 2:")
    print(feature_array * 2)

    print("\nСложить массив сам с собой:")
    print(feature_array + feature_array)

    print("\nСреднее по столбцам:")
    print("rating mean, text_length mean")
    print(feature_array.mean(axis=0))

    print("\nСреднее по строкам:")
    print(feature_array.mean(axis=1))

    # =========================================================
    # 8. Индексация и срезы
    # =========================================================
    print_section("8. Индексация и срезы")

    print("Первая строка массива:")
    print(feature_array[0])

    print("\nПервые 3 строки:")
    print(feature_array[0:3])

    print("\nТолько первая колонка, то есть rating:")
    print(feature_array[:, 0])

    print("\nТолько вторая колонка, то есть text_length:")
    print(feature_array[:, 1])