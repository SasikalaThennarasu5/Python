# Loan EMI Calculator
def calculate_emi(p, r, t):
    r = r / (12 * 100)
    t = t * 12
    emi = (p * r * (1 + r)**t) / ((1 + r)**t - 1)
    return emi

emi_lambda = lambda p, r, t: calculate_emi(p, r, t)

print("Monthly EMI:", round(emi_lambda(100000, 10, 1), 2))
