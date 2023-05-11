#-------Importar librerias -------

from tkinter import *
from tkinter import messagebox as msg
import os
from tkinter import ttk





# -------Configuracion colores y letra-------
path = os.getcwd() + "/"

txt_ingreso = "Inicio de Sesión"
txt_registro = "Cual sera tu eleccion"

color_blanco = "#f4f5f4"
color_negro = "#101010"
color_verde = "#42FF00"

color_negro_btn = "#202020"
color_background = "#ADA7A7"

font_label = "Calibri"
size_screen = "1000x1000"

# colores consola
color_exito = "\033[1;32;40m"
color_error = "\033[1;31;40m"
color_normal = "\033[0;37;40m"




root = Tk()

root.geometry(size_screen)
root.title("Reconocimiento Facial")
root.configure(bg=color_background)

# Obtener la ruta absoluta de la imagen
img_home = os.path.join(os.getcwd(), "img", "f.png")
img_ingreso = os.path.join(os.getcwd(), "img", "f.png")
img_registro = os.path.join(os.getcwd(), "img", "f.png")

# Cargar la imagen
bg_img_home = PhotoImage(file=img_home)
bg_img_ingreso = PhotoImage(file=img_ingreso)
bg_img_registro = PhotoImage(file=img_registro)

# Crear un widget Label con la imagen cargada
bg_label = Label(root, image=bg_img_home)
bg_label.place(relwidth=1, relheight=1)

#Mensaje de bienvenida
Label(text="¡Bienvenido!", fg=color_blanco, bg=color_negro, font=(font_label, 20), width="500", height="2").pack()
Label(text="¿Seras digno del ingreso?", fg=color_blanco, bg=color_negro, font=(font_label, 20), width="500", height="2").pack() 

#Botones de ingreso y registro

Button(text=txt_ingreso, fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40").pack()


Button(text=txt_registro, fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40").pack()





root.mainloop()
