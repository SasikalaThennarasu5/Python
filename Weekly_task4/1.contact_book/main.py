
from contacts import *

def main():
    contacts = load_contacts()

    while True:
        print("\n1. Add 2. Update 3. Delete 4. Search 5. List 6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            tags = set(input("Tags (comma-separated): ").split(","))
            category = tuple(input("Category (e.g. Family, Work): ").split(","))
            add_contact(contacts, name, phone, email, tags, category)

        elif choice == "2":
            name = input("Name: ")
            field = input("Field to update (phone/email): ")
            value = input("New value: ")
            update_contact(contacts, name, field, value)

        elif choice == "3":
            name = input("Name to delete: ")
            delete_contact(contacts, name)

        elif choice == "4":
            keyword = input("Search by name: ")
            result = search_contacts(contacts, keyword)
            list_contacts(result)

        elif choice == "5":
            list_contacts(contacts)

        elif choice == "6":
            save_contacts(contacts)
            break

if __name__ == "__main__":
    main()
