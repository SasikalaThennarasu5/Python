# 🔥 3. Student Grade Evaluator
name = input("Enter student name: ")
marks = [float(input(f"Enter marks for subject {i+1}: ")) for i in range(5)]
avg = sum(marks) / 5
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
else:
    grade = "D"
print(f"{name}'s average is {avg} and grade is {grade}")