import cv2 as cv2
import numpy as np
import time
"""http://192.168.0.13:5000/video_feed"""
def take_frame(inter):

    cap = cv2.VideoCapture('http://192.168.0.13:5000/video_feed')
    ret, frame = cap.read()
    i = 0
    while i == 0:
        cv2.imshow('lol', frame)
        cv2.imwrite('fotos/my_video_frame{}.png'.format(inter), frame)
        i = 1
        time.sleep(3)
    print('a')


def rect_color(frame, color):  #Red, Yellow, Blue
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_copia = frame.copy()
    range_colors = [[np.array([98, 0, 255]), np.array([179, 255, 255])],
                    [np.array([8, 0, 255]), np.array([82, 255, 255])],
                    [np.array([86, 0, 255]), np.array([103, 255, 255])]]

    color_rect = [(0, 0, 255), (0, 255, 255), (255, 0, 0)]

    if color == 'red':
        mask = cv2.inRange(img_hsv, range_colors[0][0], range_colors[0][1])

        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if 2 < w and 2 < h:
                cv2.rectangle(img_copia, (x, y), (x + w, y + h), color_rect[0], 2)

    if color == 'yellow':
        mask = cv2.inRange(img_hsv, range_colors[1][0], range_colors[1][1])

        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if 1 < w and 1 < h:
                cv2.rectangle(img_copia, (x, y), (x + w, y + h), color_rect[1], 2)

    if color == 'blue':
        mask = cv2.inRange(img_hsv, range_colors[2][0], range_colors[2][1])

        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if 2 < w and 1 < h:
                cv2.rectangle(img_copia, (x, y), (x + w, y + h), color_rect[2], 2)

    return img_copia


def center_button(frame, color):
    img_copia = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
    button = [(170, 105),  #Rojo
              (165, -115),  #Amarillo
              (185, 0)]  #Azul
    if color == 'red':
        mask_rojo = cv2.inRange(img_copia, np.array([0, 255, 255]), np.array([0, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_rojo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if str(type(hierarchies)) != "<class 'NoneType'>":
            return button[0]

    elif color == 'yellow':
        mask_amarillo = cv2.inRange(img_copia, np.array([30, 255, 255]), np.array([30, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_amarillo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if str(type(hierarchies)) != "<class 'NoneType'>":
            return button[1]

    elif color == 'blue':
        mask_azul = cv2.inRange(img_copia, np.array([120, 255, 255]), np.array([135, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_azul, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        print(hierarchies)

        if str(type(hierarchies)) != "<class 'NoneType'>":
            return button[2]

    return 0, 0


def find_vector(frame, color):
    vector = center_button(rect_color(frame, color), color)

    return vector
