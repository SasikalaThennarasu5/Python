# shift_utils.py

# Set of all unique shifts assigned
assigned_shifts = set()

# Dictionary to store shift data with employee ID tuple as key
shift_data = {}

def assign_shift(employee_id, name, department, shift):
    emp_key = (employee_id,)  # Tuple key for employee

    # Check if shift already assigned to someone else
    if shift in assigned_shifts:
        print(f"❌ Shift '{shift}' already assigned. Choose a different one.")
        return False

    shift_data[emp_key] = {
        "name": name,
        "department": department,
        "shift": shift
    }
    assigned_shifts.add(shift)
    print(f"✅ Shift assigned to {name} (ID: {employee_id})")
    return True

def display_shifts():
    print("\nEmployee Shift Schedule:")
    print("-" * 35)
    for emp_key, details in shift_data.items():
        print(f"ID: {emp_key[0]}, Name: {details['name']}, Dept: {details['department']}, Shift: {details['shift']}")