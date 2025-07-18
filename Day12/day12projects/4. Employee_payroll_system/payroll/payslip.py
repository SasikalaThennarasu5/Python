from datetime import datetime
from payroll.salary import calculate_gross_salary
from payroll.tax import calculate_tax

def generate_payslip(employee):
    gross = calculate_gross_salary(employee.base_salary)
    tax = calculate_tax(gross)
    net = gross - tax

    return (
        f"Payslip for {employee.name} (ID: {employee.emp_id})\n"
        f"Base Salary: {employee.base_salary:.2f}\n"
        f"Gross Salary: {gross:.2f}\n"
        f"Tax Deducted: {tax:.2f}\n"
        f"Net Salary: {net:.2f}\n"
        f"Issue Date: {datetime.now().strftime('%Y-%m-%d')}"
    )
