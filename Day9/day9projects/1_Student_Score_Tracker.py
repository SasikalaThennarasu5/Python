# Project 1: Student Score Tracker
students = [
    ("Alice", (85, 78, 92)),
    ("Bob", (75, 88, 80)),
    ("Charlie", (90, 85, 88))
]

for name, scores in students:
    print(f"Name: {name}")
    print(f"Math: {scores[0]}, Physics: {scores[1]}, Chemistry: {scores[2]}")
    average = sum(scores) / len(scores)
    print(f"Average: {average:.2f}\n")