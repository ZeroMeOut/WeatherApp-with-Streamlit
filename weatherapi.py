import requests
import pprint
import json

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

pprint.pprint(cleanResponse(jsonGeocodeResponse))