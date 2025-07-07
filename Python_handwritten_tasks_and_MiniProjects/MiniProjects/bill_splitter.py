# 9. Bill Splitter Between Friends
# Scenario: A group of friends want to split a dinner bill

try:
    # Input: Total bill and number of friends
    total_bill = float(input("Enter the total bill amount (₹): "))
    num_friends = int(input("Enter the number of friends: "))

    # Use if to check if friends ≥ 1, else show error
    if num_friends >= 1:
        # Use variables for calculation
        per_head = total_bill / num_friends

        # Print per-head contribution
        print("\n------ Bill Split Summary ------")
        print(f"Total Bill        : ₹{total_bill:.2f}")
        print(f"No. of Friends    : {num_friends}")
        print(f"Per Head Share    : ₹{per_head:.2f}")
        print("--------------------------------")
    else:
        print("\n Error: Number of friends must be at least 1.")

except ValueError:
    print("\n Invalid input! Please enter valid numeric values.")
