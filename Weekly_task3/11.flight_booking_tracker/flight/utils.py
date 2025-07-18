# Common utility functions (if needed)

def format_booking(passenger_id, booking_info):
    return (f"Passenger ID: {passenger_id}\n"
            f"Name       : {booking_info['name']}\n"
            f"Destination: {booking_info['destination']}\n"
            f"Flight No  : {booking_info['flight_no']}")
