visitors = set()
blacklist = {"192.168.0.2", "10.0.0.1"}

# Adding IPs
visitors.add("192.168.0.1")
visitors.add("192.168.0.2")
visitors.add("10.0.0.3")

# Removing blacklisted
for ip in blacklist:
    visitors.discard(ip)

print("Unique visitors:", len(visitors))

# Backup
backup = visitors.copy()
print("Backup:", backup)