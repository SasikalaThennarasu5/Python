# 12. Simple Quiz
q1 = input("What is the capital of France? ")
q2 = input("What is 5 + 5? ")
q3 = input("What is the color of the sky? ")
answers = [q1, q2, q3]
print("\n🧠 Your Answers and Types:")
for ans in answers:
    print(ans, "->", type(ans))
