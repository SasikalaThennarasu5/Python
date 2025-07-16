taken = {"user1", "user2"}
suggestions = ["user3", "user2", "user4"]
valid = []

for name in suggestions:
    if name not in taken:
        taken.add(name)
        valid.append(name)

print("Valid suggestions:", valid)