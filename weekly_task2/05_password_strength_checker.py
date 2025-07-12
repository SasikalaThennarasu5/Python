import string

def is_strong(password):
    return (
        any(c.islower() for c in password) and
        any(c.isupper() for c in password) and
        any(c.isdigit() for c in password) and
        any(c in string.punctuation for c in password)
    )

while True:
    pwd = input("Enter password: ")
    if is_strong(pwd):
        print("Strong password!")
        break
    else:
        print("Weak password. Include lowercase, uppercase, digit and symbol.")
