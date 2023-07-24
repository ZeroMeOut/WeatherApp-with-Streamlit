import requests
import pprint
import json

address = "London"
response = requests.get(f"https://geocode.maps.co/search?q={address}")
response.raise_for_status()
print(response.status_code)

jsonData = json.loads(response.text)
pprint.pprint(jsonData)

