# 13. Profile Builder
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
profile = {"Name": name, "Age": age, "City": city}
print(f"\n👤 Profile Summary: {profile['Name']} is {profile['Age']} years old and lives in {profile['City']}.")