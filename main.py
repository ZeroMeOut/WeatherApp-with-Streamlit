from kafka import KafkaConsumer
from json import loads
import pprint

consumer = KafkaConsumer(
    'dataflow',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
     value_deserializer=lambda x: loads(x.decode('utf-8')))

def data_cleanup(message):
    lon = message['coord']['lon']
    lat = message['coord']['lat']

for message in consumer:
    message = message.value
    pprint.pprint(message)