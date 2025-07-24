import random
class GameOverError(Exception): pass

def guess_game():
    number = random.randint(1, 10)
    tries = 0
    while tries < 5:
        try:
            guess = int(input("Guess: "))
            if guess == number:
                print("Correct!")
                return
            tries += 1
        except ValueError:
            print("Enter a number")
    raise GameOverError("Too many attempts")