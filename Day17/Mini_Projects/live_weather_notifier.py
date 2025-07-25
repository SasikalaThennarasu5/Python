import random
import time

def simulate_temperature():
    """Simulates live temperature readings."""
    temp = random.randint(25, 35)
    while True:
        change = random.randint(-3, 3)
        temp += change
        yield temp
        time.sleep(1)  # Simulate delay like API

def significant_change_generator(source, threshold=5):
    """Yields temperature only if change ≥ ±threshold."""
    prev_temp = next(source)
    yield prev_temp  # Yield the first temp

    for current_temp in source:
        if abs(current_temp - prev_temp) >= threshold:
            yield current_temp
            prev_temp = current_temp

def main():
    print("  Live Weather Notifier (Significant Changes Only) — Press Ctrl+C to stop")
    try:
        source = simulate_temperature()
        notifier = significant_change_generator(source)

        for temp in notifier:
            print(f"  Significant Temperature Change Detected: {temp}°C")

    except KeyboardInterrupt:
        print("\n Stopped weather notifier.")

if __name__ == "__main__":
    main()
