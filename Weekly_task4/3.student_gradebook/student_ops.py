
students = []

def add_student(roll_no, name):
    students.append({"info": (roll_no, name), "grades": {}})

def update_grades(roll_no, subject, grade):
    for s in students:
        if s["info"][0] == roll_no:
            s["grades"][subject] = grade
            return
    print("Student not found")

def get_all_subjects():
    subjects = set()
    for s in students:
        subjects.update(s["grades"].keys())
    return subjects

def calculate_averages():
    for s in students:
        grades = s["grades"].values()
        avg = sum(grades) / len(grades) if grades else 0
        s["average"] = avg

def find_top_students():
    calculate_averages()
    max_avg = max(s.get("average", 0) for s in students)
    return [s for s in students if s.get("average", 0) == max_avg]
