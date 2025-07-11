name = input("Enter your name: ").title()
salary = input("Enter your salary: ").replace(",", "")
salary = float(salary)
print("My name is %s and I earn ₹%.2f" % (name, salary))