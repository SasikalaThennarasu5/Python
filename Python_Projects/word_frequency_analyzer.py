from collections import Counter
import re

def read_and_clean_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read().lower()
        # Remove non-alphabetic characters and split into words
        words = re.findall(r'\b[a-z]+\b', text)
        return words
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

def yield_top_words(word_list, top_n=10):
    counter = Counter(word_list)
    for word, freq in counter.most_common(top_n):
        yield word, freq

if __name__ == "__main__":
    path = input("Enter file path: ")
    words = read_and_clean_file(path)
    print(f"Top words in {path}:")
    for word, freq in yield_top_words(words):
        print(f"{word}: {freq}")
