class LoginFailedError(Exception): pass

def login_system(users):
    attempts = 0
    while attempts < 3:
        try:
            username = input("Username: ")
            password = input("Password: ")
            if users.get(username) != password:
                raise ValueError("Invalid credentials")
            print("Login successful")
            return
        except Exception as e:
            attempts += 1
            log_error(str(e))
    raise LoginFailedError("3 failed attempts")

def log_error(msg):
    from datetime import datetime
    with open("login_errors.log", "a") as f:
        f.write(f"{datetime.now()}: {msg}\n")