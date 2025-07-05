# Project 15: Temperature Category Classifier
print("\\nProject 15: Temperature Category Classifier")
temps = [15, 22, 35, 28]
for t in temps:
    if t < 20:
        cat = "Cold"
    elif t <= 30:
        cat = "Warm"
    else:
        cat = "Hot"
    print(f"{t}°C is {cat}")