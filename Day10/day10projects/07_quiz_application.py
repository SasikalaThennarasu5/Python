quiz = {
    "Capital of India?": {"options": ["Delhi", "Mumbai", "Chennai"], "answer": "Delhi"},
    "2+2=?": {"options": ["3", "4", "5"], "answer": "4"}
}

score = 0
for q, data in quiz.items():
    print(q)
    print("Options:", data["options"])
    ans = data["answer"]  # Simulated correct answer
    if ans == data["answer"]:
        score += 1

print(f"Score: {score}/{len(quiz)}")