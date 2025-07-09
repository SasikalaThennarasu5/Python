# Project 17: Step Tracker
days = 0
total = 0
while days < 7:
    steps = int(input(f"Day {days+1} steps: "))
    if steps == 0:
        continue
    total += steps
    days += 1
else:
    print(f"Total: {total}, Avg: {total/7}")
