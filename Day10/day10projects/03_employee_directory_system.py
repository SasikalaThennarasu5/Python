# 3. Employee Directory System

employees = {
    101: {"name": "Alice", "dept": "HR", "salary": 40000},
    102: {"name": "Bob", "dept": "IT", "salary": 50000}
}

# Add employee
employees.setdefault(103, {"name": "Carol", "dept": "Finance", "salary": 45000})

# Update salary
employees[101]["salary"] = 42000

# Delete employee
employees.pop(102, None)

# Search by dept
dept = "Finance"
result = [emp["name"] for emp in employees.values() if emp["dept"] == dept]
print("In Finance:", result)