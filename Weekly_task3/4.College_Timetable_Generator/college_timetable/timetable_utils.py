# timetable_utils.py

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
PERIODS = ["Period 1", "Period 2", "Period 3", "Period 4", "Period 5"]
SUBJECTS = ["Math", "Physics", "Chemistry", "Biology", "English", "CS"]

# Timetable dictionary to store (day, period): subject
timetable = {}

def generate_timetable():
    import random

    for day in DAYS:
        used_subjects = set()
        for period in PERIODS:
            available_subjects = list(set(SUBJECTS) - used_subjects)
            if not available_subjects:
                used_subjects = set()
                available_subjects = SUBJECTS.copy()

            subject = random.choice(available_subjects)
            used_subjects.add(subject)

            # Using tuple (day, period) as key
            timetable[(day, period)] = subject

def display_timetable():
    print("\nCollege Timetable:\n")
    for day in DAYS:
        print(f"{day}:")
        for period in PERIODS:
            print(f"  {period}: {timetable[(day, period)]}")
        print("-" * 30)