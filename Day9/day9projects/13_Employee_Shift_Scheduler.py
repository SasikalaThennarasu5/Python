# Project 13: Employee Shift Scheduler
shifts = [
    (1, "Alice", ("09:00", "17:00")),
    (2, "Bob", ("10:00", "18:00")),
    (3, "Charlie", ("08:00", "16:00"))
]

for eid, name, (start, end) in shifts:
    print(f"{name} works from {start} to {end}")