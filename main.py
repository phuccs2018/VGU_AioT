import sys
from Adafruit_IO import MQTTClient
from MachineLearningModel import *
import random
import time




AIO_FEED_ID = ["humidity", "button", "humidity-graph","tem","tem-graph","facedetector"] # tên feed trong dashboard
AIO_USERNAME = "FBIWarning" # tên tài khoản của bạn
AIO_KEY = "aio_wEpl55p3OB14sTzbOEROukWrzAJY" # Mã key của dashboard
TIME = 2

#Hàm Kết nối
def connected(client):
    print(f"Kết nối thành công ...")
    for feed in AIO_FEED_ID:
        print(f"Chạy {feed}")
        client.subscribe(feed)

#Hàm Thông báo
def subscribe(client, userdata, mid, granted_qos):
    # Biến mid sẽ cho giá trị từ 1 đến index cuối của cái list AIO_FEED_ID
    print(f"Subcribe {AIO_FEED_ID[mid-1]} thành công ... ")

#Ngắt kết nối
def disconnected(client):
    print("Ngắt kết nối ...")
    sys.exit(1)

#Những hàm thông báo sẽ được gửi tin nhắn
# payload: hàm dùng để nhận giá trị từ adafruit.io
# feed_id: tên của feed tương ứng
def message(client, feed_id, payload):
    print(f"Nhận dữ liệu : {payload} từ {feed_id}")

# Chạy chương trình
client = MQTTClient(AIO_USERNAME, AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

#Tạo hàm loop để đảm bảo chương trình vẫn đang hoạt động
while True:
    time.sleep(5)
    image_capture()
    ai_result = image_detector()
    client.publish("facedetector", f"Name: {ai_result[0]} , Result: {ai_result[1]} %")
    pass