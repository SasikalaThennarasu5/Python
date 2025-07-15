# Project 20: Quiz Score Analyzer
scores = [
    (1, (80, 90, 85)),
    (2, (70, 60, 75)),
    (3, (88, 92, 95))
]

for uid, quizzes in scores:
    print(f"User {uid} - Best: {max(quizzes)}, Worst: {min(quizzes)}")