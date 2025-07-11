full_name = input("Enter full name (First Last): ").split()
if len(full_name) >= 2:
    first, last = full_name
    username = first[:3] + last[-2:]
    print("Generated Username:", username)
else:
    print("Please enter both first and last names.")