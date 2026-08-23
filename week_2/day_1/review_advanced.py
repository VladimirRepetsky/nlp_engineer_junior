class Review:
    """
    Класс отзыва с использованием атрибутов класса и декоратора @property.
    """
    # 1. АТРИБУТ КЛАССА
    # Он общий для всех экземпляров. Хранит общее количество созданных отзывов.
    total_reviews = 0
    
    def __init__(self, text: str, rating: int, author: str):
        # 2. АТРИБУТЫ ЭКЗЕМПЛЯРА
        self.text = text
        self.author = author
        
        # Используем "приватную" переменную _rating (нижнее подчеркивание), 
        # чтобы работать с ней через property
        self._rating = None 
        self.rating = rating  # При присваивании вызовется сеттер (ниже)
        
        # Увеличиваем атрибут класса
        Review.total_reviews += 1

    # 3. ДЕКОРАТОР @property (Геттер)
    # Превращает метод в свойство. Теперь можно писать review.rating вместо review.rating()
    @property
    def rating(self) -> int:
        return self._rating

    # 4. СЕТТЕР (@rating.setter)
    # Позволяет контролировать, какие значения записываются в атрибут.
    @rating.setter
    def rating(self, value: int):
        if not isinstance(value, int):
            raise TypeError("Рейтинг должен быть целым числом")
        if not (1 <= value <= 5):
            raise ValueError("Рейтинг должен быть в диапазоне от 1 до 5")
        self._rating = value

    # 5. ВЫЧИСЛЯЕМОЕ СВОЙСТВО (Главное задание дня из программы)
    # Возвращает True, если рейтинг выше 3 (то есть 4 или 5).
    @property
    def is_positive(self) -> bool:
        return self._rating > 3

    def __repr__(self) -> str:
        return f"Review(author={self.author!r}, rating={self.rating}, positive={self.is_positive})"


if __name__ == "__main__":
    print(f"Отзывов до создания: {Review.total_reviews}")
    
    # Создаем объекты
    review_1 = Review("Отличный товар, рекомендую!", 5, "Анна")
    review_2 = Review("Так себе, качество слабое.", 2, "Иван")
    review_3 = Review("Нормально, за свою цену ок.", 3, "Мария")
    
    print(f"Отзывов после создания: {Review.total_reviews}")
    print("-" * 40)
    
    # Проверяем вычисляемое свойство is_positive (обращаемся БЕЗ скобок!)
    for r in [review_1, review_2, review_3]:
        print(r)
        if r.is_positive:
            print(f"  -> Отзыв от {r.author} положительный! ✅")
        else:
            print(f"  -> Отзыв от {r.author} отрицательный/нейтральный. ❌")
            
    print("-" * 40)
    # Проверяем работу сеттера (защита от некорректных данных извне)
    try:
        print("Попытка изменить рейтинг review_2 на 10...")
        review_2.rating = 10
    except ValueError as e:
        print(f"Ошибка перехвачена: {e}")