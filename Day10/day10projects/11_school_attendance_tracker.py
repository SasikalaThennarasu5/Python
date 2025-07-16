# 11. School Attendance Tracker

attendance = {
    "2025-07-15": ["Arun", "Divya"],
    "2025-07-16": ["Divya", "Kiran"],
}

# Mark attendance
attendance["2025-07-17"] = ["Arun", "Kiran"]

# All dates
print("Dates:", list(attendance.keys()))

# Attendance count for student
student = "Kiran"
count = sum(student in names for names in attendance.values())
print(f"{student} attended {count} day(s)")
