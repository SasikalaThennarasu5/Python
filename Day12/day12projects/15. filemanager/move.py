# filemanager/move.py

import os
import shutil

def move_files(file_dict, target_base):
    for category, files in file_dict.items():
        target_folder = os.path.join(target_base, category)
        os.makedirs(target_folder, exist_ok=True)
        for file_path in files:
            try:
                filename = os.path.basename(file_path)
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved: {filename} -> {category}/")
            except Exception as e:
                print(f"Error moving {file_path}: {e}")
