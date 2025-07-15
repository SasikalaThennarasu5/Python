# Project 12: Daily Temperature Logger
temps = [
    ("2025-07-01", (28, 36)),
    ("2025-07-02", (27, 34)),
    ("2025-07-03", (29, 38))
]

last_7 = temps[-7:]
high_eve = max(last_7, key=lambda x: x[1][1])
print("Hottest evening:", high_eve)