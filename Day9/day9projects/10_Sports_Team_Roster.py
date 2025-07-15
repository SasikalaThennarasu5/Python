# Project 10: Sports Team Roster
players = [
    (1, "Alice", ("Striker", 12)),
    (2, "Bob", ("Defender", 5)),
    (3, "Charlie", ("Striker", 15))
]

strikers = sum(1 for _, _, (pos, _) in players if pos == "Striker")
print("Strikers count:", strikers)

for pid, name, (pos, goals) in players:
    if goals > 10:
        print(f"{name} ({pos}) - Goals: {goals}")