# Basic File Operations (1–10)

# 1. Create a new text file and write a welcome message.
with open("welcome.txt", "w") as f:
    f.write("Welcome to File Handling in Python!")

# 2. Open a file, write multiple lines, and close it manually.
f = open("multi_lines.txt", "w")
f.write("Line 1\n")
f.write("Line 2\n")
f.close()

# 3. Use the with statement to read a file without manually closing it.
with open("welcome.txt", "r") as f:
    print(f.read())

# 4. Read the contents of a file using .read().
with open("multi_lines.txt", "r") as f:
    content = f.read()
    print(content)

# 5. Read a file line-by-line using .readline().
with open("multi_lines.txt", "r") as f:
    line = f.readline()
    while line:
        print(line.strip())
        line = f.readline()

# 6. Read all lines into a list using .readlines().
with open("multi_lines.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# 7. Append user input to a file.
def append_input():
    text = input("Enter text to append: ")
    with open("user_input.txt", "a") as f:
        f.write(text + "\n")

# 8. Overwrite a file using 'w' mode.
with open("overwrite.txt", "w") as f:
    f.write("This will replace any existing content.")

# 9. Append data to a file and display content.
with open("append.txt", "a") as f:
    f.write("Appended line.\n")
with open("append.txt", "r") as f:
    print(f.read())

# 10. Create a file using 'x' mode, handle file exists error.
try:
    with open("newfile.txt", "x") as f:
        f.write("Created using 'x' mode.")
except FileExistsError:
    print("File already exists.")

    # Working with Context Managers & Modes (11–20)

# 11. Rewrite a script using with to ensure file auto-closing.
with open("auto_close.txt", "w") as f:
    f.write("Using with for auto-closing.")

# 12. Read/write binary file using 'wb' and 'rb'.
with open("binary.dat", "wb") as f:
    f.write(b'\x00\x01Hello')

with open("binary.dat", "rb") as f:
    print(f.read())

# 13. File reader that checks readability and writability.
with open("testfile.txt", "w+") as f:
    print(f.readable(), f.writable())

# 14. Count words, lines, characters.
def file_stats(filename):
    with open(filename, "r") as f:
        text = f.read()
        return len(text.split()), len(text.splitlines()), len(text)

# 15. Log user login/logout time.
from datetime import datetime
with open("login_report.txt", "a") as f:
    f.write(f"User logged in at: {datetime.now()}\n")

# 16. Count specific word appearances.
def count_word(filename, word):
    with open(filename, "r") as f:
        return f.read().lower().count(word.lower())

# 17. Replace a word in file and save.
def replace_word(filename, old, new):
    with open(filename, "r") as f:
        data = f.read().replace(old, new)
    with open(filename, "w") as f:
        f.write(data)

# 18. Copy file contents.
def copy_file(src, dest):
    with open(src, "r") as f1, open(dest, "w") as f2:
        f2.write(f1.read())

# 19. Reverse file contents line-by-line.
def reverse_lines(src, dest):
    with open(src, "r") as f:
        lines = f.readlines()
    with open(dest, "w") as f:
        for line in reversed(lines):
            f.write(line)

# 20. Use writelines() and readlines().
with open("lines.txt", "w") as f:
    f.writelines(["Line1\n", "Line2\n", "Line3\n"])
with open("lines.txt", "r") as f:
    print(f.readlines())

# Error Handling & File Metadata (21–30)
import os
import shutil

# 21. Handle FileNotFoundError.
try:
    with open("nofile.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist!")

# 22. Display file size and last modified date.
def file_info(filename):
    size = os.path.getsize(filename)
    modified = os.path.getmtime(filename)
    return size, modified

# 23. Check file exists and writable.
def check_file_access(filename):
    return os.path.exists(filename) and os.access(filename, os.W_OK)

# 24. try-except-finally with file
try:
    f = open("somefile.txt", "r")
    print(f.read())
except Exception as e:
    print("Error:", e)
finally:
    f.close()

# 25. Print extensions of all files in folder.
def list_extensions(path):
    for fname in os.listdir(path):
        print(os.path.splitext(fname)[1])

# 26. List all .txt files using glob.
import glob
print(glob.glob("*.txt"))

# 27. Rename file with check.
def rename_file(old, new):
    if os.path.exists(new):
        print("Target filename exists!")
    else:
        os.rename(old, new)

# 28. Delete file with error handling.
def delete_file(filename):
    try:
        os.remove(filename)
    except FileNotFoundError:
        print("File not found!")
    except PermissionError:
        print("Permission denied!")

# 29. Create folder structure.
os.makedirs("project/data/logs", exist_ok=True)

# 30. Move file to another folder.
def move_file(src, dest):
    shutil.move(src, dest)

#CSV File Handling (31–35)
import csv

# 31. Create CSV with names and marks.
with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Marks"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 75])

# 32. Read and print students with marks >80.
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if int(row["Marks"]) > 80:
            print(row["Name"])

# 33. Append new data.
with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Charlie", 88])

# 34. Convert CSV to dict.
students = {}
with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        students[row[0]] = int(row[1])
print(students)

# 35. Report highest and average.
marks = list(students.values())
print(f"Highest: {max(marks)}, Average: {sum(marks)/len(marks)}")

#JSON File Handling (36–40)

import json

# 36. Save user profile.
data = {"name": "Alice", "age": 25, "skills": ["Python", "React"]}
with open("profile.json", "w") as f:
    json.dump(data, f)

# 37. Read and display JSON.
with open("profile.json", "r") as f:
    print(json.load(f))

# 38. Add entry to existing JSON.
with open("profile.json", "r") as f:
    profiles = json.load(f)
profiles["email"] = "alice@example.com"
with open("profile.json", "w") as f:
    json.dump(profiles, f, indent=2)

# 39. Mini phonebook app.
def add_contact(name, number):
    try:
        with open("phonebook.json", "r") as f:
            phonebook = json.load(f)
    except FileNotFoundError:
        phonebook = {}
    phonebook[name] = number
    with open("phonebook.json", "w") as f:
        json.dump(phonebook, f, indent=2)

# 40. Validate required keys.
def validate_json(filename, required_keys):
    try:
        with open(filename, "r") as f:
            data = json.load(f)
            return all(key in data for key in required_keys)
    except Exception as e:
        print(e)
        return False

#Log Files & Monitoring (41–45)
from datetime import datetime

# 41. Simple logger.
def log(message):
    with open("app.log", "a") as f:
        f.write(f"{datetime.now()} - {message}\n")

# 42. Monitor (mock logic).
import time
def monitor_folder(folder):
    seen = set(os.listdir(folder))
    time.sleep(2)
    current = set(os.listdir(folder))
    new = current - seen
    for file in new:
        log(f"New file added: {file}")

# 43. Track login activity.
log("User logged in")

# 44. Record execution steps with filtering.
def step_log(message, level="INFO"):
    with open("steps.log", "a") as f:
        f.write(f"{level} - {datetime.now()} - {message}\n")

# 45. Rotate log daily (manual simulation).
def rotate_log():
    if os.path.exists("app.log"):
        os.rename("app.log", f"logs/app_{datetime.now().date()}.log")

#Text File Processing Projects (46–50)

# 46. To-Do List App
def add_task(task):
    with open("todo.txt", "a") as f:
        f.write(task + "\n")

def show_tasks():
    with open("todo.txt", "r") as f:
        print(f.read())

# 47. Merge two text files.
def merge_files(f1, f2, out):
    with open(out, "w") as out_f:
        for file in [f1, f2]:
            with open(file, "r") as f:
                out_f.write(f.read())

# 48. Convert .txt to .pdf (using fpdf)

from fpdf import FPDF

def txt_to_pdf(txtfile, pdffile):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    with open(txtfile, "r") as f:
        for line in f:
            pdf.cell(200, 10, txt=line.strip(), ln=True)
    pdf.output(pdffile)

# 49. File difference checker.
def compare_files(f1, f2):
    with open(f1, "r") as file1, open(f2, "r") as file2:
        for l1, l2 in zip(file1, file2):
            if l1 != l2:
                print(f"Difference: {l1.strip()} != {l2.strip()}")

# 50. Save daily diary by date.
def save_diary(entry):
    filename = f"{datetime.now().date()}.txt"
    with open(filename, "a") as f:
        f.write(entry + "\n")
