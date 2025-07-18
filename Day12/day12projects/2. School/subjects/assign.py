import json
import os

DATA_FILE = "subjects.json"

def assign_subject(student_id, subject):
    record = {
        "student_id": student_id,
        "subject": subject
    }

    data = []
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            data = json.load(f)

    data.append(record)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Subject '{subject}' assigned to student ID {student_id}.")
