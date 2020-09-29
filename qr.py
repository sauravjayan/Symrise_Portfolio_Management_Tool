import cv2
import numpy as np
import pyzbar.pyzbar as pyzbar

# img = cv2.imread('test.png')

cap = cv2.VideoCapture(0)


while True:

    success, img = cap.read()
    for code in pyzbar.decode(img):
        decoded_data = code.data.decode('utf-8')
        print(decoded_data)
    

    cv2.imshow('Image:', img)

    cv2.waitKey(1)
    if key == 27:
        break



