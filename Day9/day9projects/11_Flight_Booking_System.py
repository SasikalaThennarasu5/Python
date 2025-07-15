# Project 11: Flight Booking System
flights = [
    (201, "NYC", "LAX", ("Alice", "Bob")),
    (202, "DEL", "BOM", ("Charlie", "David", "Eva"))
]

for fid, src, dest, passengers in flights:
    print(f"Flight {fid} from {src} to {dest} has {len(passengers)} passengers.")