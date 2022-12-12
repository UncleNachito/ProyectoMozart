import cv2 as cv2
import time
import numpy as np
"""http://192.168.0.11:5000/video_feed"""
cap = cv2.VideoCapture(0)

def rectangulos(frame):
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_copia = frame.copy()

    blur = cv2.GaussianBlur(img_gray, (3, 3), cv2.BORDER_DEFAULT)

    ret, thresh = cv2.threshold(blur, 200, 255, cv2.THRESH_BINARY)  # 180, 255

    contours, hierarchies = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contours:
        x, y, w, h = cv2.boundingRect(contorno)
        if w < 60 and h < 60:
            cv2.rectangle(img_copia, (x, y), (x + w, y + h), (255, 0, 0), 2)

    return img_copia


def colores(imagen, mask):
    img_masked = cv2.bitwise_and(imagen, imagen, mask=mask)
    cv2.imshow('Mask', img_masked)

    blank_2 = np.zeros(img_masked.shape[:2], dtype='uint8')
    b, g, r = cv2.split(img_masked)

    blue = cv2.merge([b, blank_2, blank_2])
    green = cv2.merge([blank_2, g, blank_2])
    red = cv2.merge([blank_2, blank_2, r])

    return blue, green, red

def amarillo(frame): # (0,12,235) (33,152,255)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, np.array([30, 12, 233]), np.array([40, 255, 255]))

    contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contours:
        x, y, w, h = cv2.boundingRect(contorno)
        if w < 5 or h < 5:
            cv2.rectangle(mask, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return mask



while(True):
    ret, frame = cap.read()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    if cv2.waitKey(1) & 0xFF == ord('p'):
        cv2.imwrite('my_video_frame.png', frame)

    img_yel = amarillo(frame)
    img_rect = rectangulos(frame)

    (blue, green, red) = cv2.split(frame)






    """cv2.imshow('camara',frame)"""
    cv2.imshow('Rectangulo', img_rect)
    cv2.imshow('Yellow', img_yel)
    """cv2.imshow('Greeb', green)
    cv2.imshow('mascara', mask)"""

cap.release()
cv2.destroyAllWindows()