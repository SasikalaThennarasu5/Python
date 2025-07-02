# 2. Simple Contact Book

name = input("Enter your name: ")
phone = input("Enter your phone number: ")
email = input("Enter your email: ")

contact = {
    "Name": name,
    "Phone": phone,
    "Email": email
}

print("\n📇 Contact Information:")
print(f"Name: {contact['Name']} (type: {type(contact['Name'])})")
print(f"Phone: {contact['Phone']} (type: {type(contact['Phone'])})")
print(f"Email: {contact['Email']} (type: {type(contact['Email'])})")
