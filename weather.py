import requests, json
from decouple import config

WEATHER_API_KEY = config('WEATHER')

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"


class City:
    def __init__(self,name,lon,lat):
        self.name = name #name of the city
        self.lon = lon #longitude 
        self.lat = lat #latitude
 

Tunis = City("tunis ,TUN","36.8065","10.1815")

 


limit = 5
URL = BASE_URL + "lat=" + Tunis.lat + "&lon=" + Tunis.lon +"&lang=ar"+"&units=metric"+ "&appid=" + WEATHER_API_KEY

# HTTP request
def getCurrentWeather():

    response = requests.get(URL)
    # checking the status code of the request
    if response.status_code == 200:
    # getting data in the json format
        data = response.json()

        # getting the main dict block
        main = data['main']
        # getting temperature
        temperature = main['temp']
        # getting the humidity
        humidity = main['humidity']
        # getting the pressure
        pressure = main['pressure']
        # weather report
 
 
        
        return f""" \n
        {Tunis.name:-^30} \n
        Temperature : {temperature} °C\n
        Humidity : {humidity} %\n
        Pressure : {pressure} hPa\n
  

        
        """
    else:
        # showing the error message
        print("Error in the HTTP request")
