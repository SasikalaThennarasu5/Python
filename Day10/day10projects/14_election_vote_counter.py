# 14. Election Vote Counter

votes = ["Alice", "Bob", "Alice", "Charlie", "Alice", "Bob"]
candidates = ["Alice", "Bob", "Charlie"]
results = {}

for v in votes:
    if v in candidates:
        results[v] = results.get(v, 0) + 1
    else:
        print("Invalid vote:", v)

# Winner
winner = max(results.items(), key=lambda x: x[1])
print("Winner:", winner[0])
