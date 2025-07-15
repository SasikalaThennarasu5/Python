# Project 14: Exam Result Processing
results = [
    ("Alice", (90, 85, 92)),
    ("Bob", (75, 80, 78))
]

for name, scores in results:
    print(f"{name}: Total={sum(scores)}, Avg={sum(scores)/len(scores):.2f}")