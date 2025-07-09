# Project 16: Feedback Collector
while True:
    feedback = input("Enter feedback (or 'exit'): ")
    if feedback == "exit":
        break
    if len(feedback) < 3:
        continue
    print("Feedback saved.")
