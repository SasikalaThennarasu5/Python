import time
import random

# 1. Log file reader generator
def log_reader(filepath):
    with open(filepath, "r") as file:
        for line in file:
            yield line.strip()

# 2. Simulate sensor data (yields temperature every 1 second)
def sensor_data_simulator(count=5):
    for _ in range(count):
        temp = round(random.uniform(20.0, 30.0), 2)
        yield f"Temperature: {temp}°C"
        time.sleep(1)

# 3. Mocked API paginator (returns 5 items per page)
def mock_api_data():
    return list(range(1, 21))  # mock 20 results

def paginate_api(results, page_size=5):
    for i in range(0, len(results), page_size):
        yield results[i:i + page_size]

# 4. Streaming price monitor for stocks
def stock_price_stream(ticker, count=5):
    for _ in range(count):
        price = round(random.uniform(100.0, 200.0), 2)
        yield f"{ticker} price: ${price}"
        time.sleep(1)

# 5. Form validation simulator
def form_validation(form_data):
    if "username" not in form_data or not form_data["username"]:
        yield "Username is required."
    else:
        yield "Username valid."

    if "email" not in form_data or "@" not in form_data["email"]:
        yield "Invalid email address."
    else:
        yield "Email valid."

    if "password" not in form_data or len(form_data["password"]) < 6:
        yield "Password must be at least 6 characters."
    else:
        yield "Password valid."

# ---------------------- RUN Tasks ----------------------
if __name__ == "__main__":
    print("1. Log File Reader:")
    try:
        for log in log_reader("logfile.txt"):
            print(log)
    except FileNotFoundError:
        print("logfile.txt not found — skipping.\n")

    print("2. Sensor Data Stream (5 readings):")
    for reading in sensor_data_simulator(5):
        print(reading)
    print()

    print("3. API Pagination (mocked):")
    api_data = mock_api_data()
    for page in paginate_api(api_data):
        print("Page:", page)
    print()

    print("4. Stock Price Stream for 'AAPL':")
    for price in stock_price_stream("AAPL", 5):
        print(price)
    print()

    print("5. Form Validation Simulation:")
    form = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "abc123"
    }
    for result in form_validation(form):
        print(result)
