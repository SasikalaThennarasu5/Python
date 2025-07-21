# calendar_view.py
def show_all_dates(events):
    return {e['date'] for e in events}

def list_events_by_date(events, date):
    return [e for e in events if e['date'] == date]
