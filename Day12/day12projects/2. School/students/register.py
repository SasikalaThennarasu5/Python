import json
import os

DATA_FILE = "students.json"

def register_student(name, age, student_id):
    student = {
        "id": student_id,
        "name": name,
        "age": age
    }

    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data.append(student)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Student {name} registered.")
