email = input("Enter your email: ")
if "@" in email and "." in email:
    user, domain = email.split("@")[0], email.split("@")[1]
    if domain == "gmail.com" and len(user) > 5:
        print("Valid Gmail")
    else:
        print("Invalid Gmail")
else:
    print("Invalid email format")