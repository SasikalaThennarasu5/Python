# Voting Eligibility Checker
def check_age(age):
    return "Eligible" if age >= 18 else "Not Eligible"

eligible = lambda age: age >= 18

age = int(input("Enter your age: "))
print("Result:", check_age(age), "| Lambda check:", eligible(age))
