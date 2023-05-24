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