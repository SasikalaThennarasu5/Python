questions = [
    ("Capital of France?", "paris"),
    ("5 + 7 = ?", "12"),
    ("Water freezes at ? degrees Celsius", "0")
]

def start_quiz():
    score = 0
    for q, a in questions:
        ans = input(q + " ").strip().lower()
        if ans == a:
            print("Correct!")
            score += 1
        else:
            print("Wrong.")
    print(f"Final Score: {score}/{len(questions)} => {(score/len(questions))*100:.2f}%")

if __name__ == "__main__":
    start_quiz()