import requests
import json

from colorama import Fore, Style

def search_location(query, return_id=False):
    searched_data = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={query}&count=10&language=en&format=json").text
    searched_data = json.loads(searched_data)["results"]
    print(f"{Style.BRIGHT}Locations matching '{query}': {Style.RESET_ALL}")
    index = 0
    for item in searched_data:
        index += 1
        print(f"{Style.BRIGHT}{Fore.GREEN}{index}: {Style.RESET_ALL}{item["name"]}, {Style.BRIGHT}{Fore.BLUE}{item["country"]}")
        
    locationid = input(f"\n{Style.BRIGHT}{Fore.MAGENTA}Input location number: {Style.RESET_ALL}")
    
    if return_id:
        return f"{searched_data[int(locationid) - 1]["latitude"]},{searched_data[int(locationid) - 1]["longitude"]}"