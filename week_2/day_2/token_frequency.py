from collections import Counter
from pathlib import Path

from generator_practice import read_all_tokens

file_path = Path(__file__).resolve().parent / "reviews.txt"

counter = Counter(read_all_tokens(file_path))

print("Самые частые токены:")
for token, count in counter.most_common(10):
    print(f"{token}: {count}")