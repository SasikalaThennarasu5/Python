import os

path = input("Enter directory path: ")
try:
    files = os.listdir(path)
    print("Files and directories:")
    for f in files:
        print(f)
except FileNotFoundError:
    print("Directory not found.")
