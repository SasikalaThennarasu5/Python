import os
from pathlib import Path

def human_readable(func):
    def wrapper(*args, **kwargs):
        for path, size in func(*args, **kwargs):
            yield path, f"{size / (1024*1024):.2f} MB"
    return wrapper

@human_readable
def analyze_directory_size(directory):
    size_map = {}
    try:
        for root, dirs, files in os.walk(directory):
            for name in files:
                path = os.path.join(root, name)
                try:
                    size = os.path.getsize(path)
                    size_map[path] = size
                except Exception as e:
                    print(f"Permission denied or error: {e}")
        for path, size in sorted(size_map.items(), key=lambda x: -x[1]):
            yield path, size
    except Exception as e:
        print(f"Error analyzing directory: {e}")

if __name__ == "__main__":
    dir_path = input("Enter the directory path to analyze: ")
    for file, size in analyze_directory_size(dir_path):
        print(f"{file} - {size}")
