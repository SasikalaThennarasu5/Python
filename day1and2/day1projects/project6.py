# 6. Student Gradebook
student_name = input("Enter student name: ")
score1 = float(input("Enter score 1: "))
score2 = float(input("Enter score 2: "))
score3 = float(input("Enter score 3: "))
scores = [score1, score2, score3]
average = sum(scores) / 3
student_record = {"Name": student_name, "Scores": scores}
print(f"\n📘 {student_record['Name']}'s Average Score: {average}")
print("Type of average:", type(average))
