def is_valid_email(email):
    return (
        '@' in email and
        '.' in email.split('@')[-1] and
        len(email) >= 6
    )

while True:
    email = input("Enter email: ")
    if is_valid_email(email):
        print("Valid email!")
        break
    else:
        print("Invalid email format.")
