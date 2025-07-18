def add_student(students: dict, student_id: tuple, marks: dict, valid_subjects: set):
    if student_id in students:
        print(f"Student {student_id} already exists.")
        return
    if set(marks.keys()) != valid_subjects:
        print(f"Invalid subjects for student {student_id}. Must include: {valid_subjects}")
        return
    students[student_id] = marks
    print(f"Added student {student_id}")


def calculate_grades(marks: dict):
    avg = sum(marks.values()) / len(marks)
    if avg >= 90:
        return "A"
    elif avg >= 75:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "D"


def display_all_students(students: dict):
    print("\n--- Student Grades ---")
    for student_id, marks in students.items():
        grade = calculate_grades(marks)
        print(f"ID: {student_id} | Marks: {marks} | Grade: {grade}")
