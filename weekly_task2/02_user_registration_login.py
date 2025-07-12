users = []

def register():
    username = input("Enter username: ")
    password = input("Enter password: ")
    users.append({'username': username, 'password': password})
    print("User registered.")

def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in users:
            if user['username'] == username and user['password'] == password:
                print("Login successful!")
                return True
        attempts -= 1
        print(f"Login failed. Attempts left: {attempts}")
    print("Login blocked.")
    return False

def show_users():
    print("Registered Users:")
    for u in users:
        print("-", u['username'])

while True:
    print("\n1. Register\n2. Login\n3. Show Users\n4. Exit")
    ch = input("Choose option: ")
    if ch == '1':
        register()
    elif ch == '2':
        login()
    elif ch == '3':
        show_users()
    elif ch == '4':
        break
    else:
        print("Invalid input.")

