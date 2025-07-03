# 20. Data Type Explorer
value = input("Enter any value: ")
print("You entered:", value)
print("Original Type:", type(value))
convert_to = input("Convert to (int, float, bool, str): ")
if convert_to == "int":
    converted = int(value)
elif convert_to == "float":
    converted = float(value)
elif convert_to == "bool":
    converted = bool(value)
elif convert_to == "str":
    converted = str(value)
else:
    converted = value
print("Converted Value:", converted)
print("New Type:", type(converted))
