# Procesamiento de imagenes con OpenCv en Python
Algunos algoritmos de procesamiento de imágenes con OpenCv en Python
La mayoría de estas implementaciones son básicas para el uso en conjunto.

## Comencemos 📸 


## Construido con 🛠️

* [Python 3](https://www.python.org/downloads/) - Un lenguaje programación muy sencillo pero muy poderoso.
* [OpenCV](https://maven.apache.org/) - La librería para el manejo y procesamiento de imagenes y video más famosa del mundo (disponible para varios lenguajes). 
* [Muchas ganas](https://twitter.com/Luis_riosca) - Echale ganas y sígueme en twitter. 

### Cargar Imagenes
El primer código de esta sección contiene la estructura básica para poder cargar una imagen utilizando OpenCv y Python.

### Detección de colores HSV
Este segundo código sirve para poder binarizar una imagen con la finalidad de utilizar como mascara los pixeles que presenten cierto tono de color en ellos, este algoritmo usa como punto de partida el campo de color HSV (tono, saturación y el brillo), en lugar del que se usa por defector que es BGR para poder realizar la umbralización, para poder seleccionar los valores correspondientes a cada tono de color se utiliza la siguiente imagen:

![Hue values](https://user-images.githubusercontent.com/30400404/120573466-3dfe4a80-c3e3-11eb-9a3f-1b5e278845c6.png)

Para poder modificar el código y detectar otros colores se deben de modificar estas siguientes lineas:

```
vRojoBajo  = np.array([0, 100, 20], np.uint8)
vRojoAlto  = np.array([30, 255, 255], np.uint8)
v2RojoBajo = np.array([175, 100, 20], np.uint8)
v2RojoAlto = np.array([179, 255, 255], np.uint8)

```


