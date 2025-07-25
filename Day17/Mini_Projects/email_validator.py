import re

def email_validator(email_list):
    """
    Generator that yields only valid emails from a list using regex.
    Stops after 10 valid emails.
    """
    pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    valid_count = 0

    for email in email_list:
        if pattern.match(email):
            yield email
            valid_count += 1
        if valid_count == 10:
            break

# Example usage
def main():
    emails = [
        "test@example.com", "invalid@", "user@domain.org", "bademail.com",
        "good.email+alias@gmail.com", "john_doe123@company.net", "nope@no",
        "foo@bar.co", "alice@xyz.in", "bob_smith@edu.edu", "extra1@mail.com",
        "extra2@mail.net", "wrong@.com"
    ]

    print(" Valid Emails (Max 10):\n")
    for valid_email in email_validator(emails):
        print(valid_email)

if __name__ == "__main__":
    main()
