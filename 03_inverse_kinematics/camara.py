import cv2 as cv2
import time
import numpy as np
"""http://192.168.0.11:5000/video_feed"""
cap = cv2.VideoCapture(0)

def rectangles(frame):
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

def colours(imagen, mask):
    img_masked = cv2.bitwise_and(imagen, imagen, mask=mask)
    cv2.imshow('Mask', img_masked)

    blank_2 = np.zeros(img_masked.shape[:2], dtype='uint8')
    b, g, r = cv2.split(img_masked)

    blue = cv2.merge([b, blank_2, blank_2])
    green = cv2.merge([blank_2, g, blank_2])
    red = cv2.merge([blank_2, blank_2, r])

    return blue, green, red

def rect_color(frame, color): # (0,12,235) (33,152,255)
    img_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    img_copia = frame.copy()
    range = [[np.array([0, 12, 235]), np.array([33, 91, 255])],   #Red
             [np.array([24, 66, 235]), np.array([35, 255, 255])], #Yellow
             [np.array([37, 0, 235]), np.array([91, 153, 255])]]  #Azul

    color_rect = [(0, 0, 255), (0, 255, 255), (255, 0, 0)]
    blur = cv2.GaussianBlur(img_hsv, (3, 3), cv2.BORDER_DEFAULT)

    if color == 'red':
        mask = cv2.inRange(blur, range[0][0], range[0][1])

        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if 5 < w < 20 and 5 < h < 20:
                cv2.rectangle(img_copia, (x, y), (x + w, y + h), color_rect[0], 2)

    if color == 'yellow':
        mask = cv2.inRange(blur, range[1][0], range[1][1])

        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if 5 < w < 20 and 5 < h < 20:
                cv2.rectangle(img_copia, (x, y), (x + w, y + h), color_rect[1], 2)

    if color == 'blue':
        mask = cv2.inRange(img_hsv, range[2][0], range[2][1])
        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if 10 < w < 20 and 10 < h < 20:
                cv2.rectangle(img_copia, (x, y), (x + w, y + h), color_rect[2], 2)

    return img_copia

def rect_color_all(frame):
    return rect_color(rect_color(rect_color(frame, 'red'), 'yellow'), 'blue')

def cut(frame):
    img_copia = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
    blank = cv2.cvtColor(np.zeros(frame.shape[:2], dtype='uint8'), cv2.COLOR_GRAY2BGR)
    mask_rojo = cv2.inRange(img_copia, np.array([0, 255, 255]), np.array([0, 255, 255])) #recorte rojo
    mask_amarillo = cv2.inRange(img_copia, np.array([30, 255, 255]), np.array([30, 255, 255]))
    mask_azul = cv2.inRange(img_copia, np.array([120, 255, 255]), np.array([135, 255, 255]))

    mascaras = [mask_rojo, mask_amarillo, mask_azul]

    x0, y0, x1, y1 = frame.shape[0], frame.shape[1], 0, 0
    for mask in mascaras:
        contours, hierarchies = cv2.findContours(mask, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)
            if x < x0:
                x0 = x
            if y < y0:
                y0 = y
            if x + w > x1:
                x1 = x + w
            if y + h > y1:
                y1 = y + h
    blank[y0:y1, x0:x1] = frame[y0:y1, x0:x1]

    return blank

def center_button(frame, color):
    img_copia = cv2.cvtColor(frame.copy(), cv2.COLOR_BGR2HSV)
    button = []
    x, y, w, h = 0, 0, 0, 0

    mask_button = mask_rojo = cv2.inRange(img_copia, np.array([0, 255, 255]), np.array([0, 255, 255]))
    contours, hierarchies = cv2.findContours(mask_rojo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contorno in contours:
        xb, yb, wb, hb = cv2.boundingRect(contorno)
        if w < 10 and h < 20:
            button.append([xb, yb, xb+wb, yb+hb])

    if color == 'red':
        mask_rojo = cv2.inRange(img_copia, np.array([0, 255, 255]), np.array([0, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_rojo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        if hierarchies != []:
            return [(2*button[0][1] + button[0][4])/2, 3*(xb+xb+w)/4]

    if color == 'yellow':
        mask_amarillo = cv2.inRange(img_copia, np.array([30, 255, 255]), np.array([30, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_amarillo, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)

    if color == 'blue':
        mask_azul = cv2.inRange(img_copia, np.array([120, 255, 255]), np.array([135, 255, 255]))
        contours, hierarchies = cv2.findContours(mask_azul, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

        for contorno in contours:
            x, y, w, h = cv2.boundingRect(contorno)

    return [(y+y+h)/2, (x+x+w)/2]

def matrix_conversion(vector):
    return [2*vector[0], 2*vector[1]]

def take_frame():
    i = 0
    while i<2:
        ret, frame = cap.read()
        cv2.imwrite('my_video_frame123.png', frame)
        i += 1

def find_vector(frame, color):
    frame = cv2.imread('my_video_frame123.png')
    vector = matrix_conversion(center_button(rect_color(frame, color), color))

    return vector