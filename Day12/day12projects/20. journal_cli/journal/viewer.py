import os
import re
import fnmatch
import textwrap

JOURNAL_DIR = "journal_data"

def view_entries(date=None, keyword=None):
    files = os.listdir(JOURNAL_DIR)
    files = fnmatch.filter(files, "*.txt")

    if date:
        files = [f"{date}.txt"] if f"{date}.txt" in files else []

    for file in files:
        filepath = os.path.join(JOURNAL_DIR, file)
        with open(filepath) as f:
            content = f.read()
            if keyword:
                if not re.search(keyword, content, re.IGNORECASE):
                    continue
            print(f"\n=== {file} ===")
            print(textwrap.fill(content.strip(), width=80))