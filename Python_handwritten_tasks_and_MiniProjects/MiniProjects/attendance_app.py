# 8. Attendance Counter
# Scenario: A school wants to track attendance for a week

# Input: Attendance for 7 days (P or A)
# Use list, string, and if-else 
attendance = []
print("Enter attendance for 7 days (P for Present, A for Absent):")

for i in range(1, 8):
    status = input(f"Day {i}: ").strip().upper()
    if status not in ['P', 'A']:
        print(" Invalid input! Please enter 'P' or 'A'.")
        exit()
    attendance.append(status)

# Use for loop to count total presents
total_present = 0
for day in attendance:
    if day == 'P':
        total_present += 1

# Use if to check if total ≥ 5 → Eligible for exam
if total_present >= 5:
    eligibility = " Eligible for Exam"
else:
    eligibility = " Not Eligible for Exam"

print("\n------ Weekly Attendance Report ------")
print(f"Attendance Record : {' '.join(attendance)}")
print(f"Total Presents    : {total_present} out of 7")
print(f"Eligibility Status: {eligibility}")
print("--------------------------------------")
