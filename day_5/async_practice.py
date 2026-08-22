import asyncio
import time


async def load_reviews(source, delay):
    """
    Имитация долгой загрузки отзывов.
    Вместо реального запроса к сети мы используем asyncio.sleep(delay).
    """
    print(f"Начинаю загрузку отзывов из: {source}")

    await asyncio.sleep(delay)

    print(f"Закончил загрузку отзывов из: {source}")

    return [f"отзыв из {source}"]


async def run_sequential():
    """
    Последовательный запуск.
    Сначала ждём первую загрузку, потом вторую.
    """
    start = time.perf_counter()

    first = await load_reviews("Amazon", 2)
    second = await load_reviews("IMDB", 2)

    finish = time.perf_counter()

    return first + second, finish - start


async def run_parallel():
    """
    Параллельный запуск через asyncio.gather().
    Обе задачи стартуют и выполняются одновременно.
    """
    start = time.perf_counter()

    first, second = await asyncio.gather(
        load_reviews("Amazon", 2),
        load_reviews("IMDB", 2)
    )

    finish = time.perf_counter()

    return first + second, finish - start


async def main():
    print("=== Последовательный запуск ===")

    sequential_data, sequential_time = await run_sequential()

    print(sequential_data)
    print(f"Время последовательного запуска: {sequential_time:.2f} секунд")
    print()

    print("=== Параллельный запуск через asyncio.gather() ===")

    parallel_data, parallel_time = await run_parallel()

    print(parallel_data)
    print(f"Время параллельного запуска: {parallel_time:.2f} секунд")
    print()

    print(f"Разница во времени: {sequential_time - parallel_time:.2f} секунд")


if __name__ == "__main__":
    asyncio.run(main())