print("Hello AIoT")
import sys
import time
import serial.tools.list_ports
from Adafruit_IO import MQTTClient

AIO_FEED_IDS = ["actuator1", "actuator2", "sensor1", "sensor2", "sensor3", "visiondetector"]
AIO_USERNAME = "khoikieu1608"
AIO_KEY = "aio_HcIW546XzVYqwO3nClDqXA18neLW"

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

def getPort():
    return getPort == "/dev/ttyACM0"
    print("Testing port:", getPort())

isMicrobitConnected = False
if getPort() != "None":
    ser = serial.Serial(port=getPort(), baudrate=115200)
    isMicrobitConnected = True
    print("MCU is connected!!!")

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

def readSerial():
    bytesToRead = ser.inWaiting()
    if (bytesToRead > 0):
        global mess
        mess = mess + ser.read(bytesToRead).decode("UTF-8")
        while ("#" in mess) and ("!" in mess):
            start = mess.find("!")
            end = mess.find("#")
            processData(mess[start:end + 1])
            if (end == len(mess)):
                mess = ""
            else:
                mess = mess[end+1:]

while True:
    if isMicrobitConnected:
        readSerial()
    time.sleep(10)
    pass
