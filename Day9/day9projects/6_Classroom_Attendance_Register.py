# Project 6: Classroom Attendance Register
attendance = [
    ("2025-07-01", ("Alice", "Bob")),
    ("2025-07-02", ("Alice", "Charlie")),
    ("2025-07-03", ("Bob", "Charlie"))
]

student = "Alice"
count = sum(1 for _, students in attendance if student in students)
print(f"{student} was present on {count} days.")