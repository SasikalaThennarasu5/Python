import json

DATA_FILE = "teachers.json"

def generate_teacher_report():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            print("Teacher Report:")
            for t in data:
                print(f"ID: {t['id']} | Name: {t['name']} | Subject: {t['subject']}")
    except FileNotFoundError:
        print("No teacher data found.")
