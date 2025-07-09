# Project 19: Quiz with Exit Option
questions = ["Capital of India?", "2+2?", "Color of sky?"]
i = 0
while i < len(questions):
    ans = input(questions[i] + " (or 'quit'): ")
    if ans.lower() == "quit":
        break
    i += 1
else:
    print("Quiz complete")
