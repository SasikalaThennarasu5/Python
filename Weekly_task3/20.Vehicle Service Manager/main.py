# main.py

from service_manager import add_vehicle, show_all_services, show_service_types

# Initialize data structures
service_db = {}       # Dictionary: Plate Number Tuple -> Info
service_types_set = set()  # Set: Unique service types

# Add vehicle service records
add_vehicle(service_db, "AB123CD", "John Doe", "Oil Change", service_types_set)
add_vehicle(service_db, "XY789GH", "Jane Smith", "Tire Rotation", service_types_set)
add_vehicle(service_db, "LM456OP", "Alice Brown", "Brake Inspection", service_types_set)
add_vehicle(service_db, "AB123CD", "John Doe", "Oil Change", service_types_set)  # Same service, duplicate in dict

# Display records and service types
show_all_services(service_db)
show_service_types(service_types_set)
