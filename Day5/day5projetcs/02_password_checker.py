# Project 2: Password Checker with Limited Attempts
correct_password = "admin123"
attempts = 0
while attempts < 3:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Access granted")
        break
    attempts += 1
else:
    print("Too many attempts!")
