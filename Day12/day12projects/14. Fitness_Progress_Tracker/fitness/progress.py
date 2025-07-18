import json
import math
from datetime import datetime

PROGRESS_FILE = "data/progress.json"

def log_progress(weight_kg, goal_kg):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "weight": weight_kg,
        "goal": goal_kg,
        "difference": round(weight_kg - goal_kg, 2)
    }

    try:
        with open(PROGRESS_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(PROGRESS_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Progress updated.")

def view_latest_progress():
    try:
        with open(PROGRESS_FILE, "r") as file:
            data = json.load(file)
            latest = data[-1]
            print(f"📅 Date: {latest['date']}")
            print(f"⚖️  Current: {latest['weight']} kg | Goal: {latest['goal']} kg")
            print(f"📉 Difference: {latest['difference']} kg")
    except (FileNotFoundError, IndexError):
        print("⚠️ No progress data found.")
