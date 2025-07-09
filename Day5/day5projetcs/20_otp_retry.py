# Project 20: OTP Retry System
otp = "1234"
tries = 0
while tries < 3:
    entry = input("Enter OTP: ")
    if entry == otp:
        print("OTP correct")
        break
    tries += 1
else:
    print("OTP failed")
