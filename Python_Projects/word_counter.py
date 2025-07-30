
import os
from collections import defaultdict, Counter
from functools import wraps

# Decorator to measure execution time
import time
def time_execution(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.4f} seconds")
        return result
    return wrapper

class WordCounter:
    def __init__(self, filename):
        self.filename = filename
        self.word_freq = defaultdict(int)
        self.line_count = 0
        self.char_count = 0

    @time_execution
    def count_words(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                for line in file:
                    self.line_count += 1
                    self.char_count += len(line)
                    words = line.strip().split()
                    for word in words:
                        self.word_freq[word.lower()] += 1
        except FileNotFoundError:
            print("Error: File not found.")

    def most_common_word(self):
        if not self.word_freq:
            print("Run count_words() first.")
            return None
        counter = Counter(self.word_freq)
        return counter.most_common(1)[0]

    def display_summary(self):
        print(f"Lines: {self.line_count}")
        print(f"Characters: {self.char_count}")
        print(f"Unique words: {len(self.word_freq)}")
        most_common = self.most_common_word()
        if most_common:
            print(f"Most common word: '{most_common[0]}' ({most_common[1]} times)")

    def word_generator(self):
        for word in self.word_freq:
            yield word

# Example Usage
if __name__ == "__main__":
    filename = input("Enter the path to your text file: ")
    wc = WordCounter(filename)
    wc.count_words()
    wc.display_summary()

    print("\nWords in the file:")
    for word in wc.word_generator():
        print(word)
