import random
from question_bank import questions

def ask_question(q):
    print(q["question"])
    return input("Answer: ") == q["answer"]

def get_topics():
    return {q["topic"] for q in questions}

score = 0
for q in random.sample(questions, len(questions)):
    if ask_question(q):
        score += 1
print(f"Final Score: {score}/{len(questions)}")
print("Topics covered:", get_topics())