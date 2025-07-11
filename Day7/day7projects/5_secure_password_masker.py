password = input("Enter your password: ")
if len(password) >= 2:
    masked = password[0] + "*" * (len(password) - 2) + password[-1]
else:
    masked = "*" * len(password)
print("Masked Password:", masked)