# 20. Quiz Grader App
# Scenario: Auto-grade a multiple-choice quiz with displayed questions

# List of questions, options, and correct answers
questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
        "answer": "C"
    },
    {
        "question": "2. Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Venus", "C. Jupiter", "D. Mars"],
        "answer": "D"
    },
     {
        "question": "3. Which shape has 3 sides?",
        "options": ["A. Circle", "B. Square", "C. Triangle", "D. Rectangle"],
        "answer": "C"
    },
    {
        "question": "4. What is the boiling point of water?",
        "options": ["A. 50°C", "B. 90°C", "C. 100°C", "D. 110°C"],
        "answer": "C"
    },
    {
        "question": "5. What is the chemical symbol for Gold?",
        "options": ["A. Gd", "B. Go", "C. G", "D. Au"],
        "answer": "D"
    }
]

user_answers = []
score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans not in ['A', 'B', 'C', 'D']:
        print(" Invalid choice! Exiting quiz.")
        exit()
    
    user_answers.append(ans)

# Use loop to compare and count correct responses.
for i in range(len(questions)):
    if user_answers[i] == questions[i]["answer"]:
        score += 1

# Use if to assign grade based on score.
if score == 5:
    grade = "A+"
elif score >= 4:
    grade = "A"
elif score >= 3:
    grade = "B"
elif score >= 2:
    grade = "C"
else:
    grade = "F"

print("\n------ Quiz Results ------")
for i in range(len(questions)):
    print(f"Q{i+1}: Your Answer: {user_answers[i]} | Correct: {questions[i]['answer']}")
print(f"\nScore : {score} / 5")
print(f"Grade : {grade}")
print("--------------------------")
