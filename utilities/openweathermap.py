import requests
import json
from time import sleep
from kafka import KafkaProducer
from json import dumps

class WeatherData:
    
    def __init__(self, location, apikey, lon, lat):
        self.lon = lon
        self.lat = lat
        self.location = location
        self.apikey = apikey
        self.producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: dumps(x).encode('utf-8'))
    
    def send_weather_data(self):
        while True:
            openweathermapResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid={self.apikey}')
            self.producer.send('dataflow', value=openweathermapResponse.text)
            
    
