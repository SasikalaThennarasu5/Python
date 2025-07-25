def lazy_contact_searcher(contacts, start_char):
    key = start_char.lower()
    while True:
        found = False
        for name, number in contacts.items():
            if name.lower().startswith(key):
                new_key = yield f"{name}: {number}"
                if new_key:
                    key = new_key.lower()
                    break
                found = True
        if not found:
            yield f"No more contacts starting with '{key}'"
            return  # Stop generator

if __name__ == "__main__":
    contacts = {
        "Alice": "123-456",
        "Alan": "111-222",
        "Bob": "333-444",
        "Charlie": "555-666",
        "Catherine": "777-888"
    }

    print(" Searching contacts starting with 'A':")
    searcher = lazy_contact_searcher(contacts, "A")
    
    try:
        print(next(searcher))         # Alice
        print(searcher.send(None))   # Alan
        print(searcher.send("C"))    # Charlie
        print(next(searcher))        # Catherine
        print(next(searcher))        # No more contacts...
    except StopIteration:
        print("🔚 Search ended.")
