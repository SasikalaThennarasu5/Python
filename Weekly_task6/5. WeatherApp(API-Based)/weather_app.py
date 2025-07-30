import requests
import time
from functools import wraps

# Retry decorator for failed API calls
def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        max_attempts = 3
        for attempt in range(1, max_attempts + 1):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {attempt} failed: {e}")
                time.sleep(2)
        raise Exception("API call failed after 3 attempts.")
    return wrapper

# Weather class using OOP
class Weather:
    def __init__(self, city, data):
        self.city = city
        self.temp = data['main']['temp']
        self.humidity = data['main']['humidity']
        self.weather = data['weather'][0]['description']
        self.wind = data['wind']['speed']

    def __str__(self):
        return (
            f"Weather in {self.city}:\n"
            f"  Temperature: {self.temp}°C\n"
            f"  Humidity: {self.humidity}%\n"
            f"  Condition: {self.weather}\n"
            f"  Wind Speed: {self.wind} m/s"
        )

# File logging
def log_weather(city, weather_obj):
    with open("weather_history.txt", "a") as f:
        f.write(f"{city} | Temp: {weather_obj.temp}°C | Humidity: {weather_obj.humidity}% | "
                f"{weather_obj.weather} | Wind: {weather_obj.wind} m/s\n")

# Generator for 3-day forecast
def forecast_generator():
    forecast = [
        {"day": "Tomorrow", "temp": 30, "condition": "Sunny"},
        {"day": "Day After", "temp": 31, "condition": "Partly Cloudy"},
        {"day": "Third Day", "temp": 29, "condition": "Rainy"},
    ]
    for day in forecast:
        yield day

# API Call
@retry
def get_weather_data(city):
    API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")
    return response.json()

# Main loop
def main():
    weather_db = {}  # Dictionary to store city: Weather

    while True:
        city = input("Enter city name (or 'exit' to stop): ").strip()
        if city.lower() == 'exit':
            break
        try:
            data = get_weather_data(city)
            weather = Weather(city, data)
            weather_db[city] = weather
            print(weather)
            log_weather(city, weather)

            print("\nForecast:")
            for day in forecast_generator():
                print(f"  {day['day']}: {day['temp']}°C, {day['condition']}")

        except Exception as e:
            print(f"Error: {e}")

    print("\n--- Summary ---")
    for city, weather in weather_db.items():
        print(f"{city}: {weather.temp}°C, {weather.weather}")

if __name__ == "__main__":
    main()
