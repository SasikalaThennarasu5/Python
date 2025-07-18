# parcel.py

def add_parcel(parcel_db, tracking_id, status, city, visited_cities):
    """Add or update a parcel's status and track visited cities."""
    parcel_key = (tracking_id,)  # Tuple for tracking ID
    parcel_db[parcel_key] = {
        'status': status,
        'current_city': city
    }
    visited_cities.add(city)
    print(f"Parcel {tracking_id} updated: Status '{status}' at {city}.")


def show_parcels(parcel_db):
    """Display all parcel tracking information."""
    print("\nParcel Tracking Info:")
    for parcel_key, data in parcel_db.items():
        print(f"Tracking ID: {parcel_key[0]}, Status: {data['status']}, Current City: {data['current_city']}")
    print("-" * 40)


def show_visited_cities(visited_cities):
    """Display unique cities where parcels have been."""
    print(f"\nVisited Cities: {visited_cities}")
    print("-" * 40)
