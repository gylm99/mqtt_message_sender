import json
import time

import pandas as pd
import paho.mqtt.client as mqtt
from datetime import datetime

from paho.mqtt.client import Client

#itt kell megadni az mqtt kapcsolathoz szükséges adatokat
broker_url = "38.242.204.225"
broker_port = 1883
user_name="treestar"
password="t4Yx8:a/21x~5CaMX0T9dyKE>"
client=mqtt.Client(protocol=mqtt.MQTTv311)
client.username_pw_set(user_name,password)

client.connect(broker_url,broker_port,60,)

#Kapcsolat ellenőrzése
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
#Elküldött üzenet számláló
def on_publish(client, userdata, mid):
    print(f"Message {mid} published.")

client.on_connect = on_connect
client.on_publish = on_publish

try:
    client.connect(broker_url, broker_port, 60)
    client.loop_start()
except Exception as e:
    print(f"Connection failed: {e}")

#külső kijelzőre való mqtt üzenet küldése
def external_display(data:dict):
    external_display_topic = "realcity/drive-onboard/external-display/v1"
    client.publish(topic=external_display_topic, payload=json.dumps(data), qos=1, retain=True)

#belső kijelzőre való mqtt üzenet küldése
def internal_display(data:dict):
    internal_display_topic = "realcity/drive-onboard/internal-display/v1"
    client.publish(topic=internal_display_topic, payload=json.dumps(data), qos=1, retain=True)

#validátorra való mqtt üzenet küldése
def validator(data:dict):
    validator_topic="realcity/drive-onboard/validator-trip-status/v1"
    client.publish(topic=validator_topic, payload=json.dumps(data), qos=1, retain=True)





