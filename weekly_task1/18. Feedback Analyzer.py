# Project 18: Feedback Analyzer
print("\\nProject 18: Feedback Analyzer")
feedbacks = ["Service is good", "Need improvement", "good ambiance", "average"]
for msg in feedbacks:
    if "good" in msg.lower():
        print(f"'{msg}' → Positive")
    else:
        print(f"'{msg}' → Neutral")
