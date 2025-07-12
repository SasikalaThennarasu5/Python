# Book Reading Progress Tracker

books = [["Book1", 100, 60], ["Book2", 200, 200], ["Book3", 150, 100]]

# Update progress
books[0][2] = 100

# Check finished
for name, total, read in books:
    status = "Finished" if read >= total else "In progress"
    print(f"{name}: {read}/{total} - {status}")
