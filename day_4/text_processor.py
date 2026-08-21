import string


class TextProcessor:
    """
    Базовый класс для всех обработчиков текста.

    Он задаёт общий интерфейс: метод process().
    Дочерние классы должны переопределить этот метод.
    """

    def __init__(self, name=None):
        # Если имя не передали, используем название текущего класса.
        self.name = name if name is not None else self.__class__.__name__

        # Счётчик обработанных текстов.
        self.processed_count = 0

    def process(self, text: str) -> str:
        """
        Базовый метод обработки текста.

        Дочерние классы должны переопределить его.
        """
        raise NotImplementedError(
            "Дочерний класс должен реализовать метод process()"
        )

    def __repr__(self):
        return f"{self.name}(processed_count={self.processed_count})"


class LowerCaseProcessor(TextProcessor):
    """
    Дочерний класс, который переводит текст в нижний регистр.
    """

    def process(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Метод process() должен получать строку")

        self.processed_count += 1
        return text.lower()


class RemoveStopwordsProcessor(TextProcessor):
    """
    Дочерний класс, который удаляет стоп-слова.
    """

    DEFAULT_STOPWORDS = {
        "и",
        "в",
        "на",
        "с",
        "по",
        "не",
        "что",
        "как",
        "это",
        "из",
        "к",
        "о",
        "от",
        "за",
        "для",
        "же",
        "бы",
        "то",
        "а",
        "но",
        "так",
        "себе",
        "его",
        "ее",
        "её",
        "их",
        "мы",
        "вы",
        "он",
        "она",
        "оно",
        "они",
    }

    def __init__(self, stopwords=None):
        # Вызываем конструктор родительского класса.
        super().__init__()

        if stopwords is None:
            self.stopwords = self.DEFAULT_STOPWORDS
        else:
            self.stopwords = set(stopwords)

    def process(self, text: str) -> str:
        if not isinstance(text, str):
            raise TypeError("Метод process() должен получать строку")

        self.processed_count += 1

        # Переводим текст в нижний регистр.
        text = text.lower()

        # Удаляем пунктуацию.
        for punct in string.punctuation:
            text = text.replace(punct, " ")

        # Разбиваем текст на слова.
        words = text.split()

        # Убираем стоп-слова.
        filtered_words = [
            word for word in words if word not in self.stopwords
        ]

        # Соединяем слова обратно в строку.
        return " ".join(filtered_words)


class TextPipeline:
    """
    Класс, который последовательно применяет несколько обработчиков текста.

    Это уже мини-модель будущего NLP-пайплайна.
    """

    def __init__(self, processors):
        self.processors = processors

    def run(self, text: str) -> str:
        for processor in self.processors:
            text = processor.process(text)
        return text


if __name__ == "__main__":
    reviews = [
        "Отличный товар, рекомендую!",
        "Так себе, качество слабое.",
        "Нормально, за свою цену ок.",
    ]

    pipeline = TextPipeline(
        processors=[
            LowerCaseProcessor(),
            RemoveStopwordsProcessor(),
        ]
    )

    for review in reviews:
        print("До обработки:", review)
        print("После обработки:", pipeline.run(review))
        print("-" * 40)

    print("Информация об обработчиках:")
    for processor in pipeline.processors:
        print(processor)