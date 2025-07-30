
import random
import string

def validate_input(func):
    def wrapper(*args, **kwargs):
        guess = args[1]
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabet letter.")
            return None
        return func(*args, **kwargs)
    return wrapper

def load_words(filename="words.txt"):
    try:
        with open(filename, "r") as file:
            return file.read().split()
    except FileNotFoundError:
        return ["python", "hangman", "challenge", "programming"]

def hint_generator(word, guessed_letters):
    hints = [char if char in guessed_letters else "_" for char in word]
    yield "".join(hints)

class Hangman:
    def __init__(self, word):
        self.word = word
        self.attempts = 6
        self.guessed_letters = []

    @validate_input
    def guess(self, letter):
        letter = letter.lower()
        if letter in self.guessed_letters:
            print("Already guessed.")
            return
        self.guessed_letters.append(letter)
        if letter not in self.word:
            self.attempts -= 1

    def display_word(self):
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.word])

    def is_won(self):
        return all(letter in self.guessed_letters for letter in self.word)

    def play(self):
        print("Welcome to Hangman!")
        while self.attempts > 0 and not self.is_won():
            print(f"Word: {self.display_word()}")
            print(f"Attempts left: {self.attempts}")
            guess = input("Guess a letter: ")
            self.guess(guess)
            if self.attempts == 3:
                print("Hint:", next(hint_generator(self.word, self.guessed_letters)))
        if self.is_won():
            print(f"Congratulations! You guessed the word: {self.word}")
        else:
            print(f"You lost. The word was: {self.word}")

if __name__ == "__main__":
    words = load_words()
    word = random.choice(words)
    game = Hangman(word)
    game.play()
