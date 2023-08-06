import requests
import json
from time import sleep
from kafka import KafkaProducer
from json import dumps

def data_cleanup(message):
    lon = message['coord']['lon']
    lat = message['coord']['lat']

    weather = message['weather'][0]['main']
    weather_desc = message['weather'][0]['description']

    temp = message['main']['temp'] - 273.15
    feels_like = message['main']['feels_like'] - 273.15
    temp_min = message['main']['temp_min'] - 273.15
    temp_max = message['main']['temp_max'] - 273.15
    humidity = message['main']['humidity']

    clouds = message['clouds']['all']

    return lon, lat, weather, weather_desc, temp, feels_like, temp_min, temp_max, humidity, clouds



with open('data.json') as file:
    data = json.load(file)

lon = data['lat']
lat = data['lon']
apikey = data['api_key']

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                    value_serializer=lambda x: dumps(x).encode('utf-8'))


while True:
    openweathermapResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={apikey}')
    lon, lat, weather, weather_desc, temp, feels_like, temp_min, temp_max, humidity, clouds = data_cleanup(json.loads(openweathermapResponse.text))

    producer.send('dataflow', value=lon)
    sleep(5)

        
    
