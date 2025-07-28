# Contact Book

import csv
import json

class Contact:
    def __init__(self, name, phone, email, category="general"):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email,
            'category': self.category
        }

    @staticmethod
    def from_dict(data):
        return Contact(data['name'], data['phone'], data['email'], data.get('category', 'general'))

class ContactBook:
    def __init__(self, file_path='contacts.json'):
        self.contacts = []
        self.file_path = file_path
        self.load_contacts()

    def add_contact(self, name, phone, email, category="general"):
        self.contacts.append(Contact(name, phone, email, category))

    def search_contact(self, keyword):
        return [c for c in self.contacts if keyword.lower() in c.name.lower() or keyword in c.phone]

    def edit_contact(self, name, new_name=None, new_phone=None, new_email=None, new_category=None):
        for c in self.contacts:
            if c.name == name:
                if new_name: c.name = new_name
                if new_phone: c.phone = new_phone
                if new_email: c.email = new_email
                if new_category: c.category = new_category

    def delete_contact(self, name):
        self.contacts = [c for c in self.contacts if c.name != name]

    def export_to_csv(self, filename='contacts.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['name', 'phone', 'email', 'category'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())

    def group_by_category(self):
        groups = {}
        for c in self.contacts:
            groups.setdefault(c.category, []).append(c)
        return groups

    def save_contacts(self):
        with open(self.file_path, 'w') as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4)

    def load_contacts(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(d) for d in data]
        except FileNotFoundError:
            self.contacts = []

# CLI for demo
if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\n--- Contact Book ---")
        print("1. Add\n2. Search\n3. Edit\n4. Delete\n5. Export CSV\n6. View by Category\n7. Save & Exit")
        choice = input("Choose: ")

        if choice == '1':
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            category = input("Category (e.g. family, work): ") or "general"
            book.add_contact(name, phone, email, category)
        elif choice == '2':
            keyword = input("Search name or phone: ")
            results = book.search_contact(keyword)
            for c in results:
                print(f"{c.name} | {c.phone} | {c.email} | {c.category}")
        elif choice == '3':
            name = input("Name to edit: ")
            new_name = input("New name (or leave blank): ")
            new_phone = input("New phone: ")
            new_email = input("New email: ")
            new_category = input("New category: ")
            book.edit_contact(name, new_name or None, new_phone or None, new_email or None, new_category or None)
        elif choice == '4':
            name = input("Name to delete: ")
            book.delete_contact(name)
        elif choice == '5':
            book.export_to_csv()
            print("Exported to contacts.csv.")
        elif choice == '6':
            groups = book.group_by_category()
            for category, contacts in groups.items():
                print(f"\n[{category.upper()}]")
                for c in contacts:
                    print(f"{c.name} | {c.phone} | {c.email}")
        elif choice == '7':
            book.save_contacts()
            print("Saved. Exiting.")
            break
