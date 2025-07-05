# Project 1: Student Report Card Generator
print("Project 1: Student Report Card Generator")
name = "Arun"
std_class = "10th"
marks = [85, 90, 78, 88, 92]
total = sum(marks)
average = total / len(marks)
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
else:
    grade = "D"
print(f"Name: {name}, Class: {std_class}, Total: {total}, Average: {average:.2f}, Grade: {grade}")