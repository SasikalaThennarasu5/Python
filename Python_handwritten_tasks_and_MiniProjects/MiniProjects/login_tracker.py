# 4. Simple Login Attempt Tracker
# Scenario: Limit login attempts for user security

# Input: username & password
correct_username = "admin"
correct_password = "pass123"

# Allow 3 attempts using a for loop
for attempt in range(1, 4):
    username = input("Enter username: ")
    password = input("Enter password: ")

    # Use variables and if-else
    # If credentials match, print "Login Successful", else "Account Locked".
    if username == correct_username and password == correct_password:
        print("\n Login Successful!")
        break
    else:
        print(f" Incorrect credentials. Attempt {attempt} of 3.\n")
else:
    print(" Account Locked due to 3 failed attempts.")
