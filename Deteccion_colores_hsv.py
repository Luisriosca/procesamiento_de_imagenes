# -*- coding: utf-8 -*-
"""
Este código fue dasarrollado por: @LuisriosCode
La finalidad del código es implementarse en analisis de imagenes de 
cupones de corrosión.
Este programa se basa en la utilización de un espacio de color diferente al 
habitual (RGB) utilizamos el espacio de color conocido como HSV porque nos da acceso
a tres diferentes componentes de un color:
    H: Hue (Tono o Matíz de color) - 0 a 179
    S: Saturación - 0 a 255
    V: Value of Brigthness- 0 a 255

Anexo a este código se encuentra un archivo PNG que incluye la grafica de los 
valores de HSV.
"""
import cv2
##import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame =  cap.read()
    if ret == True:
        frameHSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.destroyAllWindows()
            break

cap.realese()
cv2.destroyAllWindows()