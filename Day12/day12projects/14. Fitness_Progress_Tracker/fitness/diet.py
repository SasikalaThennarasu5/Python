import json
from datetime import datetime

DIET_FILE = "data/diet.json"

def log_meal(meal, calories_intake):
    entry = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "meal": meal,
        "calories": calories_intake
    }

    try:
        with open(DIET_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(entry)

    with open(DIET_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Meal logged successfully.")
