import asyncio
import paho.mqtt.client as mqtt
from services.telemetry_service import telemetry_service

MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "uav/telemetry"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    asyncio.run(telemetry_service.broadcast(payload))

def start_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(MQTT_BROKER, MQTT_PORT, 60)
    client.loop_forever()
