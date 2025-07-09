# Project 15: Even Number Skipper
i = 1
while i <= 20:
    if i % 2 == 0:
        i += 1
        continue
    print(f"{i}^2 = {i*i}")
    i += 1
