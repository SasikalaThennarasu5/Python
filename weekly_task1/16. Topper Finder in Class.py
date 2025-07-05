# Project 16: Topper Finder in Class
print("\\nProject 16: Topper Finder in Class")
students = {"Ravi": 87, "Meena": 92, "Kiran": 78}
topper = max(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks")