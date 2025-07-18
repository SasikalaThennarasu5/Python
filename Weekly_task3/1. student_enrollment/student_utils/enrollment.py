# Handles student enrollment and data storage

students = {}

def add_student(student_id, name):
    if student_id in students:
        print(f"Student with ID {student_id} already exists.")
    else:
        students[student_id] = {
            'name': name,
            'courses': set()
        }
        print(f"Added student: {name} (ID: {student_id})")

def enroll_course(student_id, course):
    if student_id not in students:
        print(f"Student ID {student_id} not found.")
        return

    if course in students[student_id]['courses']:
        print(f"Student already enrolled in {course}.")
    else:
        students[student_id]['courses'].add(course)
        print(f"{students[student_id]['name']} enrolled in {course}")

def get_student_info(student_id):
    return students.get(student_id, None)

def list_students():
    return students
