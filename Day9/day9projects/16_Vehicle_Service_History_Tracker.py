# Project 16: Vehicle Service History Tracker
history = [
    ("KA01AB1234", ("2023-01-01", "2024-01-01")),
    ("TN09CD5678", ("2022-06-15", "2023-06-15"))
]

for vehicle, dates in history:
    print(f"{vehicle} serviced on: {', '.join(dates)}")