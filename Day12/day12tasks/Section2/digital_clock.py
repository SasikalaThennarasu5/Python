import time
from datetime import datetime

print("Press Ctrl+C to stop")
try:
    while True:
        now = datetime.now()
        print(now.strftime("%H:%M:%S"), end="\r")
        time.sleep(1)
except KeyboardInterrupt:
    print("\nClock stopped.")
