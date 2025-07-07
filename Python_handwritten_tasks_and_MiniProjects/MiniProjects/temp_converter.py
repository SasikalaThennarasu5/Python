# 5. Temperature Converter & Category
# Scenario: Convert temperature and categorize it

# Input: Temperature in Celsius
try:
    celsius = float(input("Enter temperature in Celsius: "))

    # Convert to Fahrenheit
    fahrenheit = (celsius * 9/5) + 32

    # Use if: <20 → Cold, 20–30 → Warm, >30 → Hot
    if celsius < 20:
        condition = "Cold"
    elif celsius <= 30:
        condition = "Warm"
    else:
        condition = "Hot"

    # Display formatted message with condition
    print("\n------ Temperature Report ------")
    print(f"Celsius     : {celsius:.2f}°C")
    print(f"Fahrenheit  : {fahrenheit:.2f}°F")
    print(f"Condition   : {condition}")
    print("--------------------------------")

except ValueError:
    print("Invalid input! Please enter a numeric temperature.")
