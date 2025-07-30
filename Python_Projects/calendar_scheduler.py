from icalendar import Calendar, Event
from datetime import datetime
import pytz

class EventScheduler:
    def __init__(self):
        self.calendar = Calendar()
        self.events_by_date = {}

    def add_event(self, summary, date_str, start_time, end_time):
        try:
            event = Event()
            tz = pytz.timezone("UTC")
            start_dt = datetime.strptime(f"{date_str} {start_time}", "%Y-%m-%d %H:%M")
            end_dt = datetime.strptime(f"{date_str} {end_time}", "%Y-%m-%d %H:%M")
            event.add("summary", summary)
            event.add("dtstart", tz.localize(start_dt))
            event.add("dtend", tz.localize(end_dt))
            self.calendar.add_component(event)

            if date_str not in self.events_by_date:
                self.events_by_date[date_str] = []
            self.events_by_date[date_str].append(event)
        except Exception as e:
            print(f"Failed to add event: {e}")

    def save_calendar(self, filename):
        with open(filename, "wb") as f:
            f.write(self.calendar.to_ical())

    def yield_daily_events(self, date_str):
        if date_str in self.events_by_date:
            for event in self.events_by_date[date_str]:
                yield event.get("summary")
        else:
            yield "No events scheduled for this date."

if __name__ == "__main__":
    scheduler = EventScheduler()
    scheduler.add_event("Meeting with Team", "2025-08-01", "10:00", "11:00")
    scheduler.add_event("Doctor Appointment", "2025-08-01", "15:00", "15:30")
    scheduler.add_event("Dinner", "2025-08-02", "20:00", "21:00")
    scheduler.save_calendar("calendar_schedule.ics")

    date = input("Enter a date (YYYY-MM-DD) to see events: ")
    for event in scheduler.yield_daily_events(date):
        print("-", event)
