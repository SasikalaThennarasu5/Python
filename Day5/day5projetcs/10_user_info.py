# Project 10: User Info Collector
data = {}
i = 0
while i < 5:
    name = input("Enter name: ").strip()
    if name == "":
        continue
    age = int(input("Enter age: "))
    data[name] = age
    i += 1
    pass
print("User info:", data)
