import requests
import json
import pprint 
import time
from datetime import datetime
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps


own = OWM('5bfa7c20f7c28654ffefacc67dbc0913')
mgr = own.weather_manager()
#print(time.tzname[1])

def with_response(location:str):
	observation = mgr.weather_at_place(location)
	w = observation.weather
        
	# device_timezone = time.tzname[0]
	# detailed_status = w.detailed_status
	# wind_speed = w.wind()['speed']
	# wind_deg = w.wind()['deg']
	# humidity = w.humidity
	# temp_max = w.temperature('celsius')['temp_max']
	# temp_min = w.temperature('celsius')['temp_min']
	# temp_curr = w.temperature('celsius')['temp']
	# feels_like = w.temperature('celsius')['feels_like']
	rain = w.rain
	# heat_index = w.heat_index
	# clouds = w.clouds
	
	# data = {
    #         "device_timezone": device_timezone,
    #         "detalited_staus": detailed_status,
    #         "wind_speed": wind_speed,
    #         "wind_deg": wind_deg,
    #         "humidity": humidity,
    #         "temp_curr": temp_curr,
    #         "rain": rain,
    #         "heat_index": heat_index,
    #         "clouds": clouds
	# }
    
	# json_data = json.dumps(data)

	return rain

while True:
    pprint.pprint(with_response('Toronto'))
    time.sleep(10)