#  16. Age and Income-Based Loan Checker
age = int(input("Enter your age: "))
income = int(input("Enter your monthly income: "))
if age < 21 or income < 20000:
    print("Not eligible for loan")
else:
    print("Loan approved")
