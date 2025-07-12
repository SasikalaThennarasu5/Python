students = []

def calculate_grade():
    name = input("Enter student name: ")
    marks = []
    for i in range(3):
        marks.append(float(input(f"Enter subject {i+1} marks: ")))
    avg = sum(marks) / len(marks)
    if avg >= 90: grade = 'A'
    elif avg >= 75: grade = 'B'
    elif avg >= 60: grade = 'C'
    elif avg >= 40: grade = 'D'
    else: grade = 'F'
    students.append({'name': name, 'avg': avg, 'grade': grade})
    print(f"{name} -> Average: {avg:.2f}, Grade: {grade}")

while True:
    ch = input("Add student record? (y/n): ")
    if ch.lower() == 'y': calculate_grade()
    else: break

