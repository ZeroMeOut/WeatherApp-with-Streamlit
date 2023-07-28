import json
import requests

class Locator():

    def __init__(self, location):
        self.location = location
    
    def lonlat(self):
        if self.location is None:
            pass
        else:
            geocodeResponse = requests.get(f"https://geocode.maps.co/search?q={self.location}")
            jsonGeocodeResponse = json.loads(geocodeResponse.text)

        list_of_results = []

        for value in jsonGeocodeResponse:
            dict = {'display_name': value['display_name'],
                    'lat': value['lat'],
                    'lon': value['lon']
            }
            
            list_of_results.append(dict)
        return list_of_results