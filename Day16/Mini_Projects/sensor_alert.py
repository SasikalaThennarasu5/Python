import random

def read_sensor():
    value = random.randint(80, 99)  # Simulated sensor range
    print(f"Sensor reading: {value}")
    return value

def alert():
    print(" Critical value reached! ALERT TRIGGERED.")

if __name__ == "__main__":
    sentinel = 99
    sensor_iter = iter(read_sensor, sentinel)

    try:
        for reading in sensor_iter:
            pass  # Just reading until sentinel is hit
        alert()  # Sentinel (99) hit → trigger alert
    except Exception as e:
        print("Error:", e)
