votes = {}
question = input("Enter poll question: ")

while True:
    option = input("Enter option to vote (or 'end' to finish): ").lower()
    if option == 'end': break
    votes[option] = votes.get(option, 0) + 1

print(f"\nResults for: {question}")
for opt, count in votes.items():
    print(f"{opt.capitalize()}: {count} votes")
