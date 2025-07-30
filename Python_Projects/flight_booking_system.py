
import json
import random
from functools import wraps

def confirm_booking(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Confirming booking...")
        return func(*args, **kwargs)
    return wrapper

class Passenger:
    def __init__(self, name):
        self.name = name

class Flight:
    def __init__(self, destination, seats):
        self.destination = destination
        self.total_seats = seats
        self.booked_seats = set()
        self.passengers = {}

    def is_seat_available(self, seat):
        return seat not in self.booked_seats

    @confirm_booking
    def book_seat(self, passenger_name, seat):
        if self.is_seat_available(seat):
            self.booked_seats.add(seat)
            self.passengers[seat] = Passenger(passenger_name)
            print(f"Seat {seat} booked for {passenger_name}.")
        else:
            raise Exception("Seat already booked.")

    def cancel_booking(self, seat):
        if seat in self.booked_seats:
            passenger = self.passengers.pop(seat).name
            self.booked_seats.remove(seat)
            print(f"Booking for seat {seat} ({passenger}) canceled.")
        else:
            raise Exception("Seat not booked.")

    def display_status(self):
        print(f"Flight to {self.destination}")
        print("Available seats:", [seat for seat in self.total_seats if seat not in self.booked_seats])

    def get_available_seats(self):
        for seat in self.total_seats:
            if seat not in self.booked_seats:
                yield seat

    def save_bookings(self, filename='bookings.json'):
        with open(filename, 'w') as f:
            data = {
                "destination": self.destination,
                "bookings": {seat: self.passengers[seat].name for seat in self.passengers}
            }
            json.dump(data, f)

# Sample usage
if __name__ == "__main__":
    available_seats = [f"{row}{col}" for row in "ABC" for col in range(1, 6)]
    flight = Flight("Paris", available_seats)

    while True:
        print("\n1. Book Seat\n2. Cancel Booking\n3. Display Flight Status\n4. Save & Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            name = input("Enter passenger name: ")
            seat = input("Enter seat number (e.g., A1): ")
            try:
                flight.book_seat(name, seat)
            except Exception as e:
                print("Error:", e)

        elif choice == '2':
            seat = input("Enter seat number to cancel: ")
            try:
                flight.cancel_booking(seat)
            except Exception as e:
                print("Error:", e)

        elif choice == '3':
            flight.display_status()

        elif choice == '4':
            flight.save_bookings()
            print("Bookings saved. Goodbye!")
            break

        else:
            print("Invalid choice.")
