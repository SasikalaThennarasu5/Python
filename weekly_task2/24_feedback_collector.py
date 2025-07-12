feedback_list = []
sentiments = {"good": 0, "bad": 0, "average": 0}

while True:
    fb = input("Enter feedback (or 'exit'): ")
    if fb.lower() == 'exit': break
    feedback_list.append(fb)
    for key in sentiments:
        if key in fb.lower():
            sentiments[key] += 1

print("\nFeedback Summary:")
for s, c in sentiments.items():
    print(f"{s.capitalize()}: {c}")
