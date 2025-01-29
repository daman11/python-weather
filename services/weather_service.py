from constants.Weather import Weather
import requests
import time
def get_weather():
    url = f"https://api.openweathermap.org/data/2.5/weather?q={Weather.CITY}&appid={Weather.API_KEY}"
    try:
        response = requests.get(url)
        data = response.json()

        weather_data = {
            "timestamp": time.strftime("%Y.%m.%d %H:%M:%S"),
            "city": data["name"],
            "pressure": data["main"]["pressure"],
            "temp_min": data["main"]["temp_min"],
            "feels_like": data["main"]["feels_like"],
            "temp": data["main"]["temp"],
            "wind_speed": data["wind"]["speed"],
            "weather_description": data["weather"][0]["description"],
        }

        return weather_data

    except Exception as error:
        print(error)

