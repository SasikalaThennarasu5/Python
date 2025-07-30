import csv
from functools import wraps

# Decorator for memoizing GPA calculation
def memoize(func):
    cache = {}
    @wraps(func)
    def wrapper(self):
        key = tuple(self.marks.items())
        if key not in cache:
            cache[key] = func(self)
        return cache[key]
    return wrapper

# Student class using OOP
class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = self.validate_marks(marks)  # {subject: mark}

    def validate_marks(self, marks):
        for subject, mark in marks.items():
            if not (0 <= mark <= 100):
                raise ValueError(f"Invalid mark {mark} in {subject}. Must be between 0 and 100.")
        return marks

    @memoize
    def calculate_gpa(self):
        total = sum(self.marks.values())
        return round(total / len(self.marks), 2)

    def get_grade(self):
        gpa = self.calculate_gpa()
        if gpa >= 90:
            return 'A'
        elif gpa >= 80:
            return 'B'
        elif gpa >= 70:
            return 'C'
        elif gpa >= 60:
            return 'D'
        else:
            return 'F'

# Dictionary to store student records
students = {}

# Add student to dictionary
def add_student(student_id, name, marks):
    try:
        student = Student(student_id, name, marks)
        students[student_id] = student
    except ValueError as e:
        print(f"Error: {e}")

# Calculate class average
def class_average():
    if not students:
        return 0
    total = sum(student.calculate_gpa() for student in students.values())
    return round(total / len(students), 2)

# Find top student
def find_top_student():
    return max(students.values(), key=lambda s: s.calculate_gpa(), default=None)

# Export to CSV
def export_to_csv(filename="grades.csv"):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Student ID', 'Name', 'Subjects', 'GPA', 'Grade'])
        for student in students.values():
            subjects = "; ".join(f"{sub}: {mark}" for sub, mark in student.marks.items())
            writer.writerow([student.student_id, student.name, subjects, student.calculate_gpa(), student.get_grade()])
    print(f"Grades exported to {filename}")

# Generator for grade A students
def get_grade_a_students():
    for student in students.values():
        if student.get_grade() == 'A':
            yield student

# Get unique subjects
def get_unique_subjects():
    subjects = set()
    for student in students.values():
        subjects.update(student.marks.keys())
    return subjects

# ---------- Example Usage ----------
if __name__ == "__main__":
    add_student("S001", "Anjali", {"Math": 95, "Science": 92, "English": 88})
    add_student("S002", "Rahul", {"Math": 78, "Science": 80, "English": 85})
    add_student("S003", "Priya", {"Math": 91, "Science": 94, "English": 96})
    add_student("S004", "Vikram", {"Math": 55, "Science": 60, "English": 58})

    print(f"Class Average GPA: {class_average()}")

    top_student = find_top_student()
    if top_student:
        print(f"Top Student: {top_student.name} with GPA {top_student.calculate_gpa()}")

    print("\nGrade A Students:")
    for student in get_grade_a_students():
        print(f"{student.name} ({student.student_id})")

    print("\nUnique Subjects in Class:")
    print(get_unique_subjects())

    export_to_csv()
