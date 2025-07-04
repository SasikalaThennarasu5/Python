#  13. Salary Tax Deduction Calculator
salary = float(input("Enter salary in LPA: "))
if salary < 5:
    tax = 0
elif salary <= 10:
    tax = salary * 0.10
else:
    tax = salary * 0.20
net_salary = salary - tax
print(f"Tax: ₹{tax}L, Net Salary: ₹{net_salary}L")