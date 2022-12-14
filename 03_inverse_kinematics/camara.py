import cv2 as cv2
import numpy as np
"""http://192.168.0.13:5000/video_feed"""
cap = cv2.VideoCapture('http://192.168.0.13:5000/video_feed')


def take_frame():
    i = 0
    while i < 2:
        ret, frame = cap.read()
        cv2.imwrite('my_video_frame1234.png', frame)
        i += 1


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


def rect_button(frame):
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_copia = frame.copy()

    mask = cv2.inRange(img_hsv, np.array([24, 31, 0]), np.array([58, 89, 185]))

    contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for contorno in contours:
        x, y, w, h = cv2.boundingRect(contorno)
        if 10 < w < 15 and 15 < h < 40:
            cv2.rectangle(img_copia, (x, y), (x + w, y + h), (255, 0, 255), 2)

    return img_copia


def center_button2(frame, color):
    img_copia = frame.copy()
    img_led = cv2.cvtColor(rect_color(frame, color), cv2.COLOR_BGR2HSV)
    img_button = cv2.cvtColor(rect_button(frame), cv2.COLOR_BGR2HSV)

    cv2.imshow('lol', img_button)

    mask_button = cv2.inRange(img_button, np.array([149, 255, 255]), np.array([150, 255, 255]))
    contours_b, hierarchies_b = cv2.findContours(mask_button, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if color == 'red':
        mask_rojo = cv2.inRange(img_led, np.array([0, 255, 255]), np.array([0, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_rojo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if str(type(hierarchies)) != "<class 'NoneType'>":
            x, y, w, h = cv2.boundingRect(contours_b[1])
            return

    elif color == 'yellow':
        mask_amarillo = cv2.inRange(img_led, np.array([30, 255, 255]), np.array([30, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_amarillo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if str(type(hierarchies)) != "<class 'NoneType'>":
            return

    elif color \
            == 'blue':
        mask_azul = cv2.inRange(img_led, np.array([120, 255, 255]), np.array([135, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_azul, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if str(type(hierarchies)) != "<class 'NoneType'>":
            return

    return 0, 0


def lol(frame):

    cv2.imwrite('my_video_frame12345.png', rect_color(frame, 'blue'))

"""take_frame()
lol(cv2.imread('my_video_frame1234.png'))"""