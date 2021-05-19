# -*- coding: utf-8 -*-
"""
Created on Tue May 18 22:38:24 2021
Programa de graficación del histograma para los valores de brillo, y los tres calares de color BRG.
Este programa está desarrollado para usarse en conjunto con la detección de color por HSV y posteriormente con 
un software de analisis metalurgico.
@author: weexo @luisrioscode


"""

import cv2
import numpy as np
from matplotlib import pyplot as plt

imagen = cv2.imread('cuponz1x.jpg')
imagenBN = cv2.imread('cupon.png', 0)

histograma  = cv2.calcHist([imagenBN], [0], None, [256], [0, 256])
histogramaAzul  = cv2.calcHist([imagen], [0], None, [256], [0, 256])
histogramaVerde = cv2.calcHist([imagen], [1], None, [256], [0, 256])
histogramaRojo  = cv2.calcHist([imagen], [2], None, [256], [0, 256])


plt.plot(histograma, color = 'gray' )
plt.xlabel('El mero brillo alv')
plt.ylabel('No. de Pixeles')
plt.show()

plt.plot(histogramaAzul, color = 'blue' )
plt.xlabel('Azul')
plt.ylabel('No. de Pixeles')
plt.show()

plt.plot(histogramaVerde, color = 'green' )
plt.xlabel('Verde')
plt.ylabel('No. de Pixeles')
plt.show()

plt.plot(histogramaRojo, color = 'red' )
plt.xlabel('Rojo')
plt.ylabel('No. de Pixeles')
plt.show()

while True:
    cv2.imshow('CUPON DE CORROSIÓN', imagen)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.destroyAllWindows()
        break


cv2.destroyAllWindows()