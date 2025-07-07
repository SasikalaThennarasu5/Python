# Topper Finder in a Class
# Scenario: Find student with highest marks

# Dictionary: name → marks
students = {
    "sugan": 87,
    "Dharun": 92,
    "Vishwa": 95,
    "Santoz": 88,
    "Manoj": 90
}

# Use for loop to find max marks and topper name
topper_name = ""
topper_marks = 0

for name, marks in students.items():
    # Use conditional logic inside loop
    if marks > topper_marks:
        topper_marks = marks
        topper_name = name

print("------ Topper Report ------")
print(f"Topper       : {topper_name}")
print(f"Highest Marks: {topper_marks}")
print("----------------------------")
