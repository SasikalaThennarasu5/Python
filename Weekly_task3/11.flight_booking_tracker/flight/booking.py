# Handles flight bookings

bookings = {}  # Key: (passenger_id,), Value: booking details
destinations = set()  # Unique destination cities

def add_booking(passenger_id, name, destination, flight_no):
    key = (passenger_id,)
    if key in bookings:
        return f"Passenger ID {passenger_id} already has a booking."

    booking_info = {
        'name': name,
        'destination': destination,
        'flight_no': flight_no
    }

    bookings[key] = booking_info
    destinations.add(destination)

    return f"Booking added for {name} to {destination} (Flight: {flight_no})"

def get_booking(passenger_id):
    key = (passenger_id,)
    return bookings.get(key, "No booking found.")

def list_destinations():
    return list(destinations)
