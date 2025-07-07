# 1. Student Grade Calculator 
# Scenario: A school wants to generate grades based on student scores.

# Input: Student name and marks in 5 subjects using variables and list
student_name = input("Enter the student's name: ")
marks = []

for i in range(1, 6):
    mark = float(input(f"Enter mark for subject {i}: "))
    marks.append(mark)

# Use for loop to calculate total and average
total = 0
for mark in marks:
    total += mark
average = total / 5

# Use if-elif-else to determine grade
# ≥90 → A, ≥80 → B, ≥70 → C, else → D
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
else:
    grade = 'D'

# Output the grade with the student’s name using f-string
print("\n------ Student Report ------")
print(f"Name           : {student_name}")
print(f"Total Marks    : {total}")
print(f"Average Marks  : {average:.2f}")
print(f"Grade          : {grade}")
print("----------------------------")
