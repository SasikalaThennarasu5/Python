class PasswordTooWeakError(Exception): pass

def validate_user(name, email, age, password):
    try:
        assert isinstance(name, str)
        assert isinstance(email, str)
        if not isinstance(age, int) or age < 13:
            raise ValueError("Age must be an integer and >= 13")
        if len(password) < 6:
            raise PasswordTooWeakError("Password too weak")
    except (ValueError, TypeError, PasswordTooWeakError) as e:
        log_error(str(e))

def log_error(msg):
    with open("registration_errors.log", "a") as f:
        f.write(msg + "\n")