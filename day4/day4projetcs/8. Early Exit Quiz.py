# Project 8: Early Exit Quiz
print("\nProject 8: Early Exit Quiz")
questions = [
    ("What is 2+2?", "4"),
    ("Capital of India?", "Delhi"),
    ("Color of sky?", "Blue"),
    ("Largest planet?", "Jupiter"),
    ("Python is a ___?", "Language")
]
for q, ans in questions:
    user_answer = ans  # Simulated correct answer
    if user_answer.lower() != ans.lower():
        print("Game Over")
        break
else:
    print("Quiz Completed!")