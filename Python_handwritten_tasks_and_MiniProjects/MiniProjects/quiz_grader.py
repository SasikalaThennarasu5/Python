    # 20. Quiz Grader App
    # Scenario: Auto-grade a multiple-choice quiz with displayed questions

    # List of questions, options, and correct answers
    # 20. Quiz Grader App (with new questions)

questions = [
    {
        "question": "1. Who wrote the national anthem of India?",
        "options": ["A. Bankim Chandra", "B. Rabindranath Tagore", "C. Subhash Chandra Bose", "D. Sarojini Naidu"],
        "answer": "B"
    },
    {
        "question": "2. What is the smallest prime number?",
        "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
        "answer": "C"
    },
    {
        "question": "3. Which organ purifies our blood?",
        "options": ["A. Heart", "B. Lungs", "C. Kidney", "D. Liver"],
        "answer": "C"
    },
    {
        "question": "4. Which gas do plants absorb from the atmosphere?",
        "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
        "answer": "C"
    },
    {
        "question": "5. Who invented the light bulb?",
        "options": ["A. Newton", "B. Einstein", "C. Thomas Edison", "D. Galileo"],
        "answer": "C"
    }
]

user_answers = []
score = 0

# Ask questions
for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)

    ans = input("Your answer (A/B/C/D): ").strip().upper()
    if ans not in ['A', 'B', 'C', 'D']:
        print("❌ Invalid choice! Exiting quiz.")
        exit()
    user_answers.append(ans)

# Check answers
for i in range(len(questions)):
    if user_answers[i] == questions[i]["answer"]:
        score += 1

# Grade assignment
if score == 5:
    grade = "A+"
elif score == 4:
    grade = "A"
elif score == 3:
    grade = "B"
elif score == 2:
    grade = "C"
else:
    grade = "F"

# Show results
print("\n------ Quiz Results ------")
for i in range(len(questions)):
    print(f"Q{i+1}: Your Answer: {user_answers[i]} | Correct: {questions[i]['answer']}")
print(f"\n✅ Score : {score} / 5")
print(f"🎓 Grade : {grade}")
print("--------------------------")
