class NoSeatsAvailableError(Exception): pass

def book_flight(seats, requested):
    try:
        if requested > seats:
            raise NoSeatsAvailableError("No seats left")
        print("Flight booked")
    except Exception as e:
        print(e)
    finally:
        print("Booking attempt logged")