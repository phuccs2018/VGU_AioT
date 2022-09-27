print("Hello AIoT")
import sys
import time
import serial.tools.list_ports
from simple_ai import *
from Adafruit_IO import MQTTClient

AIO_FEED_IDS = ["actuator1", "actuator2", "sensor1", "sensor2", "sensor3", "visiondetector"]
AIO_USERNAME = "khoikieu1608"
AIO_KEY = "aio_ekPX74OCjJMxAhDRrEAFLijildw"

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
    print("Received data from feed_id: " + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

mess = ""
def processData(data):
    data = data.replace("!", "")
    data = data.replace("#", "")
    splitData = data.split(":")
    print(splitData)
    try:
        if splitData[1] == "Sensor1":
            client.publish("sensor1", splitData[2])
        elif splitData[1] == "Sensor2":
            client.publish("sensor2", splitData[2])
        elif splitData[1] == "Sensor3":
            client.publish("sensor3", splitData[2])
        elif splitData[1] == "Actuator1":
            client.publish("actuator1", splitData[2])
        elif splitData[1] == "Actuator2":
            client.publish("actuator2", splitData[2])
    except:
        pass



while True:
    time.sleep(5)
    image_capture()
    ai_result = image_detector()
    client.publish("visiondetector", ai_result)
    pass
