from scapy.all import ARP, Ether, srp
import ipaddress
import time

def speed_test(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Scan completed in {end - start:.2f} seconds")
        return result
    return wrapper

class Scanner:
    def __init__(self, ip_range):
        self.ip_range = ip_range

    @speed_test
    def scan(self):
        try:
            arp = ARP(pdst=self.ip_range)
            ether = Ether(dst="ff:ff:ff:ff:ff:ff")
            packet = ether / arp

            result = srp(packet, timeout=2, verbose=0)[0]
            for sent, received in result:
                yield {'ip': received.psrc, 'mac': received.hwsrc}
        except Exception as e:
            print(f"Scan failed: {e}")

if __name__ == "__main__":
    subnet = input("Enter IP range (e.g., 192.168.1.0/24): ")
    scanner = Scanner(subnet)
    print("Scanning network...")
    for host in scanner.scan():
        print(f"Host found: IP={host['ip']}, MAC={host['mac']}")
