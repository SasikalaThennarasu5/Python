# traffic_control.py

def add_signal(signal_db, location, time_slot, status, active_signals):
    """Add a traffic signal with a unique (location, time) tuple."""
    signal_key = (location, time_slot)
    signal_db[signal_key] = {
        'status': status
    }
    active_signals.add(status)  # Track active signal states
    print(f"Signal at {location} during {time_slot} set to {status}.")


def update_signal(signal_db, location, time_slot, new_status, active_signals):
    """Update the status of an existing signal."""
    signal_key = (location, time_slot)
    if signal_key in signal_db:
        old_status = signal_db[signal_key]['status']
        signal_db[signal_key]['status'] = new_status
        active_signals.discard(old_status)
        active_signals.add(new_status)
        print(f"Signal at {location} during {time_slot} updated to {new_status}.")
    else:
        print(f"No existing signal found for {location} at {time_slot}.")


def show_signals(signal_db):
    """Display all traffic signals and their status."""
    print("\nTraffic Signals Status:")
    for key, data in signal_db.items():
        print(f"Location: {key[0]}, Time: {key[1]}, Status: {data['status']}")
    print("-" * 40)


def show_active_signals(active_signals):
    """Display unique active signal statuses."""
    print(f"\nActive Signal States: {active_signals}")
    print("-" * 40)
