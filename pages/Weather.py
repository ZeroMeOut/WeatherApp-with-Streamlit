import streamlit as st
from json import loads
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


consumer = KafkaConsumer(
    'dataflow',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset= 'earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')))



for message in consumer:
    
    st.write(message.value)


