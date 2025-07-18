# filemanager/scan.py

import os
import glob

FILE_TYPES = {
    'images': ['*.jpg', '*.jpeg', '*.png', '*.gif'],
    'documents': ['*.pdf', '*.docx', '*.txt'],
    'audio': ['*.mp3', '*.wav'],
    'videos': ['*.mp4', '*.mkv'],
    'archives': ['*.zip', '*.tar', '*.gz']
}

def scan_directory(directory):
    categorized_files = {key: [] for key in FILE_TYPES}
    for category, patterns in FILE_TYPES.items():
        for pattern in patterns:
            path_pattern = os.path.join(directory, pattern)
            categorized_files[category].extend(glob.glob(path_pattern))
    return categorized_files
