# 19. Email Formatter
first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()
email = f"{first_name}.{last_name}@example.com"
print("📧 Generated Email:", email)
print("Type of email:", type(email))