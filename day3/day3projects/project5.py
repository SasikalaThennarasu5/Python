# 5. BMI Calculator & Category Checker
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"
print(f"BMI: {bmi:.2f} ({category})")
