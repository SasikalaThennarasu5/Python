# Project 1: Student Roll Call System
students = []
i = 0
while i < 10:
    name = input(f"Enter student {i+1} name: ").strip()
    if name == "":
        continue
    students.append(name)
    i += 1
else:
    print("Attendance completed!")
print("Students:", students)
