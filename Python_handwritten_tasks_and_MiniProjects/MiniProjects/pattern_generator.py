# 12. Number Pattern Generator
# Scenario: Generate a triangle pattern using a loop

try:
    # Input: Number of rows
    rows = int(input("Enter the number of rows: "))

    print("\n------ Number Pattern ------")

    # Use nested for loop to print the pattern
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(j, end=' ')
        print()  # Move to next line after each row

    print("----------------------------")

except ValueError:
    print("\n Invalid input! Please enter an integer.")
