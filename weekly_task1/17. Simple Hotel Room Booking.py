# Project 17: Simple Hotel Room Booking
print("\\nProject 17: Simple Hotel Room Booking")
rooms = {"AC": 1500, "Non-AC": 800}
room_type = "AC"
nights = 4
total = rooms[room_type] * nights
if nights > 3:
    total *= 0.9
print(f"Total room price: ₹{total}")