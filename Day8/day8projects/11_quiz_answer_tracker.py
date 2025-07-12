# Quiz Answer Tracker

correct_answers = ["A", "C", "B", "D"]
user_answers = ["A", "C", "A", "D"]

correct = 0
for i in range(len(correct_answers)):
    if user_answers[i] == correct_answers[i]:
        correct += 1

print(f"Correct: {correct}, Incorrect: {len(correct_answers) - correct}")
