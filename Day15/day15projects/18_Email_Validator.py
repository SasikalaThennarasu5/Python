class InvalidEmailFormatError(Exception): pass

def validate_emails(emails):
    for email in emails:
        try:
            if '@' not in email or '.' not in email:
                raise InvalidEmailFormatError("Invalid format")
        except Exception as e:
            log(str(e))

def log(msg):
    with open("email_errors.log", "a") as f:
        f.write(msg + "\n")