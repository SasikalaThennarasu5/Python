# main.py

from parcel import add_parcel, show_parcels, show_visited_cities

# Initialize data structures
parcel_db = {}
visited_cities = set()

# Track parcels
add_parcel(parcel_db, 701, "In Transit", "New York", visited_cities)
add_parcel(parcel_db, 702, "Delivered", "Los Angeles", visited_cities)
add_parcel(parcel_db, 701, "Out for Delivery", "New York", visited_cities)
add_parcel(parcel_db, 703, "In Transit", "Chicago", visited_cities)
add_parcel(parcel_db, 704, "In Transit", "Chicago", visited_cities)  # City already exists in set

# Display current parcels and visited cities
show_parcels(parcel_db)
show_visited_cities(visited_cities)
