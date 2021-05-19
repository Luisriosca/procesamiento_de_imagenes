# -*- coding: utf-8 -*-
"""
Created on Sun May 16 20:47:26 2021

@author: weexo - @Luisrioscode

Este código describe como utilizar imagenes en python y openCV.
Este código es para usarse en combinación con segmentación HSV.


"""
import cv2
import numpy as np

imagen = cv2.imread('cupon.png', 0)
cv2.imshow('Prueba de imagen', imagen)
cv2.imwrite('grises.png', imagen)
cv2.waitKey(10000)
cv2.destroyAllWindows()