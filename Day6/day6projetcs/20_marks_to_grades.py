# Marks to Grade Converter
def convert_grades(marks):
    return list(map(lambda m: "A" if m >= 90 else "B" if m >= 75 else "C" if m >= 50 else "F", marks))

marks = [95, 67, 88, 45, 76]
print("Grades:", convert_grades(marks))
