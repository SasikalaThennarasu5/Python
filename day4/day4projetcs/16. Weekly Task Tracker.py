# Project 16: Weekly Task Tracker
print("\nProject 16: Weekly Task Tracker")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
tasks = ["Read", "Write", "Code", "Review", "Submit", "Rest", "Play"]
for day, task in zip(days, tasks):
    print(f"{day}: {task}")
