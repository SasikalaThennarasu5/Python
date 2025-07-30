import csv
import functools

class Student:
    def __init__(self, student_id, name, marks):
        self.student_id = student_id
        self.name = name
        self.marks = marks  # Dictionary of subject: mark

    def calculate_gpa(self):
        total = sum(self.marks.values())
        return round(total / len(self.marks), 2)

    def get_grade(self):
        avg = self.calculate_gpa()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'

students = {}

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(student_id):
        if student_id not in cache:
            cache[student_id] = func(student_id)
        return cache[student_id]
    return wrapper

def add_student():
    student_id = input("Enter ID: ")
    name = input("Enter name: ")
    marks = {}
    subjects = set()
    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        try:
            score = float(input(f"Enter marks for {subject}: "))
            if 0 <= score <= 100:
                marks[subject] = score
                subjects.add(subject)
            else:
                print("Marks should be between 0 and 100.")
        except ValueError:
            print("Invalid marks.")
    students[student_id] = Student(student_id, name, marks)
    print(f"{name} added successfully.")

@memoize
def get_gpa(student_id):
    return students[student_id].calculate_gpa()

def top_student():
    if not students:
        print("No students added.")
        return
    top = max(students.values(), key=lambda s: s.calculate_gpa())
    print(f"Top student: {top.name} with GPA {top.calculate_gpa()}")

def export_to_csv():
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "GPA", "Grade"])
        for student in students.values():
            writer.writerow([student.student_id, student.name, student.calculate_gpa(), student.get_grade()])
    print("Grades exported to grades.csv")

def class_average():
    if not students:
        print("No students added.")
        return
    avg = sum(s.calculate_gpa() for s in students.values()) / len(students)
    print(f"Class average GPA: {round(avg, 2)}")

def grade_A_students():
    for student in students.values():
        if student.get_grade() == 'A':
            yield student

def menu():
    while True:
        print("\n--- Student Grade Calculator ---")
        print("1. Add Student")
        print("2. Show Top Student")
        print("3. Export Grades")
        print("4. Class Average")
        print("5. Show Grade A Students")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            add_student()
        elif choice == '2':
            top_student()
        elif choice == '3':
            export_to_csv()
        elif choice == '4':
            class_average()
        elif choice == '5':
            for student in grade_A_students():
                print(f"{student.name} ({student.student_id}) - GPA: {student.calculate_gpa()}")
        elif choice == '6':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
