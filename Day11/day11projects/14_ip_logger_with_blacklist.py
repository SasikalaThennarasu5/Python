visitors = set()
blacklist = {"192.168.1.1"}

incoming = ["192.168.1.2", "192.168.1.1", "10.0.0.1"]

for ip in incoming:
    if {ip}.isdisjoint(blacklist):
        visitors.add(ip)

print("Clean IPs:", visitors)