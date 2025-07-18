# service_manager.py

def add_vehicle(service_db, plate_number, owner_name, service_type, service_types_set):
    """Add vehicle service record using tuple for plate number."""
    vehicle_key = (plate_number,)  # Tuple for immutability
    service_types_set.add(service_type)  # Ensure no duplicate service types
    
    service_db[vehicle_key] = {
        'owner': owner_name,
        'service_type': service_type
    }
    print(f"Vehicle {plate_number} (Owner: {owner_name}) added for '{service_type}' service.")


def show_all_services(service_db):
    """Display all vehicle service records."""
    print("\nVehicle Service Records:")
    for vehicle_key, info in service_db.items():
        print(f"Plate: {vehicle_key[0]}, Owner: {info['owner']}, Service: {info['service_type']}")
    print("-" * 40)


def show_service_types(service_types_set):
    """Display all unique service types."""
    print(f"\nService Types Offered: {service_types_set}")
    print("-" * 40)
