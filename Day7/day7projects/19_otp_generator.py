import random, string
mobile = input("Enter your mobile number: ")
last4 = mobile[-4:]
otp = last4 + ''.join(random.choices(string.ascii_uppercase + string.digits, k=2))
print("Generated OTP:", otp)