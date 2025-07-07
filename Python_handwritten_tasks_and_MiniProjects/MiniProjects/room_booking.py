# 16. Room Booking Price Calculator
# Scenario: Hotel room booking system with discount logic

try:
    # Input: Room type and nights stayed
    room_type = input("Enter room type (Standard/Deluxe): ").strip().lower()
    nights = int(input("Enter number of nights stayed: "))

    # Use if-else for pricing
    if room_type == "standard":
        rate_per_night = 1000
    elif room_type == "deluxe":
        rate_per_night = 1500
    else:
        print("\n Invalid room type. Please enter 'Standard' or 'Deluxe'.")
        exit()

    # Calculate total price
    total_price = rate_per_night * nights

    # If nights > 3 → 20% discount
    if nights > 3:
        discount = 0.20 * total_price
    else:
        discount = 0

    final_price = total_price - discount

    print("\n------ Booking Summary ------")
    print(f"Room Type        : {room_type.title()}")
    print(f"Nights Stayed    : {nights}")
    print(f"Rate per Night   : ₹{rate_per_night}")
    print(f"Total Price      : ₹{total_price:.2f}")
    print(f"Discount Applied : ₹{discount:.2f}")
    print(f"Final Price      : ₹{final_price:.2f}")
    print("-----------------------------")

except ValueError:
    print("\n Invalid input! Please enter valid data.")
