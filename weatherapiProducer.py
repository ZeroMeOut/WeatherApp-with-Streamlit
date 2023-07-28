import requests
import time
import json
from kafka import KafkaProducer
from json import dumps




location = data[0]
lat = location['lat']
lon = location['lon']
API_key = '5bfa7c20f7c28654ffefacc67dbc0913'

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

while True:
    openweathermapResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_key}')
    jsonOpenweathermapResponse = json.loads(openweathermapResponse.text)

    producer.send('dataflow',value= jsonOpenweathermapResponse)
    
    time.sleep(10)


