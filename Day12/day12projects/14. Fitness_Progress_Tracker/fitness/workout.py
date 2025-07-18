import json
from datetime import datetime

WORKOUT_FILE = "data/workouts.json"

def log_workout(workout_type, duration_min, calories_burned):
    workout = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "type": workout_type,
        "duration": duration_min,
        "calories": calories_burned
    }

    try:
        with open(WORKOUT_FILE, "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    data.append(workout)

    with open(WORKOUT_FILE, "w") as file:
        json.dump(data, file, indent=4)

    print("✅ Workout logged successfully.")
