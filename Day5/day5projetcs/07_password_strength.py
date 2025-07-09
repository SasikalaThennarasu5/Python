# Project 7: Password Strength Tester
while True:
    pwd = input("Enter a password: ")
    if len(pwd) < 6:
        print("Too short, try again.")
        continue
    print("Password accepted")
    break
