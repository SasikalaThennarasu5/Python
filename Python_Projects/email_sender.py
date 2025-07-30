import smtplib
from email.message import EmailMessage
from functools import wraps
import time
import os

def retry(attempts=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Attempt {attempt+1} failed: {e}")
                    time.sleep(delay)
            print("All attempts failed.")
        return wrapper
    return decorator

class Email:
    def __init__(self, subject, body, sender, recipients, attachments=None):
        self.subject = subject
        self.body = body
        self.sender = sender
        self.recipients = recipients
        self.attachments = attachments if attachments else []

    def build_message(self):
        msg = EmailMessage()
        msg['Subject'] = self.subject
        msg['From'] = self.sender
        msg['To'] = ', '.join(self.recipients)
        msg.set_content(self.body)

        for filepath in self.attachments:
            if os.path.exists(filepath):
                with open(filepath, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(filepath)
                    msg.add_attachment(file_data, maintype='application',
                                       subtype='octet-stream', filename=file_name)
        return msg

@retry(attempts=3)
def send_email(email_obj, smtp_server='smtp.gmail.com', port=587, password=''):
    msg = email_obj.build_message()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls()
        server.login(email_obj.sender, password)
        server.send_message(msg)
        print("Email sent successfully!")

# Example usage
if __name__ == "__main__":
    email = Email(
        subject="Test Email",
        body="This is a test email sent from Python.",
        sender="your_email@gmail.com",
        recipients=["recipient@example.com"],
        attachments=["example.txt"]
    )
    send_email(email, password="your_email_password")
