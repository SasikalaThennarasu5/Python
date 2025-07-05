# Project 12: Marks to Grade Converter
print("\\nProject 12: Marks to Grade Converter")
marks = [95, 82, 67, 49, 76]
for m in marks:
    if m >= 90:
        grade = "A"
    elif m >= 75:
        grade = "B"
    elif m >= 60:
        grade = "C"
    else:
        grade = "D"
    print(f"Marks: {m}, Grade: {grade}")