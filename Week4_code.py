import sys
import time
import  random
from Adafruit_IO import MQTTClient
from physical_week4 import *
import time


AIO_FEED_IDS = ["sensor1", 'sensor2','switch','actuator1','actuator2']
AIO_USERNAME = "chosang2000vn"
AIO_KEY = 'aio_Blnx27Syj3JfZvvQkak5VxbUvSP1'

def connected(client):
    print("Connect Successfully ...")
    for feed in AIO_FEED_IDS:
        client.subscribe(feed)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribed  ...")

def disconnected(client):
    print("Disconnected ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Received Message: " + payload)
    state = True if (str(payload) == "1") else False
    if feed_id == "actuator1":
        setDevice1(state)
    if feed_id == 'actuator2':
        setDevice2(state)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
while True:
    temp = readTemperature()
    mois = readMoistrure()
    client.publish("sensor1", temp)
    client.publish("sensor2", mois)
    time.sleep(5)
    pass





