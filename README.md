# Procesamiento de imagenes con OpenCv en Python
Algunos algoritmos de procesamiento de imágenes con OpenCv en Python
La mayoría de estas implementaciones son básicas para el uso en conjunto.

## Comencemos 📸 


## Construido con 🛠️

* [Python 3](https://www.python.org/downloads/) - Un lenguaje programación muy sencillo pero muy poderoso.
* [OpenCV](https://maven.apache.org/) - La librería para el manejo y procesamiento de imagenes y video más famosa del mundo (disponible para varios lenguajes). 
* [Muchas ganas](https://twitter.com/Luis_riosca) - Sígueme en twitter. 

### Cargar Imagenes
El primer código de esta sección contiene la estructura básica para poder cargar una imagen utilizando OpenCv y Python.

### Detección de colores HSV
Este segundo código sirve para poder binarizar una imagen con la finalidad de utilizar como mascara los pixeles que presenten cierto tono de color en ellos, este algoritmo usa como punto de partida el campo de color HSV (tono, saturación y el brillo), en lugar del que se usa por defecto (BGR) para poder realizar la umbralización.
Una vez identificado el color que queremos detectar en una imagen tenermos que seleccionar los valores correspondientes al tono de color y pasarle unos valores base para la saturación y el brillo, casi siempre 100 y 20 para el valor minimo y 255 y 255 para el valor máximo, para determinar los valores del tono se utiliza la siguiente imagen:

![Hue values](https://user-images.githubusercontent.com/30400404/120573466-3dfe4a80-c3e3-11eb-9a3f-1b5e278845c6.png)

Para poder modificar el código y detectar otros colores aparte del rojo se deben de modificar estas siguientes lineas:


```py
#Deteccion_de_colores_camara/imagen

  vRojoBajo  = np.array([0, 100, 20], np.uint8)
  vRojoAlto  = np.array([30, 255, 255], np.uint8)
  v2RojoBajo = np.array([175, 100, 20], np.uint8)
  v2RojoAlto = np.array([179, 255, 255], np.uint8)

```
Para detectar el color rojo se escriben dos rangos de valores para el tono de color, ya que el color rojo se encuentra al final y al principio de nuestra grafica de tonos, brillo y saturación, si deseas detectar un color diferente puedes comentar la tercera y cuarta linea de los umbrales:

```py
#Deteccion_de_colores_camara/imagen

  vBajo  = np.array([0, 100, 20], np.uint8)
  vAlto  = np.array([30, 255, 255], np.uint8)
  #v2RojoBajo = np.array([175, 100, 20], np.uint8)
  #v2RojoAlto = np.array([179, 255, 255], np.uint8)

```
y más abajo dentro del <b>while</b> también comentamos la variable mascara que fusiona las dos mascaras del color rojo.

```py
  mascaraRojo1 = cv2.inRange(frameHSV, vRojoBajo, vRojoAlto)
  #mascaraRojo2 = cv2.inRange(frameHSV, v2RojoBajo, v2RojoAlto)
  #mascara = cv2.add(mascaraRojo1,mascaraRojo2)
```
Una vez determinada la mascara se ocupa la función siguiente para poder generar un recorte de las zonas "enmascaradas".

```py
  mascaraRojaVis =  cv2.bitwise_and(imagen, imagen, mask = mascara)
```
