# Project 4: Student Score Analyzer
print("\nProject 4: Student Score Analyzer")
marks = [78, 92, 88, 64, 95]
maximum = marks[0]
minimum = marks[0]
total = 0
for mark in marks:
    if mark > maximum:
        maximum = mark
    if mark < minimum:
        minimum = mark
    total += mark
average = total / len(marks)
print(f"Highest: {maximum}, Lowest: {minimum}, Average: {average:.2f}")