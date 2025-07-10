# Employee Info Manager
def add_employee(**kwargs):
    info = f"Name: {kwargs['name']}, Role: {kwargs['role']}, Salary: ₹{kwargs['salary']}"
    return info, kwargs

data = add_employee(name="Alice", role="Manager", salary=60000)
print("Formatted Info:", data[0])
print("Dictionary:", data[1])
