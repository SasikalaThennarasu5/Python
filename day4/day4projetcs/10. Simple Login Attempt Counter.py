# Project 10: Simple Login Attempt Counter
print("\nProject 10: Simple Login Attempt Counter")
username = "admin"
password = "1234"
for attempt in range(3):
    user = "admin"
    pwd = "1234"
    if user == username and pwd == password:
        print("Login Successful")
        break
else:
    print("Account Locked")
