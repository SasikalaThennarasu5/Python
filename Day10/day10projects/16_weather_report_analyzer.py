# 16. Weather Report Analyzer

weather = {
    "Chennai": [33, 34, 35],
    "Delhi": [28, 30, 32],
}

# Add new temp
weather["Chennai"].append(36)

# Average temp per city
for city, temps in weather.items():
    avg = sum(temps) / len(temps)
    print(f"{city} Avg Temp: {avg:.1f}")

# Hottest average city
hottest = max(weather.items(), key=lambda x: sum(x[1])/len(x[1]))
print("Hottest City:", hottest[0])
