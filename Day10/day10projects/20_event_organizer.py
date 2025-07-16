# 20. Event Organizer

events = {
    "Coding Contest": {"participants": ["Ravi"], "max": 3}
}

# Register participant
if len(events["Coding Contest"]["participants"]) < events["Coding Contest"]["max"]:
    events["Coding Contest"]["participants"].append("Meena")

# Cancel registration
events["Coding Contest"]["participants"].remove("Ravi")

# Count
for event, data in events.items():
    print(f"{event} has {len(data['participants'])} participant(s)")
