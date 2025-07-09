# Project 9: Fuel Filling Simulation
total = 0
while total < 50:
    fuel = float(input("Enter fuel amount: "))
    if fuel <= 0:
        continue
    total += fuel
    print(f"Total filled: {total}L")
