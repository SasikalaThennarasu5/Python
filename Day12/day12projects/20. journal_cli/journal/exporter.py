import os
from datetime import datetime

JOURNAL_DIR = "journal_data"

def export_all(export_file="journal_export.txt"):
    with open(export_file, "w") as outfile:
        for file in sorted(os.listdir(JOURNAL_DIR)):
            if file.endswith(".txt"):
                with open(os.path.join(JOURNAL_DIR, file)) as infile:
                    outfile.write(f"\n=== {file} ===\n")
                    outfile.write(infile.read())