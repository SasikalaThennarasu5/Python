class OverBookingError(Exception): pass

def book_room(guests, rooms=5):
    try:
        assert isinstance(guests, int)
        if guests > rooms:
            raise OverBookingError("Too many guests")
        print("Booking confirmed")
    except Exception as e:
        print(e)