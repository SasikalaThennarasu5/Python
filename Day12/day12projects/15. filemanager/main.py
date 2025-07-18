# filemanager/main.py

import sys
import os
from filemanager import scan, move, report

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <target_directory>")
        return

    target_dir = sys.argv[1]

    if not os.path.isdir(target_dir):
        print(f"❌ Directory '{target_dir}' not found.")
        return

    print(f"📁 Scanning directory: {target_dir}")
    file_data = scan.scan_directory(target_dir)
    report.generate_report(file_data)
    move.move_files(file_data, target_dir)
    print("✅ File organization complete.")

if __name__ == "__main__":
    main()
