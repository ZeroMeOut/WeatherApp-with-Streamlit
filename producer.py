import requests
import json
from time import sleep
from kafka import KafkaProducer
from json import dumps


with open('data.json') as file:
    data = json.load(file)

lon = data['lat']
lat = data['lon']
apikey = data['api_key']

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                    value_serializer=lambda x: dumps(x).encode('utf-8'))


while True:
    openweathermapResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}')
    producer.send('dataflow', value=openweathermapResponse.text)
    sleep(5)

        
    
