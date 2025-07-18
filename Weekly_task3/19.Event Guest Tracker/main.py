# main.py

from guest_utils import add_guest, show_event_guests, show_unique_guests

# Initialize data structures
event_db = {}  # Dictionary: Event ID -> {Guest Name -> RSVP}
guest_set = set()  # Prevent guest duplicates

# Add guests to events
add_guest(event_db, 901, "Alice", "Yes", guest_set)
add_guest(event_db, 901, "Bob", "No", guest_set)
add_guest(event_db, 902, "Charlie", "Yes", guest_set)
add_guest(event_db, 902, "Alice", "Yes", guest_set)  # Should warn: Alice is already registered
add_guest(event_db, 903, "David", "Maybe", guest_set)

# Display guests and RSVP status
show_event_guests(event_db)
show_unique_guests(guest_set)
