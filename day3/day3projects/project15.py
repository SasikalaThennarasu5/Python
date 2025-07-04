#  15. Bitwise Access Rights Checker
READ = 1
WRITE = 2
EXECUTE = 4
user_perm = int(input("Enter permission number: "))
print("Read Access:", bool(user_perm & READ))
print("Write Access:", bool(user_perm & WRITE))
print("Execute Access:", bool(user_perm & EXECUTE))
