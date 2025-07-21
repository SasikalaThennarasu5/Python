from event_ops import add_event, delete_event, update_event
from calendar_view import show_all_dates, list_events_by_date

events = []
event_id = 1

e1 = {'id': ('E001',), 'date': '2025-07-21', 'time': '10:00', 'desc': 'Meeting', 'participants': {'Alice', 'Bob'}}
add_event(events, e1)

print("All Dates with Events:", show_all_dates(events))
print("Events on 2025-07-21:", list_events_by_date(events, '2025-07-21'))
