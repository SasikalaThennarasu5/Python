# 14. Username Availability Checker
usernames = ["alice", "bob", "admin"]
new_username = input("Choose a username: ").lower()
if new_username in usernames:
    print("Username already taken.")
else:
    print("Username available.")