# Employee Management System

employees = [["John", "HR"], ["Alice", "IT"], ["Bob", "Finance"]]

# Add employee
employees.append(["Nina", "Marketing"])

# Update department
employees[1][1] = "Tech Support"

# Remove employee
employees.remove(["Bob", "Finance"])

# Sort alphabetically by name
employees.sort(key=lambda x: x[0])

print("Employees:")
for emp in employees:
    print(f"{emp[0]} - {emp[1]}")
