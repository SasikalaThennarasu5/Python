import json

DATA_FILE = "subjects.json"

def generate_subject_report():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            print("Subject Assignments:")
            for r in data:
                print(f"Student ID: {r['student_id']} | Subject: {r['subject']}")
    except FileNotFoundError:
        print("No subject assignment data found.")
