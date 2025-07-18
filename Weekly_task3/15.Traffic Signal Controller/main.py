# main.py

from traffic_control import add_signal, update_signal, show_signals, show_active_signals

# Initialize database for traffic signals
signal_db = {}
active_signals = set()

# Add signals
add_signal(signal_db, "Crossroad A", "Morning", "Green", active_signals)
add_signal(signal_db, "Crossroad B", "Evening", "Red", active_signals)

# Update a signal
update_signal(signal_db, "Crossroad A", "Morning", "Yellow", active_signals)

# Display signals and active states
show_signals(signal_db)
show_active_signals(active_signals)
