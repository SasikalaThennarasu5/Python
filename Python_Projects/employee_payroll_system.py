
import csv
from functools import wraps

def admin_only(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Admin access verified.")
        return func(*args, **kwargs)
    return wrapper

class Employee:
    def __init__(self, emp_id, name, hours, rate):
        if hours < 0 or rate < 0:
            raise ValueError("Hours and rate must be non-negative.")
        self.emp_id = emp_id
        self.name = name
        self.hours = hours
        self.rate = rate

    def compute_salary(self):
        base = self.hours * self.rate
        overtime = (self.hours - 40) * (self.rate * 1.5) if self.hours > 40 else 0
        salary = base + overtime
        tax = 0.1 if salary < 1000 else 0.2 if salary <= 2000 else 0.3
        return salary * (1 - tax)

class PayrollSystem:
    def __init__(self):
        self.employees = {}

    def add_employee(self, emp):
        self.employees[emp.emp_id] = emp

    @admin_only
    def update_employee_salary(self, emp_id, hours, rate):
        if emp_id in self.employees:
            self.employees[emp_id].hours = hours
            self.employees[emp_id].rate = rate
        else:
            print("Employee not found.")

    def generate_payslips(self):
        for emp in self.employees.values():
            print(f"{emp.name} (ID: {emp.emp_id}) - Salary: ${emp.compute_salary():.2f}")

    def export_to_csv(self, filename="payroll.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Name', 'Hours', 'Rate', 'Salary'])
            for emp in self.employees.values():
                writer.writerow([emp.emp_id, emp.name, emp.hours, emp.rate, f"{emp.compute_salary():.2f}"])

    def get_overtime_employees(self):
        return (emp for emp in self.employees.values() if emp.hours > 40)

if __name__ == "__main__":
    payroll = PayrollSystem()
    payroll.add_employee(Employee("E001", "Alice", 45, 20))
    payroll.add_employee(Employee("E002", "Bob", 38, 18))
    payroll.add_employee(Employee("E003", "Charlie", 50, 22))

    payroll.generate_payslips()
    payroll.export_to_csv()

    print("\nEmployees with Overtime:")
    for emp in payroll.get_overtime_employees():
        print(emp.name)
