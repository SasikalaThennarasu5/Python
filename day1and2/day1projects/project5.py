# 5. Temperature Converter

celsius_input = input("Enter temperature in Celsius: ")
print("Type before conversion:", type(celsius_input))

celsius = float(celsius_input)
fahrenheit = (celsius * 9/5) + 32

print(f"\n🌡️ {celsius}°C is equal to {fahrenheit}°F")
print("Type after conversion:", type(fahrenheit))
