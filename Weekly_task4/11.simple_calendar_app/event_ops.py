# event_ops.py
def add_event(events, event):
    events.append(event)

def delete_event(events, event_id):
    return [e for e in events if e['id'] != event_id]

def update_event(events, event_id, new_event):
    return [new_event if e['id'] == event_id else e for e in events]
