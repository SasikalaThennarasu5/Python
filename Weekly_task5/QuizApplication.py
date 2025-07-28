# Quiz Application

import json
import random
import time

class Question:
    def __init__(self, text, options, answer, q_type="mcq", difficulty="medium"):
        self.text = text
        self.options = options
        self.answer = answer
        self.q_type = q_type
        self.difficulty = difficulty

    def to_dict(self):
        return {
            "text": self.text,
            "options": self.options,
            "answer": self.answer,
            "q_type": self.q_type,
            "difficulty": self.difficulty
        }

    @staticmethod
    def from_dict(data):
        return Question(
            data["text"],
            data["options"],
            data["answer"],
            data["q_type"],
            data["difficulty"]
        )

class QuizApp:
    def __init__(self, bank_file="questions.json"):
        self.questions = []
        self.score = 0
        self.bank_file = bank_file
        self.load_questions()

    def add_question(self, question):
        self.questions.append(question)

    def save_questions(self):
        with open(self.bank_file, 'w') as f:
            json.dump([q.to_dict() for q in self.questions], f, indent=4)

    def load_questions(self):
        try:
            with open(self.bank_file, 'r') as f:
                data = json.load(f)
                self.questions = [Question.from_dict(q) for q in data]
        except FileNotFoundError:
            self.questions = []

    def start_quiz(self, difficulty="medium", timed=False):
        filtered = [q for q in self.questions if q.difficulty == difficulty]
        if not filtered:
            print("No questions available at this difficulty.")
            return
        self.score = 0
        random.shuffle(filtered)
        for q in filtered:
            print(f"\nQ: {q.text}")
            if q.q_type == "mcq":
                for i, opt in enumerate(q.options):
                    print(f"{i+1}. {opt}")
                if timed:
                    start = time.time()
                try:
                    ans = int(input("Your answer (number): "))
                except:
                    ans = -1
                if timed and time.time() - start > 10:
                    print("⏰ Time's up!")
                    continue
                if q.options[ans-1] == q.answer:
                    self.score += 1
                    print("✅ Correct!")
                else:
                    print(f"❌ Wrong. Correct answer: {q.answer}")
            elif q.q_type == "tf":
                ans = input("True or False? ").lower()
                if ans in q.answer.lower():
                    self.score += 1
                    print("✅ Correct!")
                else:
                    print(f"❌ Wrong. Correct answer: {q.answer}")
        print(f"\nFinal Score: {self.score}/{len(filtered)}")

# CLI for demo
if __name__ == "__main__":
    app = QuizApp()

    while True:
        print("\n--- Quiz Application ---")
        print("1. Add Question\n2. Start Quiz\n3. Save Question Bank\n4. Load Question Bank\n5. Exit")
        choice = input("Choose: ")

        if choice == '1':
            text = input("Question text: ")
            q_type = input("Type (mcq/tf): ").lower()
            difficulty = input("Difficulty (easy/medium/hard): ").lower()
            if q_type == "mcq":
                options = [input("Option 1: "), input("Option 2: "), input("Option 3: "), input("Option 4: ")]
                answer = input("Correct option text: ")
            else:
                options = ["True", "False"]
                answer = input("Correct answer (True/False): ")
            q = Question(text, options, answer, q_type, difficulty)
            app.add_question(q)
            print("Question added.")
        elif choice == '2':
            diff = input("Choose difficulty (easy/medium/hard): ").lower()
            timed = input("Enable timer? (y/n): ").lower() == 'y'
            app.start_quiz(difficulty=diff, timed=timed)
        elif choice == '3':
            app.save_questions()
            print("Questions saved.")
        elif choice == '4':
            app.load_questions()
            print("Questions loaded.")
        elif choice == '5':
            break
