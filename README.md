# Reconocimiento Facial

## Metodologia de la investigacion.

Prof, Ing Carlos R. Rodriguez.
Autores: Enzo Pennisi, Pablo Sepulveda, Vanina Luna.

### Introduccion: 

En este proyecto de investigación se busca diseñar e implementar un sistema de autenticación basado en el reconocimiento facial utilizando Python en Linux, con el objetivo de sustituir la contraseña en un proceso de login.
Para esto, se conectará el sistema a una base de datos donde se almacenarán las fotos y datos a comparar. 
La aplicación utiliza la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI) y la biblioteca OpenCV para capturar y procesar imágenes.

### Objetivos generales:

    * Investigar y comprender el funcionamiento del reconocimiento facial, incluyendo técnicas y algoritmos utilizados en el procesamiento de imágenes.
    * Seleccionar y estudiar las herramientas y tecnologías necesarias para el desarrollo del sistema de autenticación basado en reconocimiento facial.
    * Diseñar e implementar un prototipo funcional de autenticación basado en reconocimiento fa-cial, que permita identificar y autenticar a los usuarios utilizando sus características faciales.
    * Evaluar la precisión y la eficacia del sistema propuesto mediante pruebas y análisis de su rendimiento en diferentes condiciones de iluminación, ángulos y variaciones faciales.
    * Integrar el sistema de autenticación con una base de datos relacional SQL para almacenar y gestionar los registros de usuarios de manera eficiente
    * Utilizar técnicas de optimización en la base de datos SQL para mejorar el rendimiento del almacenamiento y la gestión de los registros de usuarios.
    * Facilitar el proceso de registro de nuevos usuarios, proporcionando una interfaz intuitiva y amigable que capture y almacene sus datos faciales en la base de datos.
    * Eliminar la carpeta "Capturas Registro" del proyecto para reducir el tamaño total y mejorar la organización del sistema.
    * Ofrecer opciones para administrar los datos de los usuarios, permitiendo actualizar, eliminar o visualizar la información almacenada en la base de datos.
    * Realizar pruebas exhaustivas del sistema, asegurando su estabilidad, seguridad y usabilidad en entornos reales.

### Marco Teorico:

El proyecto requería el uso del lenguaje de programación Python, del cual no teníamos ningún conocimiento previo. Por lo tanto, se decidió iniciar una investigación sobre las características, posibilidades y aplicaciones de este lenguaje, así como su sintaxis y estructura. El aprendizaje de un nuevo lenguaje en un plazo tan corto fue un desafío que nos generó muchos errores y dificultades. Sin embargo, pudimos contar con el apoyo de algunas personas que poseían un conocimiento básico de Python y que nos orientaron en algunos aspectos fundamentales. Además, recurrimos a diversas fuentes de información en línea, como guías y tutoriales, que nos facilitaron el proceso de aprendizaje y nos permitieron avanzar en el desarrollo del proyecto.

### Funcionalidades:

El programa ofrece las siguientes funcionalidades:

####    Registro:

Al hacer clic en el botón "Registrarse", se abrirá una ventana emergente donde los usuarios pueden ingresar su nombre de usuario y capturar una imagen de su rostro. Para capturar la imagen, se utiliza la cámara web del dispositivo. Después de capturar la imagen, se recorta la sección del rostro detectada utilizando el detector de rostros MTCNN y se guarda en la base de datos. Posteriormente, se muestra un mensaje de éxito en la ventana emergente y se informa al usuario que el registro ha sido exitoso.

####    Inicio de Sesión:

Al hacer clic en el botón "Inicio de Sesión", se abrirá otra ventana emergente donde los usuarios pueden ingresar su nombre de usuario y capturar una imagen de su rostro. Similar al proceso de registro, se captura la imagen y se recorta la sección del rostro utilizando MTCNN. Luego, se compara esta imagen con la imagen de registro previamente guardada para determinar la compatibilidad. Si el grado de compatibilidad supera un umbral predeterminado, se muestra un mensaje de éxito en la ventana emergente y se informa al usuario que ha iniciado sesión correctamente. De lo contrario, se muestra un mensaje de error indicando que la imagen capturada no coincide con la imagen de registro.

####    Mostrar usuarios:

Al hacer clic, permite visualizar todos los usuarios registrados en la base de datos.
Al utilizar esta función, se despliega una lista completa de los usuarios registrados, incluyendo sus nombres y datos relevantes. Esta visualización brinda la posibilidad de administrar los usuarios de manera más eficiente, permitiendo realizar acciones como la edición de información, eliminación de usuarios o simplemente visualizar los detalles asociados a cada uno de ellos.

####    Salir:

Al hacer clic en el botón "Salir", se cierra la aplicación y finaliza la ejecución del programa.

### Requisitos:

El programa requiere las siguientes bibliotecas y componentes:

    * Tkinter: Biblioteca para crear interfaces gráficas de usuario en Python.
    * OpenCV: Biblioteca para el procesamiento de imágenes y la captura de video.
    * MTCNN: Detector de rostros utilizado para detectar y recortar la sección del rostro en las imágenes.
    * Matplotlib: biblioteca de visualización de datos en Python
    * Tensorflow: Es una biblioteca de código abierto para realizar cálculos numéricos utilizando gráficos de flujo de datos.

### Configuración y Ejecución:

Para ejecutar el programa, asegúrese de tener instaladas las bibliotecas mencionadas anteriormente. Luego, guarde el código en un archivo con extensión .py. Asegúrese de tener las imágenes de fondo (f.png) y actualice las rutas de las imágenes en el código para que coincidan con la ubicación de los archivos en su sistema.

Una vez que el código y las imágenes están configurados, puede ejecutar el programa ejecutando el archivo .py. Se abrirá una ventana principal que le permitirá seleccionar la opción de inicio de sesión o registro.

### Conclusión:

Este proyecto de investigación se centró en el diseño e implementación de un sistema de autenticación basado en reconocimiento facial utilizando Python en Linux. El objetivo principal fue reemplazar el uso de contraseñas en el proceso de inicio de sesión, brindando una alternativa más segura y conveniente para los usuarios.

Durante el desarrollo del proyecto, se investigaron y comprendieron los fundamentos del reconocimiento facial, incluyendo técnicas y algoritmos utilizados en el procesamiento de imágenes. Se seleccionaron y estudiaron las herramientas y tecnologías necesarias, como Tkinter para la interfaz gráfica de usuario, OpenCV para la captura y procesamiento de imágenes, y MTCNN para la detección de rostros.

Se logró diseñar e implementar un prototipo funcional que permitía identificar y autenticar a los usuarios utilizando sus características faciales. Se realizaron pruebas exhaustivas para evaluar la precisión y eficacia del sistema en diferentes condiciones de iluminación, ángulos y variaciones faciales.

Además, se integró el sistema de autenticación con una base de datos relacional SQL para almacenar y gestionar los registros de usuarios de manera eficiente. Se utilizaron técnicas de optimización en la base de datos para mejorar el rendimiento del almacenamiento y la gestión de los registros de usuarios.

El proceso de registro de nuevos usuarios se facilitó mediante una interfaz intuitiva y amigable que capturaba y almacenaba sus datos faciales en la base de datos. Se implementaron opciones para administrar los datos de los usuarios, permitiendo actualizar, eliminar o visualizar la información almacenada.

En términos de funcionalidades, el programa ofrecía la capacidad de registro de nuevos usuarios, inicio de sesión basado en reconocimiento facial, visualización de usuarios registrados y salida del programa.

A lo largo del proyecto, se enfrentaron desafíos significativos, como el aprendizaje de Python en un plazo corto de tiempo y la resolución de errores y dificultades asociadas al uso de nuevas tecnologías. Sin embargo, el trabajo en equipo, el apoyo de personas con conocimientos previos y la búsqueda de información en línea fueron recursos clave para superar estos obstáculos y avanzar en el desarrollo del proyecto.

### Instructivo para compilar el proyecto: 

El proyecto se ha desarrollado utilizando la versión de Python que viene instalada por defecto con la versión de Ubuntu 22.04.2 LTS.
Este requiere de una serie de librerías que deben ser instaladas previamente para garantizar su correcto funcionamiento. Estas librerías son: pip, tkinter, opencv, matplotlib, mtcnn y tensorflow. Además, se deben instalar las dependencias necesarias para cada una de estas librerías.
Para facilitar el proceso de instalación, se proporciona un archivo llamado “instalar_librerias.sh” en la carpeta del proyecto, que contiene los comandos para instalar todas las librerías de forma automática. Para ejecutar este archivo, se debe ingresar el siguiente comando en la terminal: ./instalar_librerias.sh
