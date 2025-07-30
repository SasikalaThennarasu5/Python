import json
import re
from functools import wraps
from datetime import datetime

def log_actions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with open("log.txt", "a") as log:
            log.write(f"{datetime.now()} - Called {func.__name__}\n")
        return func(*args, **kwargs)
    return wrapper

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def validate_phone(self, phone):
        return re.match(r"^\d{10}$", phone)

    def validate_email(self, email):
        return re.match(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", email)

    @log_actions
    def add_contact(self, name, phone, email):
        if name in self.contacts:
            print("Contact already exists.")
            return
        if not self.validate_phone(phone):
            print("Invalid phone number.")
            return
        if not self.validate_email(email):
            print("Invalid email address.")
            return
        self.contacts[name] = Contact(name, phone, email)
        print("Contact added successfully.")

    @log_actions
    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted.")
        else:
            print("Contact not found.")

    @log_actions
    def update_contact(self, name, phone=None, email=None):
        if name not in self.contacts:
            print("Contact not found.")
            return
        if phone:
            if not self.validate_phone(phone):
                print("Invalid phone number.")
                return
            self.contacts[name].phone = phone
        if email:
            if not self.validate_email(email):
                print("Invalid email address.")
                return
            self.contacts[name].email = email
        print("Contact updated.")

    @log_actions
    def search_contacts(self, keyword):
        return (contact for contact in self.contacts.values() if keyword.lower() in contact.name.lower())

    @log_actions
    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts.values():
            print(contact)

    @log_actions
    def save_to_file(self, filename="contacts.json"):
        with open(filename, "w") as file:
            data = {name: contact.__dict__ for name, contact in self.contacts.items()}
            json.dump(data, file)
        print("Contacts saved.")

    @log_actions
    def load_from_file(self, filename="contacts.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.contacts = {name: Contact(**info) for name, info in data.items()}
            print("Contacts loaded.")
        except FileNotFoundError:
            print("No saved contacts found.")

def main():
    manager = ContactManager()
    manager.load_from_file()

    while True:
        print("\n--- Personal Contact Manager ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Update Contact")
        print("4. Search Contact")
        print("5. Display All Contacts")
        print("6. Save Contacts")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            manager.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Enter name to delete: ")
            manager.delete_contact(name)

        elif choice == "3":
            name = input("Enter name to update: ")
            phone = input("New phone (press Enter to skip): ")
            email = input("New email (press Enter to skip): ")
            phone = phone if phone else None
            email = email if email else None
            manager.update_contact(name, phone, email)

        elif choice == "4":
            keyword = input("Search keyword: ")
            found = False
            for contact in manager.search_contacts(keyword):
                print(contact)
                found = True
            if not found:
                print("No matching contacts.")

        elif choice == "5":
            manager.display_contacts()

        elif choice == "6":
            manager.save_to_file()

        elif choice == "7":
            manager.save_to_file()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
