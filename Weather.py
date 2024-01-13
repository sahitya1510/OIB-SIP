pip install requests

import requests

def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can use 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            print(f"\nWeather in {location.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {description}")
        else:
            print(f"Error: {data['message']}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Command-Line Weather App")

    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    location = input("Enter a city or ZIP code: ")

    get_weather(api_key, location)

if __name__ == "__main__":
    main()
