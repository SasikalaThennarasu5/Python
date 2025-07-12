# Class Attendance System

master_list = ["Alice", "Bob", "Charlie", "David", "Eva"]
present = ["Alice", "Bob", "Eva", "Alice"]

# Remove duplicates
present = list(set(present))

# Count absentees
absentees = set(master_list) - set(present)
print("Absent:", absentees)
