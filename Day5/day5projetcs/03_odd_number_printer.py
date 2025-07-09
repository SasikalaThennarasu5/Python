# Project 3: Odd Number Printer
i = 1
odds = []
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    odds.append(i)
    i += 1
print("Odd numbers:", odds)
