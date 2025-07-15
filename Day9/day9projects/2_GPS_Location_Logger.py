# Project 2: GPS Location Logger
locations = [
    (12.9716, 77.5946),
    (12.2958, 76.6394),
    (11.0168, 76.9558),
    (13.0827, 80.2707),
    (17.3850, 78.4867),
    (19.0760, 72.8777)
]

last_five = locations[-5:]
for lat, lon in last_five:
    print(f"Latitude: {lat}, Longitude: {lon}")