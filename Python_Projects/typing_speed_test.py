import time
import random

sample_texts = [
    "The quick brown fox jumps over the lazy dog.",
    "Python programming is fun and versatile.",
    "Always test your code thoroughly before deployment."
]

results = []

def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        return result, end - start
    return wrapper

def yield_words(text):
    for word in text.split():
        yield word

@timed
def typing_test(text):
    print("Type the following text as fast as you can:")
    print(text)
    input("Press Enter to start...")
    user_input = input("> ")
    return user_input == text

def save_high_score(duration):
    with open("high_scores.txt", "a") as f:
        f.write(f"{duration:.2f} seconds\n")

if __name__ == "__main__":
    text = random.choice(sample_texts)
    correct, duration = typing_test(text)
    if correct:
        print(f"Great! You typed it in {duration:.2f} seconds.")
        save_high_score(duration)
    else:
        print("Text did not match. Try again.")
