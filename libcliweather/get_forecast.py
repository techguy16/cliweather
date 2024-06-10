import requests
import json

from colorama import Fore, Style

weather = {
    "0": "Clear",
    "1": "Mainly clear",
    "2": "Mainly clear",
    "3": "Mainly clear",
    "51": "Drizzle",
    "52": "Drizzle",
    "53": "Drizzle",
    "80": "Rain"
}
def get_weather(lat, long):
    # print(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m")
    searched_data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code").text
    searched_data = json.loads(searched_data)
    # print(searched_data)
    tempWeather = str(searched_data["current"]["weather_code"])
    print(f"{Style.BRIGHT}{Fore.GREEN}Currently {Fore.RESET}{searched_data["current"]["temperature_2m"]}{searched_data["current_units"]["temperature_2m"]}{Style.RESET_ALL} with {Style.BRIGHT}{weather[tempWeather]}")