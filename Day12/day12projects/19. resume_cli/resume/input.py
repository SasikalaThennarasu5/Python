import json
import os

DATA_FILE = "resume_data.json"

def collect_input():
    resume_data = {
        "name": input("Name: "),
        "email": input("Email: "),
        "phone": input("Phone: "),
        "summary": input("Professional Summary: "),
        "experience": input("Experience (comma-separated jobs): ").split(","),
        "education": input("Education: "),
        "skills": input("Skills (comma-separated): ").split(",")
    }
    with open(DATA_FILE, "w") as f:
        json.dump(resume_data, f, indent=2)
    return resume_data

def load_input():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            return json.load(f)
    else:
        return None