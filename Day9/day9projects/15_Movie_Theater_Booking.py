# Project 15: Movie Theater Booking
seats = (
    ("A1", "A2", "A3"),
    ("B1", "B2", "B3"),
    ("C1", "C2", "C3")
)

for row in seats:
    for seat in row:
        print(f"Seat: {seat}")