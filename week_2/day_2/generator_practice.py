import string
from pathlib import Path

# Дополнительные символы, которые могут встречаться в русском тексте.
EXTRA_PUNCTUATION = "«»…—–"


def tokenize_line(line):
    """
    Превращает одну строку в список токенов.

    Токен — это отдельное слово.
    Пока мы делаем простую токенизацию:
    1. Переводим текст в нижний регистр.
    2. Заменяем знаки препинания на пробелы.
    3. Разбиваем строку по пробелам.
    """
    line = line.lower()

    punctuation = string.punctuation + EXTRA_PUNCTUATION

    for char in punctuation:
        line = line.replace(char, " ")

    # Возвращаем только непустые слова.
    return [word for word in line.split() if word]


def read_tokenized_lines(file_path):
    """
    Генератор, который читает файл построчно и возвращает
    список токенов для каждой непустой строки.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            # Пропускаем пустые строки.
            if not line:
                continue

            yield tokenize_line(line)


def read_all_tokens(file_path):
    """
    Генератор, который возвращает по одному токену из всего файла.
    """
    for tokens in read_tokenized_lines(file_path):
        for token in tokens:
            yield token


if __name__ == "__main__":
    # Путь к файлу рядом с этим скриптом.
    file_path = Path(__file__).resolve().parent / "reviews.txt"

    print(f"Читаем файл: {file_path}")

    print("\n=== Проверка протокола итератора ===")

    # Создаём генератор.
    iterator = read_all_tokens(file_path)

    try:
        print("Первый токен:", next(iterator))
        print("Второй токен:", next(iterator))
    except StopIteration:
        print("Файл пуст или токены закончились.")

    print("\n=== Первые 20 токенов ===")

    for index, token in enumerate(read_all_tokens(file_path), start=1):
        print(f"{index}: {token}")

        # Ограничимся первыми 20 токенами, чтобы не выводить весь файл.
        if index == 20:
            break

    print("\n=== Подсчёт строк и токенов ===")

    total_lines = 0
    total_tokens = 0

    for tokens in read_tokenized_lines(file_path):
        total_lines += 1
        total_tokens += len(tokens)

    print(f"Всего непустых строк: {total_lines}")
    print(f"Всего токенов: {total_tokens}")