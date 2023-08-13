import streamlit as st
from json import loads
from kafka import KafkaConsumer, TopicPartition

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
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset= 'earliest',
    enable_auto_commit=True,
    group_id='my-group',
    value_deserializer=lambda x: loads(x.decode('utf-8')),
    )

partition = TopicPartition('dataflow', 0)
consumer.assign([partition])
end_offset = consumer.end_offsets([partition])
consumer.seek(partition,list(end_offset.values())[0]-1)



for message in consumer: 
    lon, lat, weather, weather_desc, temp, feels_like, temp_min, temp_max, humidity, clouds = data_cleanup(loads(message.value))
    # st.write(lon, lat, weather, weather_desc, temp, feels_like, temp_min, temp_max, humidity, clouds)

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.write(f"longitude: {lon}")
    st.write(f"latitude: {lat}")

with col2:
    st.write(f"weather: {weather}")
    st.write(f"weather description: {weather_desc}")
    
with col3:
    st.write(f"temp: {temp}")
    st.write(f"feels like: {feels_like}")

with col4:
    st.write(f"temp min: {temp_min}")
    st.write(f"temp max: {temp_max}")

with col5:
    st.write(f"humidity: {humidity}")
    st.write(f"clouds: {clouds}")

    



