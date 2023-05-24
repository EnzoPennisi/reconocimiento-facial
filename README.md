# Reconocimiento Facial

## Metodologia de la investigacion.

Prof, Ing Carlos R. Rodriguez.
Autores: Enzo Pennisi, Pablo Sepulveda, Vanina Luna.

### Introduccion: 

En este proyecto de investigación se busca diseñar e implementar un sistema de autenticación basado en el reconocimiento facial utilizando Python en Linux, con el objetivo de sustituir la contraseña en un proceso de login.
Para esto, se conectará el sistema a una base de datos donde se almacenarán las fotos y datos a comparar. 
La aplicación utiliza la biblioteca Tkinter para crear una interfaz gráfica de usuario (GUI) y la biblioteca OpenCV para capturar y procesar imágenes.

### Objetivos generales:

    * Investigar y comprender el funcionamiento del reconocimiento facial.
    * Seleccionar y estudiar lo necesario para el desarrollo del proyecto.
    * Diseñar e implementar un prototipo de autenticación basado en reconocimiento facial.
    * Evaluar la precisión y la eficacia del sistema propuesto.
    * Integrar el sistema con una base de datos

### Objetivos a futuro:

    * Incorporar una base de datos relacional SQL que permita optimizar el almacenamiento y la gestión de los registros de usuarios.
    * Facilitar el proceso de registro.
    * Eliminar la carpeta “Capturas Registro”, para reducir el tamaño total del proyecto.
    * Ofrecer opciones para administrar los datos de los usuarios.

### Marco Teorico:

El proyecto requería el uso del lenguaje de programación Python, del cual no teníamos ningún conocimiento previo. Por lo tanto, se decidió iniciar una investigación sobre las características, posibilidades y aplicaciones de este lenguaje, así como su sintaxis y estructura. El aprendizaje de un nuevo lenguaje en un plazo tan corto fue un desafío que nos generó muchos errores y dificultades. Sin embargo, pudimos contar con el apoyo de algunas personas que poseían un conocimiento básico de Python y que nos orientaron en algunos aspectos fundamentales. Además, recurrimos a diversas fuentes de información en línea, como guías y tutoriales, que nos facilitaron el proceso de aprendizaje y nos permitieron avanzar en el desarrollo del proyecto.

### Funcionalidades:

El programa ofrece las siguientes funcionalidades:

####    Registro:
Al hacer clic en el botón "Registrarse", se abrirá una ventana emergente donde los usuarios pueden ingresar su nombre de usuario y capturar una imagen de su rostro. Para capturar la imagen, se utiliza la cámara web del dispositivo. Después de capturar la imagen, se recorta la sección del rostro detectada utilizando el detector de rostros MTCNN y se guarda en una carpeta llamada "Capturas Registro". Posteriormente, se muestra un mensaje de éxito en la ventana emergente y se informa al usuario que el registro ha sido exitoso.

####    Inicio de Sesión:
Al hacer clic en el botón "Inicio de Sesión", se abrirá otra ventana emergente donde los usuarios pueden ingresar su nombre de usuario y capturar una imagen de su rostro. Similar al proceso de registro, se captura la imagen y se recorta la sección del rostro utilizando MTCNN. Luego, se compara esta imagen con la imagen de registro previamente guardada para determinar la compatibilidad. Si el grado de compatibilidad supera un umbral predeterminado, se muestra un mensaje de éxito en la ventana emergente y se informa al usuario que ha iniciado sesión correctamente. De lo contrario, se muestra un mensaje de error indicando que la imagen capturada no coincide con la imagen de registro.

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

### Conclusión (parcial):

Este proyecto de investigación se ha centrado en el desarrollo y aplicación de un sistema de autenticación que usa reconocimiento facial con Python en Linux. Mediante el uso de bibliotecas como Tkinter y OpenCV, se consiguió crear un prototipo funcional que permite a los usuarios registrarse y acceder al sistema usando imágenes faciales en vez de contraseñas.

A lo largo del desarrollo del proyecto, se exploraron y entendieron los principios del reconocimiento facial, se escogieron y analizaron los componentes necesarios para su aplicación, y se logró diseñar e implementar un sistema capaz de capturar, procesar y comparar imágenes faciales para autenticar a los usuarios.

La evaluación de la exactitud y eficiencia del sistema propuesto mostró resultados prometedores, aunque es importante tener en cuenta que todavía hay retos y oportunidades de mejora. En ese sentido, se plantearon objetivos a futuro, como la incorporación de una base de datos relacional SQL para optimizar el almacenamiento y gestión de registros de usuarios, la simplificación del proceso de registro, la reducción del tamaño del proyecto eliminando la carpeta de capturas de registro y la implementación de opciones para administrar los datos de los usuarios.

En suma, este proyecto ha establecido las bases para la aplicación de un sistema de autenticación que usa reconocimiento facial, ofreciendo una alternativa segura y conveniente a las contraseñas tradicionales. Con mejoras y refinamientos adicionales, este sistema tiene el potencial de ser una solución efectiva y confiable en entornos de autenticación.

### Instructivo para compilar el proyecto: 

El proyecto se ha desarrollado utilizando la versión de Python que viene instalada por defecto con la versión de Ubuntu 22.04.2 LTS.
Este requiere de una serie de librerías que deben ser instaladas previamente para garantizar su correcto funcionamiento. Estas librerías son: pip, tkinter, opencv, matplotlib, mtcnn y tensorflow. Además, se deben instalar las dependencias necesarias para cada una de estas librerías.
Para facilitar el proceso de instalación, se proporciona un archivo llamado “instalar_librerias.sh” en la carpeta del proyecto, que contiene los comandos para instalar todas las librerías de forma automática. Para ejecutar este archivo, se debe ingresar el siguiente comando en la terminal: ./instalar_librerias.sh

### Notas
Este proyecto se encuentra en desarrollo y puede estar sujeto a cambios y mejoras adicionales.