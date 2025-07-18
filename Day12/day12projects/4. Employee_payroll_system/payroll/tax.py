def calculate_tax(gross):
    if gross <= 5000:
        return 0
    elif gross <= 10000:
        return gross * 0.1
    else:
        return gross * 0.2
