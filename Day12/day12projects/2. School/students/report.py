import json

DATA_FILE = "students.json"

def generate_student_report():
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
            print("Student Report:")
            for s in data:
                print(f"ID: {s['id']} | Name: {s['name']} | Age: {s['age']}")
    except FileNotFoundError:
        print("No student data found.")
