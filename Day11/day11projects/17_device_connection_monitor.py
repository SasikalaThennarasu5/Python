connected = {"Device1", "Device2"}
disconnected = connected.pop()
print("Disconnected:", disconnected)

other_server = {"Device3", "Device4"}
all_devices = connected | other_server
print("All Devices:", all_devices)