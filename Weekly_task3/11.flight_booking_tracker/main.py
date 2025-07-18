from flight import add_booking, get_booking, list_destinations, process_payment
from flight.utils import format_booking

def main():
    print(add_booking(101, "Alice", "Paris", "AF123"))
    print(process_payment(101, 45000))

    print(add_booking(102, "Bob", "Tokyo", "JL456"))
    print(process_payment(102, 62000))

    print(add_booking(101, "Alice", "London", "BA789"))  # Duplicate ID

    print("\n--- All Destinations ---")
    print(list_destinations())

    print("\n--- Booking Details ---")
    for pid in [101, 102, 999]:
        booking = get_booking(pid)
        if isinstance(booking, dict):
            print(format_booking(pid, booking))
        else:
            print(f"{pid}: {booking}")

if __name__ == "__main__":
    main()
