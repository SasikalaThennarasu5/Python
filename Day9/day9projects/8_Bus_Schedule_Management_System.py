# Project 8: Bus Schedule Management System
routes = [
    (101, "08:00", "10:00", ("Stop1", "Stop2", "Stop3")),
    (102, "09:00", "11:00", ("StopA", "StopB", "StopC"))
]

for bus_no, dep, arr, stops in routes:
    print(f"Bus {bus_no}: {dep} to {arr} via {', '.join(stops)}")