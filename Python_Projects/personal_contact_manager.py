import json
import re
from functools import wraps

# Decorator to log function calls
def log_actions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Contact class
class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"

# Manager class
class ContactManager:
    def __init__(self):
        self.contacts = {}

    @log_actions
    def add_contact(self, name, phone, email):
        if not re.match(r"\d{10}$", phone):
            raise ValueError("Invalid phone number format. Must be 10 digits.")
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email format.")
        self.contacts[name] = Contact(name, phone, email)

    @log_actions
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
        else:
            print("Contact not found.")

    @log_actions
    def search_contact(self, query):
        def generator():
            for name, contact in self.contacts.items():
                if query.lower() in name.lower():
                    yield contact
        return generator()

    @log_actions
    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                if not re.match(r"\d{10}$", phone):
                    raise ValueError("Invalid phone number format.")
                self.contacts[name].phone = phone
            if email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                    raise ValueError("Invalid email format.")
                self.contacts[name].email = email
        else:
            print("Contact not found.")

    @log_actions
    def save_to_file(self, filename="contacts.json"):
        data = {name: vars(contact) for name, contact in self.contacts.items()}
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)

    @log_actions
    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
                for name, info in data.items():
                    self.contacts[name] = Contact(**info)
        except FileNotFoundError:
            print("No existing contact file found. Starting fresh.")

    @log_actions
    def display_all_contacts(self):
        for contact in self.contacts.values():
            print("-" * 20)
            print(contact)
            print("-" * 20)

def menu():
    manager = ContactManager()
    manager.load_from_file()

    while True:
        print("\n--- Contact Manager Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Display All Contacts")
        print("6. Save & Exit")

        choice = input("Enter your choice: ")
        try:
            if choice == "1":
                name = input("Name: ")
                phone = input("Phone: ")
                email = input("Email: ")
                manager.add_contact(name, phone, email)
            elif choice == "2":
                name = input("Enter name to delete: ")
                manager.delete_contact(name)
            elif choice == "3":
                query = input("Enter name to search: ")
                results = manager.search_contact(query)
                for contact in results:
                    print(contact)
            elif choice == "4":
                name = input("Enter name to update: ")
                phone = input("New phone (leave blank to skip): ")
                email = input("New email (leave blank to skip): ")
                manager.update_contact(name, phone if phone else None, email if email else None)
            elif choice == "5":
                manager.display_all_contacts()
            elif choice == "6":
                manager.save_to_file()
                print("Contacts saved. Exiting...")
                break
            else:
                print("Invalid choice.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    menu()
