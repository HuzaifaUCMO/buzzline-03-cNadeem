from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('csv_topic',
                         bootstrap_servers='localhost:9092',
                         auto_offset_reset='earliest',
                         value_deserializer=lambda v: json.loads(v.decode('utf-8')))

for msg in consumer:
    data = msg.value
    print(f"Received: {data}")
    if float(data['temperature']) > 75:
        print("⚠️ ALERT: High temperature detected!")
