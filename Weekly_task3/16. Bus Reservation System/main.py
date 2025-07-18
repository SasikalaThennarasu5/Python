# main.py

from bus_ops import reserve_seat, show_reservations, show_occupied_seats

# Initialize data structures
seat_db = {}
occupied_seats = set()

# Reserve seats
reserve_seat(seat_db, occupied_seats, 601, "A1")
reserve_seat(seat_db, occupied_seats, 602, "A2")
reserve_seat(seat_db, occupied_seats, 601, "A3")  # Same user, new seat (allowed here)
reserve_seat(seat_db, occupied_seats, 603, "A1")  # Duplicate seat

# Display current reservations and occupied seats
show_reservations(seat_db)
show_occupied_seats(occupied_seats)
