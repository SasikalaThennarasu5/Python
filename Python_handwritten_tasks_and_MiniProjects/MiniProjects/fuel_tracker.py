# 17. Fuel Consumption Tracker
# Scenario: Monitor fuel usage and alert user

try:
    # Input: Daily fuel consumption (list of 7)
    print("Enter daily fuel consumption for 7 days (in liters):")
    fuel_data = []

    for i in range(1, 8):
        value = float(input(f"Day {i}: "))
        fuel_data.append(value)

    # Use for loop to sum total
    total_fuel = 0
    for amount in fuel_data:
        total_fuel += amount

    # Use if to print alert if total > 50 liters
    print("\n------ Weekly Fuel Report ------")
    print(f"Daily Usage (L)   : {fuel_data}")
    print(f"Total Fuel Used   : {total_fuel:.2f} liters")

    if total_fuel > 50:
        print(" Alert: Fuel usage exceeded 50 liters!")
    else:
        print(" Fuel usage is within the safe limit.")
    print("---------------------------------------")

except ValueError:
    print("\n Invalid input! Please enter numeric values only.")
