# Project 13: Employee Bonus Report Generator
print("\nProject 13: Employee Bonus Report Generator")
employees = [("John", 95), ("Priya", 82), ("Sam", 60)]
for name, score in employees:
    if score >= 90:
        bonus = 10000
        grade = "Excellent"
    elif score >= 75:
        bonus = 5000
        grade = "Good"
    else:
        bonus = 2000
        grade = "Average"
    print(f"{name} ({grade}): ₹{bonus}")
