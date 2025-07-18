# main.py

from shift_utils import assign_shift, display_shifts

def main():
    assign_shift("E001", "Alice", "HR", "Morning")
    assign_shift("E002", "Bob", "IT", "Afternoon")
    assign_shift("E003", "Charlie", "Finance", "Night")
    assign_shift("E004", "Daisy", "IT", "Morning")  # Should show duplicate warning

    display_shifts()

if __name__ == "__main__":
    main()