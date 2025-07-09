# Project 8: Number Guessing Game
secret = 7
tries = 0
while tries < 5:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    tries += 1
else:
    print("Out of tries!")
