# 2. Age Category Classifier
# Scenario: Classify people into categories based on age

# Input: Name and age
name = input("Enter your name: ")

# Use variables and data type validation
try:
    age = int(input("Enter your age: "))

    # Use if-elif-else to classify age
    # <13 → Child, 13–19 → Teen, 20–59 → Adult, ≥60 → Senior
    if age < 13:
        category = "Child"
    elif age <= 19:
        category = "Teen"
    elif age <= 59:
        category = "Adult"
    else:
        category = "Senior"

    # Display a proper message with classification
    print("\n------ Age Classification ------")
    print(f"Name       : {name}")
    print(f"Age        : {age}")
    print(f"Category   : {category}")
    print("--------------------------------")

except ValueError:
    print("Invalid input! Age must be a number.")
