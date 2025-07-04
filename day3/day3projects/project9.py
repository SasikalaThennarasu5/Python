#  9. User Age Classification System
name = input("Enter name: ")
age = int(input("Enter age: "))
if age < 13:
    category = "Child"
elif age <= 19:
    category = "Teenager"
elif age <= 59:
    category = "Adult"
else:
    category = "Senior"
print(f"{name} is a {category}")
