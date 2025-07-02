# 17. Unique Visitor Counter
visitors = set()
for i in range(5):
    name = input(f"Enter name of visitor {i+1}: ")
    visitors.add(name)
print("\n🚶 Unique Visitors:", visitors)
print("Total unique visitors:", len(visitors))
