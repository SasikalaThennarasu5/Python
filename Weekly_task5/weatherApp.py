# Weather App using OpenWeatherMap API

import requests
import json
from datetime import datetime

class WeatherApp:
    def __init__(self, api_key, favorites_file="favorites.json"):
        self.api_key = api_key
        self.favorites_file = favorites_file
        self.favorites = self.load_favorites()

    def get_weather(self, city):
        try:
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"
            res = requests.get(url).json()
            if res.get("cod") != 200:
                return f"Error: {res.get('message')}"
            weather = {
                "city": res["name"],
                "temp_c": res["main"]["temp"],
                "temp_f": res["main"]["temp"] * 9 / 5 + 32,
                "desc": res["weather"][0]["description"],
                "humidity": res["main"]["humidity"]
            }
            return weather
        except Exception as e:
            return f"Error: {str(e)}"

    def get_forecast(self, city):
        try:
            url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={self.api_key}&units=metric"
            res = requests.get(url).json()
            if res.get("cod") != "200":
                return f"Error: {res.get('message')}"
            forecast = []
            for entry in res["list"][:5]:  # first 5 forecasts (~1 day apart)
                dt = datetime.fromtimestamp(entry["dt"])
                temp = entry["main"]["temp"]
                desc = entry["weather"][0]["description"]
                forecast.append((dt.strftime("%Y-%m-%d %H:%M"), temp, desc))
            return forecast
        except Exception as e:
            return f"Error: {str(e)}"

    def save_favorite(self, city):
        if city not in self.favorites:
            self.favorites.append(city)
            self.save_favorites()

    def load_favorites(self):
        try:
            with open(self.favorites_file, 'r') as f:
                return json.load(f)
        except:
            return []

    def save_favorites(self):
        with open(self.favorites_file, 'w') as f:
            json.dump(self.favorites, f)

    def show_weather_alerts(self, city):
        # Note: Real alerts require a premium OpenWeatherMap subscription.
        # We'll simulate it.
        return f"No weather alerts for {city} (simulated)."

# CLI for demo
if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    app = WeatherApp(api_key)

    while True:
        print("\n--- Weather App ---")
        print("1. Current Weather\n2. 5-Day Forecast\n3. Temperature Unit Conversion\n4. Weather Alerts\n5. Save Favorite Location\n6. View Favorites\n7. Exit")
        choice = input("Choose: ")

        if choice == '1':
            city = input("Enter city: ")
            weather = app.get_weather(city)
            if isinstance(weather, dict):
                print(f"{weather['city']} - {weather['desc'].capitalize()}")
                print(f"Temp: {weather['temp_c']}°C / {weather['temp_f']}°F | Humidity: {weather['humidity']}%")
            else:
                print(weather)
        elif choice == '2':
            city = input("Enter city: ")
            forecast = app.get_forecast(city)
            if isinstance(forecast, list):
                print(f"\n5-Day Forecast for {city}:")
                for dt, temp, desc in forecast:
                    print(f"{dt} - {temp}°C - {desc.capitalize()}")
            else:
                print(forecast)
        elif choice == '3':
            temp = float(input("Enter temperature: "))
            unit = input("Convert to (C/F): ").upper()
            if unit == 'C':
                print(f"{temp}°F = {(temp - 32) * 5 / 9:.2f}°C")
            elif unit == 'F':
                print(f"{temp}°C = {(temp * 9 / 5) + 32:.2f}°F")
            else:
                print("Invalid unit.")
        elif choice == '4':
            city = input("Enter city: ")
            print(app.show_weather_alerts(city))
        elif choice == '5':
            city = input("Enter city: ")
            app.save_favorite(city)
            print("Saved to favorites.")
        elif choice == '6':
            print("Favorite Locations:")
            for c in app.favorites:
                print(f"- {c}")
        elif choice == '7':
            break
