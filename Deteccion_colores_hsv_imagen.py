# -*- coding: utf-8 -*-
"""
Created on Sun May 16 21:05:31 2021

@author: Luisriosca
"""

import cv2
import numpy as np
imagen = cv2.imread('cupon.png')

#El valor de tono o Hue es geometricamente un cono
vRojoBajo  = np.array([0, 100, 20], np.uint8)
vRojoAlto  = np.array([30, 255, 255], np.uint8)
v2RojoBajo = np.array([175, 100, 20], np.uint8)
v2RojoAlto = np.array([179, 255, 255], np.uint8)

while True:
    frameHSV = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)
    mascaraRojo1 = cv2.inRange(frameHSV, vRojoBajo, vRojoAlto)
    mascaraRojo2 = cv2.inRange(frameHSV, v2RojoBajo, v2RojoAlto)
    mascara = cv2.add(mascaraRojo1,mascaraRojo2)
    mascaraRojaVis =  cv2.bitwise_and(imagen, imagen, mask = mascara)
    cv2.imshow('Frame', imagen)
    cv2.imshow('Mascara normal', mascara)
    cv2.imshow('Mascara roja', mascaraRojaVis)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break

cv2.destroyAllWindows()
