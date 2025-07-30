
import os
import shutil
from functools import wraps

# Decorator: @dry_run
def dry_run(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("[Dry Run] Previewing file organization...")
        for file in func(*args, dry=True, **kwargs):
            print(f"Would move: {file}")
    return wrapper

# Generator to yield files being moved
def get_files(directory):
    for file in os.listdir(directory):
        full_path = os.path.join(directory, file)
        if os.path.isfile(full_path):
            yield full_path

# Function to organize files
@dry_run
def organize(directory, dry=False):
    extension_map = {
        "jpg": "Images",
        "png": "Images",
        "jpeg": "Images",
        "mp4": "Videos",
        "mov": "Videos",
        "mp3": "Music",
        "txt": "Documents",
        "pdf": "Documents",
        "py": "Code",
        "zip": "Archives",
    }

    moved_files = []
    for filepath in get_files(directory):
        ext = filepath.split(".")[-1].lower()
        folder = extension_map.get(ext, "Others")
        dest_folder = os.path.join(directory, folder)
        os.makedirs(dest_folder, exist_ok=True)
        dest_path = os.path.join(dest_folder, os.path.basename(filepath))
        if not dry:
            try:
                shutil.move(filepath, dest_path)
            except PermissionError:
                print(f"Permission denied: {filepath}")
        moved_files.append(filepath)
        yield filepath

    return moved_files

# If you want to run directly, uncomment:
# organize("path_to_directory")
