from grade_utils.grades import add_student, calculate_grades, display_all_students

# Dictionary to hold student marks
students = {}

# Set of valid subjects
valid_subjects = {"Math", "Science", "English"}

# Add students
add_student(students, (1, "A001"), {"Math": 85, "Science": 78, "English": 90}, valid_subjects)
add_student(students, (2, "A002"), {"Math": 92, "Science": 88, "English": 95}, valid_subjects)
add_student(students, (3, "A003"), {"Math": 70, "Science": 60, "English": 65}, valid_subjects)

# Display results
display_all_students(students)
