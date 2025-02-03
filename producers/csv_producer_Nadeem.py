from kafka import KafkaProducer
import csv
import time
import json

producer = KafkaProducer(bootstrap_servers='localhost:9092', 
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        producer.send('csv_topic', row)
        print(f"Sent: {row}")
        time.sleep(1)
