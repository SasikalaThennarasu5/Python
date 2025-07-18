from weather_data import weather

def main():
    visited_cities = set()

    while True:
        print("\n--- City Weather Report ---")
        print("1. Add City Weather Data")
        print("2. Get Weather by Coordinates")
        print("3. List Visited Cities")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            city = input("Enter city name: ")
            lat = float(input("Enter latitude: "))
            lon = float(input("Enter longitude: "))
            weather_desc = input("Enter weather description: ")
            weather.add_weather_data((lat, lon), city, weather_desc)
            visited_cities.add(city)
            print(f"Added weather data for {city}.")

        elif choice == '2':
            lat = float(input("Enter latitude: "))
            lon = float(input("Enter longitude: "))
            result = weather.get_weather((lat, lon))
            if result:
                print(f"City: {result['city']}, Weather: {result['weather']}")
            else:
                print("Weather data not found for the given coordinates.")

        elif choice == '3':
            print("Visited Cities:", ', '.join(visited_cities) if visited_cities else "None")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
