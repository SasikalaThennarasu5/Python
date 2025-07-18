# bus_ops.py

def reserve_seat(seat_db, occupied_seats, user_id, seat_number):
    """Reserve a seat for a user using tuple ID and prevent duplicate reservations."""
    if seat_number in occupied_seats:
        print(f"Seat {seat_number} is already reserved.")
        return False

    user_key = (user_id,)  # Tuple for user ID
    seat_db[user_key] = {
        'seat_number': seat_number
    }
    occupied_seats.add(seat_number)
    print(f"User {user_id} successfully reserved seat {seat_number}.")
    return True


def show_reservations(seat_db):
    """Display all seat reservations."""
    print("\nBus Seat Reservations:")
    for user_key, data in seat_db.items():
        print(f"User ID: {user_key[0]}, Seat Number: {data['seat_number']}")
    print("-" * 40)


def show_occupied_seats(occupied_seats):
    """Display all occupied seats."""
    print(f"\nOccupied Seats: {occupied_seats}")
    print("-" * 40)
