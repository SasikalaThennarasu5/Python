import time
import pygame

class Timer:
    def __init__(self, work_duration=25, break_duration=5):
        self.work_duration = work_duration * 60
        self.break_duration = break_duration * 60
        self.session_type = "Work"

    def start(self):
        duration = self.work_duration if self.session_type == "Work" else self.break_duration
        for remaining in yield_time(duration):
            mins, secs = divmod(remaining, 60)
            print(f"{self.session_type} Session - {mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
        notify()
        self.save_session()

    def save_session(self):
        with open("pomodoro_sessions.txt", "a") as f:
            f.write(f"{self.session_type} session completed.\n")

def notify():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()
    time.sleep(5)
    pygame.mixer.music.stop()

def yield_time(duration):
    for remaining in range(duration, 0, -1):
        yield remaining

if __name__ == "__main__":
    pomodoro = Timer()
    pomodoro.start()
