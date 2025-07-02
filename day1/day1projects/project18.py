# 18. Simple BMI Calculator
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
print(f"\n💪 Your BMI is: {bmi:.2f}")
print("Type of BMI variable:", type(bmi))