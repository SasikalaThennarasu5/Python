# 11. Voting Eligibility Checker
# Scenario: A system to check who can vote

try:
    # Input: Name and age
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Use if to check if age ≥ 18 → Eligible
    if age >= 18:
        status = " Eligible to Vote"
    else:
        # Use else to say "Not eligible"
        status = " Not Eligible to Vote"

    # Print formatted message
    print("\n------ Voting Eligibility ------")
    print(f"Name       : {name}")
    print(f"Age        : {age}")
    print(f"Status     : {status}")
    print("--------------------------------")

except ValueError:
    print("\n Invalid input! Please enter a valid numeric age.")
