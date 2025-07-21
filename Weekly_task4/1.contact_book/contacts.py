
import os
import json
from validator import is_valid_email, is_valid_phone

CONTACTS_FILE = "data/contacts.txt"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

def add_contact(contacts, name, phone, email, tags, category):
    if not is_valid_phone(phone):
        print("Invalid phone number.")
        return
    if not is_valid_email(email):
        print("Invalid email.")
        return
    contacts[name] = {
        "phone": phone,
        "email": email,
        "tags": list(tags),
        "category": category
    }

def update_contact(contacts, name, field, value):
    if name in contacts:
        contacts[name][field] = value
    else:
        print("Contact not found.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found.")

def search_contacts(contacts, keyword):
    return {k: v for k, v in contacts.items() if keyword.lower() in k.lower()}

def list_contacts(contacts):
    for name in sorted(contacts.keys()):
        print(f"{name}: {contacts[name]}")
