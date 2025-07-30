
import json
import base64
import os
from cryptography.fernet import Fernet
from getpass import getpass

def logged_in(func):
    def wrapper(self, *args, **kwargs):
        if self.authenticated:
            return func(self, *args, **kwargs)
        else:
            print("Access denied. Please login first.")
    return wrapper

class PasswordEntry:
    def __init__(self, website, username, password):
        self.website = website
        self.username = username
        self.password = password

    def to_dict(self):
        return {
            "website": self.website,
            "username": self.username,
            "password": self.password
        }

class PasswordManager:
    def __init__(self, filename='passwords.enc'):
        self.filename = filename
        self.entries = []
        self.authenticated = False
        self.key_file = 'key.key'
        self.key = self.load_or_create_key()
        self.fernet = Fernet(self.key)
        self.load_passwords()

    def load_or_create_key(self):
        if os.path.exists(self.key_file):
            with open(self.key_file, 'rb') as f:
                return f.read()
        else:
            key = Fernet.generate_key()
            with open(self.key_file, 'wb') as f:
                f.write(key)
            return key

    def authenticate(self):
        password = getpass("Enter master password: ")
        if password == "admin123":  # Dummy check for example
            self.authenticated = True
        else:
            print("Incorrect password.")

    def save_passwords(self):
        data = json.dumps([entry.to_dict() for entry in self.entries])
        encrypted = self.fernet.encrypt(data.encode())
        with open(self.filename, 'wb') as f:
            f.write(encrypted)

    def load_passwords(self):
        if not os.path.exists(self.filename):
            return
        try:
            with open(self.filename, 'rb') as f:
                encrypted = f.read()
            decrypted = self.fernet.decrypt(encrypted)
            data = json.loads(decrypted.decode())
            self.entries = [PasswordEntry(**entry) for entry in data]
        except Exception as e:
            print(f"Failed to load passwords: {e}")

    @logged_in
    def add_password(self, website, username, password):
        self.entries.append(PasswordEntry(website, username, password))
        self.save_passwords()

    @logged_in
    def get_password(self, website):
        for entry in self.entries:
            if entry.website == website:
                return f"Username: {entry.username}, Password: {entry.password}"
        return "Entry not found."

    @logged_in
    def delete_password(self, website):
        self.entries = [e for e in self.entries if e.website != website]
        self.save_passwords()

    def generate_password(self, length=12):
        import random
        import string
        chars = string.ascii_letters + string.digits + "!@#$%^&*()"
        return ''.join(random.choice(chars) for _ in range(length))

    def compromised_passwords(self):
        seen = set()
        for entry in self.entries:
            if entry.password in seen:
                yield entry
            seen.add(entry.password)

    def weak_passwords(self):
        for entry in self.entries:
            if len(entry.password) < 8:
                yield entry

def main():
    manager = PasswordManager()
    manager.authenticate()
    while True:
        print("\n1. Add Password\n2. Get Password\n3. Delete Password\n4. Generate Password\n5. Exit")
        choice = input("Choice: ")
        if choice == '1':
            website = input("Website: ")
            username = input("Username: ")
            password = input("Password: ")
            manager.add_password(website, username, password)
        elif choice == '2':
            website = input("Website: ")
            print(manager.get_password(website))
        elif choice == '3':
            website = input("Website: ")
            manager.delete_password(website)
        elif choice == '4':
            print("Generated Password:", manager.generate_password())
        elif choice == '5':
            break

if __name__ == "__main__":
    main()
