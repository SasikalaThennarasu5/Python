# File Organizer

import os
import shutil
import time

class FileOrganizer:
    def __init__(self, target_dir):
        self.target_dir = target_dir

    def organize_by_extension(self):
        print("Organizing files by extension...")
        for file in os.listdir(self.target_dir):
            path = os.path.join(self.target_dir, file)
            if os.path.isfile(path):
                ext = file.split('.')[-1] if '.' in file else 'no_extension'
                folder = os.path.join(self.target_dir, ext.upper())
                os.makedirs(folder, exist_ok=True)
                shutil.move(path, os.path.join(folder, file))
        print("Organization complete.")

    def remove_duplicates(self):
        print("Removing duplicate files...")
        seen = {}
        for root, _, files in os.walk(self.target_dir):
            for file in files:
                path = os.path.join(root, file)
                with open(path, 'rb') as f:
                    content = f.read()
                key = hash(content)
                if key in seen:
                    os.remove(path)
                    print(f"Removed duplicate: {file}")
                else:
                    seen[key] = path
        print("Duplicate removal complete.")

    def bulk_rename(self, pattern):
        print("Bulk renaming files...")
        i = 1
        for file in os.listdir(self.target_dir):
            path = os.path.join(self.target_dir, file)
            if os.path.isfile(path):
                ext = file.split('.')[-1] if '.' in file else ''
                new_name = f"{pattern}_{i}.{ext}" if ext else f"{pattern}_{i}"
                os.rename(path, os.path.join(self.target_dir, new_name))
                i += 1
        print("Renaming complete.")

    def find_largest_files(self, top_n=5):
        files = []
        for root, _, filenames in os.walk(self.target_dir):
            for f in filenames:
                path = os.path.join(root, f)
                if os.path.isfile(path):
                    size = os.path.getsize(path)
                    files.append((f, size, path))
        largest = sorted(files, key=lambda x: x[1], reverse=True)[:top_n]
        for name, size, path in largest:
            print(f"{name} - {size/1024:.2f} KB - {path}")

    def auto_organize_schedule(self, interval=60):
        print(f"Starting automatic organization every {interval} seconds. Press Ctrl+C to stop.")
        try:
            while True:
                self.organize_by_extension()
                time.sleep(interval)
        except KeyboardInterrupt:
            print("\nAuto-organization stopped.")

# CLI for demo
if __name__ == "__main__":
    path = input("Enter directory path to organize: ")
    if not os.path.isdir(path):
        print("Invalid directory.")
    else:
        organizer = FileOrganizer(path)

        while True:
            print("\n--- File Organizer ---")
            print("1. Organize by Extension\n2. Remove Duplicates\n3. Bulk Rename\n4. Find Largest Files\n5. Start Auto Organizer\n6. Exit")
            choice = input("Choose: ")

            if choice == '1':
                organizer.organize_by_extension()
            elif choice == '2':
                organizer.remove_duplicates()
            elif choice == '3':
                pattern = input("Enter rename pattern: ")
                organizer.bulk_rename(pattern)
            elif choice == '4':
                organizer.find_largest_files()
            elif choice == '5':
                interval = int(input("Enter interval (seconds): "))
                organizer.auto_organize_schedule(interval)
            elif choice == '6':
                break
