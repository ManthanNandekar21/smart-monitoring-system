# ai_service.py
# This file acts as the AI Analyzer Service.

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'sensor-data',
    bootstrap_servers='localhost:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("AI Service Started...")

for message in consumer:

    data = message.value

    temperature = data['temperature']

    print("Received:", data)

    # AI Logic
    if temperature > 70:
        print("ALERT! High Temperature Detected")
    else:
        print("Temperature Normal")