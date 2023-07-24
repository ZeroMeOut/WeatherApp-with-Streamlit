import requests
import pprint
import json
import time

# Getting Geo Location, longitude and latitude
address = "London"
geocodeResponse = requests.get(f"https://geocode.maps.co/search?q={address}")
geocodeResponse.raise_for_status()
# print(response.status_code)

jsonGeocodeResponse = json.loads(geocodeResponse.text)

def cleanResponse(response: list):
    list_of_results = []

    for value in response:
        dict = {'display_name': value['display_name'],
                'lat': value['lat'],
                'lon': value['lon']
        }
        
        list_of_results.append(dict)
    return list_of_results

data = cleanResponse(jsonGeocodeResponse)

location = data[0]
lat = location['lat']
lon = location['lon']
API_key = '5bfa7c20f7c28654ffefacc67dbc0913'

while True:
    openweathermapResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
    jsonOpenweathermapResponse = json.loads(openweathermapResponse.text)

    pprint.pprint(jsonOpenweathermapResponse)

    time.sleep(10)

