# Student Grading System
def grade_student(marks):
    if any(m < 35 for m in marks):
        print("Re-evaluation needed.")
        return grade_student([int(input(f"Re-enter mark {i+1}: ")) for i in range(5)])
    avg = sum(marks) / 5
    if avg >= 90: grade = 'A'
    elif avg >= 75: grade = 'B'
    elif avg >= 50: grade = 'C'
    else: grade = 'D'
    return avg, grade

marks = [int(input(f"Enter mark {i+1}: ")) for i in range(5)]
average, grade = grade_student(marks)
print("Average:", average, "| Grade:", grade)
