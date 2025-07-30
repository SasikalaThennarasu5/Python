import datetime
import time
from playsound import playsound
from functools import wraps

def snooze(delay=300):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"Snoozing for {delay // 60} minutes...")
            time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@snooze(delay=10)  # 10 seconds for demo
def ring_alarm():
    print("Wake up! Playing alarm sound...")
    playsound('alarm.mp3')

def set_alarm(alarm_time):
    try:
        alarm_dt = datetime.datetime.strptime(alarm_time, "%H:%M").time()
    except ValueError:
        print("Invalid time format. Use HH:MM.")
        return
    print(f"Alarm set for {alarm_dt.strftime('%H:%M')}")
    while True:
        now = datetime.datetime.now().time()
        if now.hour == alarm_dt.hour and now.minute == alarm_dt.minute:
            ring_alarm()
            break
        time.sleep(10)

# Example usage
if __name__ == "__main__":
    set_alarm("07:30")  # Set your desired alarm time
