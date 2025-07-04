#  12. Driving License Eligibility System
age = int(input("Enter your age: "))
has_aadhar = input("Do you have Aadhar? (yes/no): ").lower()
if age >= 18:
    if has_aadhar == "yes":
        print("Eligible for license")
    else:
        print("Aadhar required for license")
else:
    print("Not eligible for license")