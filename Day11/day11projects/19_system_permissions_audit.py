required = {"read", "write"}
user_permissions = {"read"}

print("Has all permissions?", required.issubset(user_permissions))
missing = required - user_permissions
print("Missing:", missing)