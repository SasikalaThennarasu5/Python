# 19. City Distance Map

distances = {
    "Chennai": {"Bangalore": 350, "Delhi": 2200},
    "Bangalore": {"Chennai": 350, "Delhi": 2100},
}

# Query distance
print("Distance:", distances["Chennai"].get("Delhi", "Not Found"))

# Update distance
distances["Chennai"]["Mumbai"] = 1300

# Shortest from Chennai
shortest = min(distances["Chennai"].items(), key=lambda x: x[1])
print("Shortest from Chennai:", shortest)
