import os

filename = input("Enter filename to write: ")

if os.path.exists(filename):
    print(f"{filename} already exists. Not overwriting.")
else:
    with open(filename, 'w') as f:
        f.write("New file created.")
    print(f"{filename} created successfully.")
