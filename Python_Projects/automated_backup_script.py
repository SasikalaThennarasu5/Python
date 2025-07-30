import os
import zipfile
import schedule
import time
from datetime import datetime

def schedule_backup(func):
    def wrapper(*args, **kwargs):
        print("Scheduling backup...")
        return func(*args, **kwargs)
    return wrapper

class Backup:
    def __init__(self, source_dir, backup_dir):
        self.source_dir = source_dir
        self.backup_dir = backup_dir

    def _zip_folder(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_filename = f"backup_{timestamp}.zip"
        backup_path = os.path.join(self.backup_dir, backup_filename)

        with zipfile.ZipFile(backup_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(self.source_dir):
                for file in files:
                    full_path = os.path.join(root, file)
                    arcname = os.path.relpath(full_path, self.source_dir)
                    zipf.write(full_path, arcname)
                    yield f"Added {arcname} to backup"

    @schedule_backup
    def run_backup(self):
        print("Starting backup...")
        try:
            for status in self._zip_folder():
                print(status)
            print("Backup completed successfully.")
        except Exception as e:
            print(f"Backup failed: {e}")

if __name__ == "__main__":
    source = input("Enter the source directory: ")
    dest = input("Enter the destination backup directory: ")

    backup = Backup(source, dest)
    schedule.every().day.at("01:00").do(backup.run_backup)

    print("Automated backup scheduled daily at 01:00 AM.")
    while True:
        schedule.run_pending()
        time.sleep(1)
