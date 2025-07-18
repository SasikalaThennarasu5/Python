import json
import os

DATA_FILE = "teachers.json"

def register_teacher(name, subject, teacher_id):
    teacher = {
        "id": teacher_id,
        "name": name,
        "subject": subject
    }

    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data.append(teacher)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Teacher {name} registered.")
