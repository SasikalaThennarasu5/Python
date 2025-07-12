# Online Order History

orders = ["Order1", "Order2", "Order3", "Order4", "Order5", "Order6"]

# Add new
orders.append("Order7")

# Cancelled
orders.remove("Order3")

# Last 5
print("Last 5 orders:", orders[-5:])

# Count
print("Total orders:", len(orders))
