#-------Importar librerias -------

from tkinter import *
from tkinter import messagebox as msg
import os
from tkinter import ttk
import cv2
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot as plt



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


#GENERAL
def saltoDeLinea(screen):
    Label(screen, text="", bg=color_background).pack()
    
def imprimirMensaje(screen, text, flag):
    if flag:
        print(color_exito + text + color_normal)
        screen.destroy()
        msg.showinfo(message=text, title="¡Éxito!")
    else:
        print(color_error + text + color_normal)
        Label(screen, text=text, fg="red", bg=color_background, font=(font_label, 12)).pack()


def configurarPantalla(screen, text, image_screen):
    screen.title(text)
    screen.geometry(size_screen)
    screen.configure(bg=color_background)
    
    Label(screen, image=image_screen, bg=color_negro, text=f"{text}", fg=color_blanco, font=(font_label, 18), width="500", height="2").place(relwidth=1, relheight=1) 

def configurarEntradaDatos(screen, var, flag):   
    Label(screen, text="Ingrese usuario:", fg=color_blanco, bg=color_negro, font=(font_label, 12)).pack()
    
    entry = Entry(screen, textvariable=var, justify=CENTER, font=(font_label, 12))
    entry.focus_force()
    entry.pack(side=TOP, ipadx=30, ipady=6)
    
    saltoDeLinea(root)
    frame = Frame(screen)
    frame.pack()
    
    if flag == 0:
        Button(frame, text="Registrarse", fg=color_blanco, bg=color_negro, borderwidth=10,font=(font_label, 14), height="2", width="40", command=capturarRostroRegistro).grid(row=5, column=0, padx=0, pady=0, sticky="nsew")
    
    return entry

#REGISTRO 
def capturarRostroRegistro():
    cap = cv2.VideoCapture(0)
    usuario_reg_img = usuario1.get()
    img = f"{usuario_reg_img}.jpg"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Registro Facial", frame)
        if cv2.waitKey(0) == 27:
            break
    
    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    usuario_entry1.delete(0, END)
    
    pixeles = plt.imread(img)
    faces = MTCNN().detect_faces(pixeles)
        
def ventanaRegistro():
    global usuario1
    global usuario_entry1
    global screen1

    screen1 = Toplevel(root)
    usuario1 = StringVar()
        
    configurarPantalla(screen1, txt_registro, bg_img_registro)
    usuario_entry1 = configurarEntradaDatos(screen1, usuario1, 0)


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
saltoDeLinea(root)
Button(text=txt_ingreso, fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40").pack()

saltoDeLinea(root)
Button(text=txt_registro, fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command=ventanaRegistro).pack()





root.mainloop()
