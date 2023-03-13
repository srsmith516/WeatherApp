import datetime as dt
import requests

API_KEY = open('apikey.txt','r').read()

def k_to_f(kelvin):
        celsius = kelvin - 273.15
        fahrenheit = celsius * (9/5) + 32
        return celsius, fahrenheit

def get_coor(arg):
    if(arg == "Home"):
            return 33.97, -117.32
    else:
            return 0.00, 0.00


def get_weather_data(Location):
    lat, lon = get_coor(Location)
    url = "https://api.openweathermap.org/data/2.5/weather?lat="+str(lat)+"&lon="+str(lon)+"&appid=" + API_KEY
    response = requests.get(url).json()
    temp_kelvin = response['main']['temp']
    temp_celsius, temp_fahrenheit = k_to_f(temp_kelvin)
    feels_like_kelvin = response['main']['feels_like']
    feels_like_celsius, feels_like_fahrenheit = k_to_f(feels_like_kelvin)
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    print(f"Temperature: {temp_fahrenheit:.2f}")
    print(response)
    return temp_celsius, temp_fahrenheit, feels_like_celsius, feels_like_fahrenheit, humidity, wind_speed, sunrise_time, sunset_time
