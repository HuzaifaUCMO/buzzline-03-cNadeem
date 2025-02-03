from kafka import KafkaProducer
import json
import time

producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

messages = [
    {"message": "Kafka is amazing!", "author": "Huzaifa"},
    {"message": "Streaming data is powerful.", "author": "Bob"},
    {"message": "Real-time processing is the future.", "author": "Alice"}
]

while True:
    for msg in messages:
        producer.send('json_topic', msg)
        print(f"Sent: {msg}")
    time.sleep(2)
