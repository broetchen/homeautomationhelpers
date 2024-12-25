#!/usr/bin/python3

import random
import time
import sys

from paho.mqtt import client as mqtt_client


broker = '192.168.XXX.YYY'
port = 1883
topic = "zigbee2mqtt/" + sys.argv[1] + "/set"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
from time import gmtime, strftime
import json
import datetime
import requests
import time




def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
#    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic, value):
    msg_count = 0
    while True:
        time.sleep(1)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1


def run():
  lastrun=1
  client = connect_mqtt()


  client.publish(topic, '{"occupied_heating_setpoint":' + sys.argv[2] +'}' )

if __name__ == '__main__':
    run()
