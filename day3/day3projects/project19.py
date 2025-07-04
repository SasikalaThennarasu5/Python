#  19. Mobile Recharge Validator
mobile = input("Enter mobile number: ")
amount = float(input("Enter recharge amount: "))
if len(mobile) == 10 and amount > 10:
    print("Recharge successful")
else:
    print("Invalid mobile number or amount")