# filemanager/report.py

def generate_report(file_dict):
    print("\n--- File Organization Report ---")
    for category, files in file_dict.items():
        print(f"{category.capitalize()} ({len(files)} files):")
        for f in files:
            print(f"  - {f}")
