from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import cv2
from USBport import *


cam = cv2.VideoCapture(0)
import time


# Load the model
model = load_model('keras_model.h5')


def image_capture():
   ret,frame = cam.read()
   cv2.imwrite ("test.png",frame)

def image_detector():

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1.
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    # Replace this with the path to your image
    image = Image.open('test.png')
    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)
    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    print(f"preditction result: {prediction[0]}")

    #print(f"model:  {model}")
    #print(f"image_array: {image_array}")

    output = prediction[0]
    #assign default value for max confidence
    max_index = 0
    max_confidence = output[0]
    #print(f"output = {output}")
    #find the maximum confidence and its index
    for i in range(1, len(output)):
        if max_confidence < output[i]:
            max_confidence = output[i]
            max_index = i
    #print(max_index, max_confidence)


    file = open("labels.txt",encoding="utf8")
    data = file.read().split("\n")
    #0: Organic
    #1: Inorganic
    #print(f"data: {data}")
    #print(f"data[0]: {data[0]}")


    #print(f"Name of the max output: {data[max_index]}")
    #print (f"Max out put: {max_confidence * 100} %")

    return [data, output]