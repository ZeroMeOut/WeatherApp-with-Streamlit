import streamlit as st
from json import loads
from kafka import KafkaConsumer, TopicPartition


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
    st.write(message.value)


