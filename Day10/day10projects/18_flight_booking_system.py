# 18. Flight Booking System

flights = {
    "AI101": {"route": "Delhi-Chennai", "passengers": ["Amit", "Sara"]},
}

# Add passenger
flights.setdefault("AI102", {"route": "Mumbai-Bangalore", "passengers": []})
flights["AI102"]["passengers"].append("Ravi")

# Remove passenger
flights["AI101"]["passengers"].remove("Sara")

# Seat availability
print("Seats in AI101:", len(flights["AI101"]["passengers"]))
