# Handles weather data storage and retrieval

weather_db = {}

def add_weather_data(coords, city, weather_description):
    weather_db[coords] = {
        'city': city,
        'weather': weather_description
    }

def get_weather(coords):
    return weather_db.get(coords, None)
