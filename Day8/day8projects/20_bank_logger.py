# Bank Transaction Logger

transactions = [500, -100, 1200, -300, 200]

# Add
transactions.append(-150)

# Remove error
transactions.remove(-300)

# Balance
print("Balance:", sum(transactions))

# Last 3
print("Recent transactions:", transactions[-3:])
