# Project 18: Voting Eligibility Checker
i = 0
eligible = 0
while i < 5:
    age = int(input(f"Enter age of person {i+1}: "))
    if age >= 18:
        eligible += 1
    i += 1
    pass
print(f"Eligible voters: {eligible}")
