
import requests
import json
from functools import wraps
from time import sleep

def retry(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Attempt {i+1} failed: {e}")
                sleep(2)
        print("All attempts failed.")
    return wrapper

class Weather:
    def __init__(self, city, api_key):
        self.city = city
        self.api_key = api_key
        self.data = {}

    @retry
    def fetch_weather(self):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code != 200:
            raise Exception(f"Error fetching weather: {response.text}")
        self.data = response.json()

    def display_weather(self):
        if not self.data:
            print("No weather data available.")
            return
        main = self.data.get("main", {})
        print(f"Weather in {self.city}:")
        print(f"Temperature: {main.get('temp')}°C")
        print(f"Humidity: {main.get('humidity')}%")
        print(f"Pressure: {main.get('pressure')} hPa")

    def log_weather(self, filename="weather_log.json"):
        with open(filename, "a") as file:
            json.dump(self.data, file)
            file.write("\n")

    def forecast_generator(self):
        forecast = [f"Day {i+1}: Sunny with a chance of clouds" for i in range(3)]  # mock data
        for day in forecast:
            yield day

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    while True:
        city = input("Enter city name (or 'exit' to quit): ").strip()
        if city.lower() == "exit":
            break
        w = Weather(city, api_key)
        w.fetch_weather()
        w.display_weather()
        w.log_weather()
        print("Forecast:")
        for day in w.forecast_generator():
            print("-", day)
