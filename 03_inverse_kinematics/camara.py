import cv2 as cv2
import matplotlib.pyplot as plt
import numpy as np
"""http://192.168.0.11:5000/video_feed"""
cap = cv2.VideoCapture(0)



while(True):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array([0,46,104])
    higher = np.array([5,255,189])
    mask = cv2.inRange(img_hsv, lower, higher)


    kernel = np.ones((5,5),np.uint8)
    mask_erode = cv2.erode(mask, kernel, iterations = 1)
    mask_dila = cv2.dilate(mask, kernel, iterations = 1)
    mask_gauss = cv2.GaussianBlur(mask_dila,(5,5),0)

    contours, hierarchy = cv2.findContours(mask_gauss, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contours:
        x, y, w, h = cv2.boundingRect(contorno)
        rectangulo = cv2.rectangle(mask, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow('camara',frame)
    cv2.imshow('mascara', mask)

cap.release()
cv2.destroyAllWindows()