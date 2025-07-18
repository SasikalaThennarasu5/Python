# guest_utils.py

def add_guest(event_db, event_id, guest_name, rsvp_status, guest_set):
    """Add guest to an event with RSVP tracking and prevent duplicates."""
    if guest_name in guest_set:
        print(f"Guest '{guest_name}' is already registered for an event.")
        return False

    event_key = (event_id,)  # Tuple for event ID
    if event_key not in event_db:
        event_db[event_key] = {}

    event_db[event_key][guest_name] = rsvp_status
    guest_set.add(guest_name)
    print(f"Added '{guest_name}' to Event {event_id} with RSVP: {rsvp_status}")
    return True


def show_event_guests(event_db):
    """Display all events with their guest lists and RSVP status."""
    print("\nEvent Guest Lists:")
    for event_key, guests in event_db.items():
        print(f"Event ID: {event_key[0]}")
        for guest_name, rsvp in guests.items():
            print(f" - {guest_name}: RSVP {rsvp}")
        print("-" * 40)


def show_unique_guests(guest_set):
    """Display all unique guests."""
    print(f"\nUnique Guests Across Events: {guest_set}")
    print("-" * 40)
