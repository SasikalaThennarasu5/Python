import os
from datetime import datetime

JOURNAL_DIR = "journal_data"

def save_entry(text):
    os.makedirs(JOURNAL_DIR, exist_ok=True)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = os.path.join(JOURNAL_DIR, f"{date_str}.txt")
    with open(filename, "a") as f:
        f.write(f"\n[{datetime.now().strftime('%H:%M')}]\n{text}\n")

def new_entry():
    print("Write your journal entry (end with a blank line):")
    lines = []
    while True:
        line = input()
        if not line.strip():
            break
        lines.append(line)
    save_entry("\n".join(lines))