
import random
import time

def temperature_sensor():
    """Infinite generator simulating temperature readings."""
    override = None
    while True:
        temp = override if override is not None else random.randint(70, 105)
        override = yield temp  # Receive override value via send()

def lazy_stream(generator_func):
    """Wrap generator for lazy iteration using iter(callable, sentinel)."""
    gen = generator_func()

    def fetch():
        try:
            return next(gen)
        except StopIteration:
            return 101  # Exceeds sentinel to break

    return gen, iter(fetch, 101)  # Sentinel is 101 (we stop on >100)

# Example usage
if __name__ == "__main__":
    gen, stream = lazy_stream(temperature_sensor)

    print(" Real-Time Temperature Sensor Stream (breaking on >100):\n")

    for temp in stream:
        print(f"Temperature: {temp}°F")
        time.sleep(0.5)

        # Manual override after 5 readings
        if temp < 90:
            gen.send(102)  # Force break by sending a high value
