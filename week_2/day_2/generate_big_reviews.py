from pathlib import Path

samples = [
    "Отличный товар, рекомендую!",
    "Так себе, качество слабое.",
    "Нормально, за свою цену ок.",
    "Очень понравилось, буду заказывать ещё.",
    "Ужасно, не советую.",
    "Доставка быстрая, упаковка целая.",
]

target = Path(__file__).resolve().parent / "reviews_big.txt"

with open(target, "w", encoding="utf-8") as file:
    for i in range(100_000):
        line = samples[i % len(samples)]
        file.write(line + "\n")

print(f"Файл создан: {target}")