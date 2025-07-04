# 10. Access Control Based on Role
role = input("Enter role (admin/user): ").lower()
has_id = input("Do you have ID? (yes/no): ").lower()
if role in ["admin", "user"]:
    if role == "admin" and has_id == "yes":
        print("Access granted to admin panel")
    elif role == "user" and has_id == "yes":
        print("Access granted to user panel")
    else:
        print("ID required for access.")
else:
    print("Invalid role")