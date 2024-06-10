import argparse
import libcliweather.geocode
import libcliweather.get_forecast

parser = argparse.ArgumentParser()
parser.add_argument("-g", "--geocode", metavar='', type=str, help="Search and set location")
parser.add_argument("-w", "--weather", action="store_true", help="Get weather at lat&long")
args = parser.parse_args()

if args.geocode:
    coords = libcliweather.geocode.search_location(args.geocode, True).split(",")
    lat = coords[0]
    long = coords[1]
    if args.weather:
        libcliweather.get_forecast.get_weather(lat, long)