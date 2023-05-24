# Importar librerias

from tkinter import *
from tkinter import messagebox as msg
import os
from tkinter import ttk
import cv2
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot as plt

# Configuracion colores y letra
path = os.getcwd() + "/"

txt_ingreso = "Inicio de Sesión"
txt_registro = "Registrarse"

color_blanco = "#f4f5f4"
color_negro = "#101010"
color_negro_btn = "#202020"
color_background = "#ADA7A7"

font_label = "Calibri"
size_screen = "1000x1000"

# Colores consola
color_exito = "\033[1;32;40m"
color_error = "\033[1;31;40m"
color_normal = "\033[0;37;40m"


# GENERAL
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
    
    if flag:
        Button(frame, text="Permitir acceso",fg=color_blanco, bg=color_negro_btn, borderwidth=10, font=(font_label, 14), height="2", width="40",command=capturarRostroIngreso).grid(row=20, column=0, padx=0, pady=0, sticky="nsew")
    else:
        Button(frame, text="Registrarse", fg=color_blanco, bg=color_negro, borderwidth=10,font=(font_label, 14), height="2", width="40", command=capturarRostroRegistro).grid(row=5, column=0, padx=0, pady=0, sticky="nsew")
    return entry

def recortarRostro(img, faces):
    
    path_registro = os.getcwd() + "/Capturas Registro"
    
    #Crear una carpeta para guardar las capturas de registro en caso de que no exista
    if not os.path.exists(path_registro):
        os.makedirs(path_registro);
    
    data = plt.imread(img)
    for i in range(len(faces)):
        x1, y1, ancho, alto = faces[i]["box"]
        x2, y2 = x1 + ancho, y1 + alto
        plt.subplot(1,len(faces), i + 1)
        plt.axis("off")
        face = cv2.resize(data[y1:y2, x1:x2],(150,200), interpolation=cv2.INTER_CUBIC)
        nombre_imagen = f"{path_registro}/{img}"
        cv2.imwrite(nombre_imagen, face)
        plt.imshow(data[y1:y2, x1:x2])

# REGISTRO 
def capturarRostroRegistro():
    cap = cv2.VideoCapture(0)
    usuario_reg_img = usuario1.get()
    img = f"{usuario_reg_img}.jpg"

    while True:
        ret, frame = cap.read()
        frame_original = frame.copy()
        
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceClassif.detectMultiScale(gray,1.2, 5)
        
        cv2.rectangle(frame, (10, 5), (240, 25), (50, 50, 50), -1)
        cv2.putText(frame, 'Presione G, para registrarse', (10, 20), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        cv2.rectangle(frame, (10, 50), (210, 25), (50, 50, 50), -1)
        cv2.putText(frame, 'presione Esc para salir', (10, 45), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)

        for (x,y,w,h) in faces:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),2)
        
        cv2.imshow("Registro Facial", frame)
        key = cv2.waitKey(1)
        if key == ord("g"):
            registrar = True
            break
        elif key == 27:
            registrar = False
            break
    
    if registrar:
        cv2.imwrite(img, frame_original)
        cap.release()
        cv2.destroyAllWindows()

        usuario_entry1.delete(0, END)
    
        pixeles = plt.imread(img)
        faces = MTCNN().detect_faces(pixeles)
        recortarRostro(img, faces)
        os.remove(img)
        imprimirMensaje(screen1, "¡Registro Exitoso!", 1) 
    else:
        cap.release()
        cv2.destroyAllWindows()
        imprimirMensaje(screen1, "¡Registro Cancelado!", 1) 
        
def ventanaRegistro():
    global usuario1
    global usuario_entry1
    global screen1

    screen1 = Toplevel(root)
    usuario1 = StringVar()
        
    configurarPantalla(screen1, txt_registro, bg_img_registro)
    usuario_entry1 = configurarEntradaDatos(screen1, usuario1, 0)
    
# INGRESO
def compatibilidad(img1, img2):
    orb = cv2.ORB_create()

    kpa, dac1 = orb.detectAndCompute(img1, None)
    kpa, dac2 = orb.detectAndCompute(img2, None)

    comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = comp.match(dac1, dac2)

    similar = [x for x in matches if x.distance < 70]
    if len(matches) == 0:
        return 0
    return len(similar)/len(matches)

def capturarRostroIngreso():
    cap = cv2.VideoCapture(0)
    usuario_ingreso = usuario2.get()
    img = f"{usuario_ingreso}_login.jpg"
    img_usuario = f"{usuario_ingreso}.jpg"

    while True:
        ret, frame = cap.read()
        
        cv2.rectangle(frame, (10, 5), (240, 25), (50, 50, 50), -1)
        cv2.putText(frame, 'Presione I, para ingresar', (10, 20), 2, 0.5, (255, 255, 255), 1, cv2.LINE_AA)
        
        cv2.imshow("Login Facial", frame)
                
        key = cv2.waitKey(1)
        if key == ord("i"):            
            break;
    
    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    usuario_entry2.delete(0, END)
    
    pixeles = plt.imread(img)
    faces = MTCNN().detect_faces(pixeles)

    recortarRostro(img, faces)
    saltoDeLinea(screen2)
    
    path_registro = os.path.join(os.getcwd(), "Capturas Registro")
    path_imagenUsuario = os.path.join(path_registro, img_usuario)
    path_imagenLogin = os.path.join(path_registro, img)
    if os.path.exists(path_imagenUsuario):
        face_reg = cv2.imread(path_imagenUsuario, 0)
        face_ing = cv2.imread(img, 0)

        comp = compatibilidad(face_reg, face_ing)
        compResul = "{}Compatibilidad del {:.1%}{}".format(color_error, float(comp), color_normal)
        porcentaje = float(comp) * 100
        if comp >= 0.94:
            print(compResul)
            imprimirMensaje(screen2, f"Bienvenido, {usuario_ingreso}", 1)
        else:
            print(compResul)
            imprimirMensaje(screen2, f"¡Error! Incompatibilidad de datos {porcentaje}%", 0)
    else:
        imprimirMensaje(screen2, "¡Error! Usuario no encontrado", 0)
    os.remove(path_imagenLogin)
    os.remove(img)

def ventanaIngreso():
    global screen2
    global usuario2
    global usuario_entry2

    screen2 = Toplevel(root)
    usuario2 = StringVar()
    
    configurarPantalla(screen2, txt_ingreso, bg_img_ingreso)
    usuario_entry2 = configurarEntradaDatos(screen2, usuario2, 1)
    
def salir():
    root.destroy()
    
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

# Mensaje de bienvenida
Label(text="¡Bienvenido!", fg=color_blanco, bg=color_negro, font=(font_label, 20), width="500", height="2").pack()
Label(text="¿Seras digno del ingreso?", fg=color_blanco, bg=color_negro, font=(font_label, 20), width="500", height="2").pack() 

# Botones de ingreso y registro
saltoDeLinea(root)
Button(text=txt_ingreso, fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command=ventanaIngreso).pack()

saltoDeLinea(root)
Button(text=txt_registro, fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command=ventanaRegistro).pack()

saltoDeLinea(root)
Button(text="Salir", fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command=salir).pack()

root.mainloop()