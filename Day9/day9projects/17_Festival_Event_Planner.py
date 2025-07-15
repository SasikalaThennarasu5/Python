# Project 17: Festival Event Planner
events = [
    ("Dance", ("10:00", "11:00", "Hall A")),
    ("Music", ("11:30", "12:30", "Hall B"))
]

for name, (start, end, loc) in events:
    print(f"{name}: {start} - {end} at {loc}")