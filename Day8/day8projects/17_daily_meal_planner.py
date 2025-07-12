# Daily Meal Planner

meals = [["Monday", "Idly"], ["Tuesday", "Dosa"], ["Saturday", "Poori"], ["Sunday", "Biriyani"]]

# Update
meals[0][1] = "Pongal"

# Remove
meals.remove(["Tuesday", "Dosa"])

# Weekend meals
print("Weekend meals:", meals[-2:])
