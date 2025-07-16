# 1. Student Marks Manager

students = {}

# Add students
students["Arun"] = {"Math": 80, "Science": 75}
students["Divya"] = {"Math": 95, "Science": 88}

# Update marks
students["Arun"]["Science"] = 85

# Remove subject
students["Divya"].pop("Math", None)

# Remove student
students.pop("Divya", None)

# List all students and average marks
for name, subjects in students.items():
    avg = sum(subjects.values()) / len(subjects)
    print(f"{name} - Average: {avg:.2f}")

# Topper
topper = max(students.items(), key=lambda x: sum(x[1].values()))
print("Topper:", topper[0])

# Get with missing data
print(students.get("Ravi", "No record"))

# Passed students (avg > 50)
passed = {k: v for k, v in students.items() if sum(v.values()) / len(v) > 50}
print("Passed:", passed)