slotA = {"Mon 9AM", "Wed 11AM"}
slotB = {"Wed 11AM", "Fri 1PM"}

conflict = slotA & slotB
available = slotA - slotB

print("Conflicts:", conflict)
print("Available:", available)