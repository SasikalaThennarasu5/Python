1. Online Voting Eligibility Checker
name = input("Enter your name: ")
age = int(input("Enter your age: "))
citizenship = input("Enter your citizenship: ")
print(f"Name: {name}, Age: {age} ({type(age)}), Citizenship: {citizenship} ({type(citizenship)})")
if age >= 18 and citizenship.lower() == "indian":
    print(f"{name}, you are eligible to vote.")
else:
    print(f"{name}, you are not eligible to vote.")
