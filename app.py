import streamlit as st

import requests
import json
from time import sleep
from kafka import KafkaProducer
from json import dumps
from json import loads
from utilities import locator, openweathermap
from kafka import KafkaConsumer


# Cleans up data from the consumer
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

# For Binary Search, this part doesn,t work well for some reason
def binary_search(list_of_dicts, key, target):
    low = 0
    high = len(list_of_dicts) - 1

    while low <= high:
        mid = (low + high) // 2
        current_dict = list_of_dicts[mid]

        if target == current_dict.get(key):
            return current_dict
        elif target < current_dict.get(key):
            high = mid - 1
        else:
            low = mid + 1

    return None


st.title('Weather Locator')

api_key = st.text_input('API Key', value = "5bfa7c20f7c28654ffefacc67dbc0913")
user_input = st.text_input('Input location')

locator = locator.Locator(user_input)
locations = locator.lonlat()

display_names = [location['display_name'] for location in locations]

target = st.selectbox(
    'Select a location',
    display_names
)


selected_location = binary_search(locations, 'display_name', target)

if selected_location is not None:
    lat = selected_location['lat']
    lon = selected_location['lon']

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                      value_serializer=lambda x: dumps(x).encode('utf-8'))
    
    while True:
            openweathermapResponse = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}')
            jsonOpenweathermapResponse = json.loads(openweathermapResponse.text)

            producer.send('dataflow', value=jsonOpenweathermapResponse)
            producer.flush()


if selected_location is not None:
    if 'consumer' not in st.session_state:
        st.session_state['consumer'] = []

    consumer = KafkaConsumer(
        'dataflow',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        response = message.value
        st.session_state['consumer'].append(response)
        st.write(st.session_state['consumer'])


    