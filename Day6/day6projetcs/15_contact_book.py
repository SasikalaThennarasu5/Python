# Contact Book
contacts = {}

def add_contact(**kwargs):
    global contacts
    contacts[kwargs["name"]] = kwargs["phone"]
    return sorted(contacts)

def search_contact(name):
    return contacts.get(name, "Not Found")

add_contact(name="John", phone="1234567890")
print("Contacts:", add_contact(name="Alice", phone="9876543210"))
print("Search Alice:", search_contact("Alice"))
