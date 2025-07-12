contacts = []

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    contacts.append([name, phone, email])
    print("Contact added.")

def search_contact():
    key = input("Search name: ").lower()
    for c in contacts:
        if key in c[0].lower():
            print("Found:", c)


def delete_contact():
    name = input("Enter name to delete: ").lower()
    for i, c in enumerate(contacts):
        if name == c[0].lower():
            contacts.pop(i)
            print("Deleted.")
            return
    print("Not found.")

def show_all():
    for c in contacts:
        print(c)

while True:
    print("\n1. Add\n2. Search\n3. Delete\n4. Show All\n5. Exit")
    ch = input("Choose: ")
    if ch == '1': add_contact()
    elif ch == '2': search_contact()
    elif ch == '3': delete_contact()
    elif ch == '4': show_all()
    elif ch == '5': break
    else: print("Invalid")
