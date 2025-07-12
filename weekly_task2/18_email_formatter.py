first = input("Enter first name: ").strip().lower()
last = input("Enter last name: ").strip().lower()
domain = input("Enter domain (e.g. example.com): ").strip().lower()
email = f"{first}.{last}@{domain}"
print("Formatted Email:", email)