# Project 2: Online Exam Result Evaluator
print("\\nProject 2: Online Exam Result Evaluator")
marks = [45, 56, 72, 61, 39]
if any(m < 35 for m in marks):
    print("Result: Fail")
else:
    total = sum(marks)
    percentage = total / len(marks)
    if percentage >= 90:
        print("Grade: A")
    elif percentage >= 75:
        print("Grade: B")
    elif percentage >= 60:
        print("Grade: C")
    else:
        print("Grade: D")