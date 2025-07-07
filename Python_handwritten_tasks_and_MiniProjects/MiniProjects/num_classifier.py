# 7. Even/Odd Number Classifier
# Scenario: Print whether numbers are even or odd

# Input: List of 10 numbers
try:
    input_str = input("Enter 10 numbers separated by spaces: ")
    numbers = list(map(int, input_str.split()))

    if len(numbers) != 10:
        print("\n Please enter exactly 10 numbers.")
    else:
        # Use a for loop + if condition to classify each as even or odd
        print("\n------ Even/Odd Classification ------")
        for num in numbers:
            if num % 2 == 0:
                classification = "Even"
            else:
                classification = "Odd"

            # Use list and print() with message formatting
            print(f"{num:<5} → {classification}")
        print("-------------------------------------")
        
except ValueError:
    print("\n Invalid input! Please enter only integers.")
