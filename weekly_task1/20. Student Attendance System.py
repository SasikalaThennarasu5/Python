# Project 20: Student Attendance System
print("\\nProject 20: Student Attendance System")
students = ["Ravi", "Divya", "Kumar", "Reshma"]
statuses = ["P", "A", "P", "P"]
present_count = 0
for status in statuses:
    if status == "P":
        present_count += 1
print(f"Total Present: {present_count}")