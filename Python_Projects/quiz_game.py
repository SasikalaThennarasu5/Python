
import json
import time
from functools import wraps
from random import shuffle

# Decorator to time quiz duration
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Time taken: {end - start:.2f} seconds")
        return result
    return wrapper

# Question class
class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def __str__(self):
        opt_str = "\n".join([f"{i+1}. {opt}" for i, opt in enumerate(self.options)])
        return f"{self.question}\n{opt_str}"

# Generator to yield questions one by one
def question_generator(questions):
    for q in questions:
        yield q

# Load questions from a JSON file
def load_questions(filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file)
            questions = []
            for item in data:
                questions.append(Question(item['question'], item['options'], item['answer']))
            return questions
    except FileNotFoundError:
        print("Questions file not found.")
        return []

# Run quiz and calculate score
@timer
def start_quiz(questions):
    score = 0
    q_gen = question_generator(questions)
    for q in q_gen:
        print("\n" + str(q))
        try:
            choice = int(input("Your answer (1-4): "))
            if q.options[choice - 1].lower() == q.answer.lower():
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! Correct answer: {q.answer}")
        except (ValueError, IndexError):
            print("Invalid input.")
    print(f"\nYour final score: {score}/{len(questions)}")

# Main function
def main():
    questions = load_questions("quiz_questions.json")
    if questions:
        shuffle(questions)
        start_quiz(questions)

if __name__ == "__main__":
    main()
