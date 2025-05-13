#!/usr/bin/python3

import paho.mqtt.client as mqtt
import json

# MQTT broker settings
BROKER = '192.168.178.XXX'
PORT = 1883
KEEPALIVE = 60
TOPIC = 'battery'

# Called when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe('zigbee2mqtt/#')

# Called when a message is received
def on_message(client, userdata, msg):
    decoded_message=str(msg.payload.decode("utf-8"))
    topic = msg.topic.replace('zigbee2mqtt/','')
    try:
        message=json.loads(decoded_message)
    except:
        pass
    else:
        message=json.loads(decoded_message)
        if ('battery' in message):
            if (message['battery'] < 50):
                print (topic + " " + 'batterie: ' + str(message['battery']))

        if ('update_available' in message):
            if (message['update_available']):
                print (topic + " update_available: " + str(message['update_available']))

# Create MQTT client and bind callbacks
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(BROKER, PORT, KEEPALIVE)

# Start the loop to process callbacks
client.loop_forever()
