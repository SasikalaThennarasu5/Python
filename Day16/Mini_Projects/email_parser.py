import re

# Email validation regex
EMAIL_REGEX = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

def valid_email_generator(lines):
    for line in lines:
        # Find all email-like patterns in each line
        matches = re.findall(EMAIL_REGEX, line)
        for email in matches:
            yield email

if __name__ == "__main__":
    # Sample email lines (can be replaced with file.readlines())
    email_lines = [
        "Contact us at support@example.com for help.",
        "Invalid: test@@mail.com or just text",
        "Sales: sales@company.org and HR: hr@company.org",
        "This line has no email",
        "admin123@domain.co.in"
    ]

    print(" Valid Emails Found:")
    email_iter = valid_email_generator(email_lines)

    try:
        while True:
            print(next(email_iter))
    except StopIteration:
        print("All valid emails processed.")
