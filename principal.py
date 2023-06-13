# Importar librerias

from tkinter import *
from tkinter import messagebox as msg
import os
from tkinter import ttk
import cv2
from mtcnn.mtcnn import MTCNN
from matplotlib import pyplot as plt
import basedatos as bd

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

res_bd = {"id": 0, "affected": 0} #retorno variable base de datos | id: idUsuario | affected: booleano 0/1

# GENERAL ----------------------------------------------------------------
def saltoDeLinea(screen):
    # Agrega un salto de linea dentro de la ventana
    
    Label(screen, text="", bg=color_background).pack()
    
def imprimirMensaje(screen, text, flag):
    # Imprime un mensaje por consola y ventana
    
    if flag:
        print(color_exito + text + color_normal)
        screen.destroy()
        msg.showinfo(message=text, title="¡Éxito!")
    else:
        print(color_error + text + color_normal)
        Label(screen, text=text, fg="red", bg=color_background, font=(font_label, 12)).pack()

def configurarPantalla(screen, text, image_screen):
    # Configura la ventana emergente
    
    screen.title(text)
    screen.geometry(size_screen)
    screen.configure(bg=color_background)
    
    Label(screen, image=image_screen, bg=color_negro, text=f"{text}", fg=color_blanco, font=(font_label, 18), width="500", height="2").place(relwidth=1, relheight=1) 

def configurarEntradaDatos(screen, var, flag): 
    # Configura la entrada de datos para ingreso y registro segun corresponda
    
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
    data = plt.imread(img)
    for i in range(len(faces)):
        x1, y1, ancho, alto = faces[i]["box"]
        x2, y2 = x1 + ancho, y1 + alto
        plt.subplot(1,len(faces), i + 1)
        plt.axis("off")
        face = cv2.resize(data[y1:y2, x1:x2],(150,200), interpolation=cv2.INTER_CUBIC)
        cv2.imwrite(img, face)
        plt.imshow(data[y1:y2, x1:x2])

# REGISTRO ---------------------------------------------------------------- 
def registrarRostroBD(img):
    nombre_usuario = img.replace(".jpg","").replace(".png","")
    res_bd = bd.registrarUsuario(nombre_usuario, path + img)

    saltoDeLinea(screen1)
    
    if(res_bd["affected"]):
        imprimirMensaje(screen1, "¡Éxito! Ha sido registrado correctamente", 1)
    else:
        imprimirMensaje(screen1, "¡Error! No ha sido registrado correctamente", 0)
    os.remove(img)
    
def capturarRostroRegistro():
    # Captura el rostro al registrarse y envia un mensaje con los resultados del mismo
    
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
        registrarRostroBD(img)
    else:
        cap.release()
        cv2.destroyAllWindows()
        imprimirMensaje(screen1, "¡Registro Cancelado!", 1) 
        
def ventanaRegistro():
    # Crea la ventana de registro
    
    global usuario1
    global usuario_entry1
    global screen1

    screen1 = Toplevel(root)
    usuario1 = StringVar()
        
    configurarPantalla(screen1, txt_registro, bg_img_registro)
    usuario_entry1 = configurarEntradaDatos(screen1, usuario1, 0)
    
# INGRESO ----------------------------------------------------------------
def compatibilidad(img1, img2):
    # Verifica la compatibilidad de la imagen capturada con la que fue guardada en el registro
    
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
    # Captura el rostro al ingresar y entrega un mensaje con los resultados de compatibiildad
    
    cap = cv2.VideoCapture(0)
    usuario_ingreso = usuario2.get()
    img = f"{usuario_ingreso}_login.jpg"
    img_usuario = f"{usuario_ingreso}.jpg"

    while True:
        ret, frame = cap.read()
        cv2.imshow("Login Facial", frame)
                
        key = cv2.waitKey(1)
        if MTCNN().detect_faces(frame):            
            break;
    
    cv2.imwrite(img, frame)
    cap.release()
    cv2.destroyAllWindows()

    usuario_entry2.delete(0, END)
    
    pixeles = plt.imread(img)
    faces = MTCNN().detect_faces(pixeles)

    recortarRostro(img, faces)
    saltoDeLinea(screen2)
    
    res_bd = bd.obtenerUsuario(usuario_ingreso, path + img_usuario)
    if(res_bd["affected"]):
        my_files = os.listdir()
        if img_usuario in my_files:
            face_reg = cv2.imread(img_usuario, 0)
            face_ing = cv2.imread(img, 0)

            comp = compatibilidad(face_reg, face_ing)
            compResul = "{}Compatibilidad del {:.1%}{}".format(color_error, float(comp), color_normal)
            porcentaje = float(comp) * 100
            if comp >= 0.90:
                print(compResul)
                imprimirMensaje(screen2, f"Bienvenido, {usuario_ingreso}", 1)
            else:
                print(compResul)
                imprimirMensaje(screen2, f"¡Error! Incompatibilidad de datos {porcentaje}%", 0)
            os.remove(img_usuario)
            
        else:
            imprimirMensaje(screen2, "¡Error! Usuario no encontrado", 0)
    else:
        imprimirMensaje(screen2, "¡Error! Usuario no encontrado", 0)
    os.remove(img)

def ventanaIngreso():
    # Crea la ventana de ingreso
    
    global screen2
    global usuario2
    global usuario_entry2

    screen2 = Toplevel(root)
    usuario2 = StringVar()
    
    configurarPantalla(screen2, txt_ingreso, bg_img_ingreso)
    usuario_entry2 = configurarEntradaDatos(screen2, usuario2, 1)

def mostrarUsuarios():
    screen3 = Toplevel()
    screen3.title("Lista de usuarios")
    screen3.geometry("300x500")

    usuarios_frame = Frame(screen3, bg='white')
    usuarios_frame.pack(fill=BOTH, expand=True)

    # Encabezado de la lista
    header = Label(usuarios_frame, text='Lista de usuarios', font=('Arial', 14, 'bold'), bg='white')
    header.pack(side=TOP, pady=10)

    # Tabla de usuarios
    usuarios_tabla = ttk.Treeview(usuarios_frame, columns=('ID', 'Nombre'), show='headings')
    usuarios_tabla.heading('ID', text='ID', anchor='center')
    usuarios_tabla.column('ID', width=50, anchor='center')
    usuarios_tabla.heading('Nombre', text='Nombre', anchor='center')
    usuarios_tabla.column('Nombre', width=200, anchor='center')
    usuarios_tabla.pack(side=TOP, padx=10, pady=10, fill=BOTH, expand=True)

    # Obtener la lista de usuarios
    usuarios_lista = bd.obtenerUsuarios()
    for usuario in usuarios_lista:
        usuarios_tabla.insert('', END, values=usuario)

    # Botón para borrar un usuario seleccionado en la lista
    def borrarUsuarioSeleccionado():
        item_seleccionado = usuarios_tabla.focus()
        if item_seleccionado:
            usuario_id = usuarios_tabla.item(item_seleccionado)['values'][0]
            bd.borrarUsuario(usuario_id)
            
            # Actualizar la lista de usuarios después de borrar uno
            usuarios_tabla.delete(*usuarios_tabla.get_children())
            usuarios_lista = bd.obtenerUsuarios()
            for usuario in usuarios_lista:
                usuarios_tabla.insert('', END, values=usuario)
            
    def actualizarUsuarioSeleccionado():
        item_seleccionado = usuarios_tabla.focus()
        if item_seleccionado:
            usuario_id = usuarios_tabla.item(item_seleccionado)['values'][0]
            screen4 = Toplevel()
            screen4.title("Actualizar nombre")
            screen4.geometry("300x150")

            Label(screen4, text="Nuevo nombre:").pack()
            nuevo_nombre_entry = Entry(screen4)
            nuevo_nombre_entry.pack()

            def actualizarNombre():
                nuevo_nombre = nuevo_nombre_entry.get()
                bd.actualizarNombreUsuario(usuario_id, nuevo_nombre)
                screen4.destroy()
                
                # Actualizar la lista de usuarios después de actualizar uno
                usuarios_tabla.delete(*usuarios_tabla.get_children())
                usuarios_lista = bd.obtenerUsuarios()
                for usuario in usuarios_lista:
                    usuarios_tabla.insert('', END, values=usuario)
        else:
            screen3.grab_set()
            msg.showwarning("Advertencia", "Por favor seleccione un usuario antes de actualizar")
            
        Button(screen4, text="Actualizar", command=actualizarNombre).pack()
        
    btn_borrar = Button(usuarios_frame, text='Borrar usuario', command=borrarUsuarioSeleccionado, font=('Arial', 10, 'bold'), fg='red')
    btn_borrar.pack(side=BOTTOM, pady=10)

    btn_actualizar = Button(usuarios_frame, text='Actualizar nombre', command=actualizarUsuarioSeleccionado, font=('Arial', 10, 'bold'), fg='blue')
    btn_actualizar.pack(side=BOTTOM, pady=10)
                    

    
def salir():
    # Cierra la ejecucion
    
    root.destroy()

# VENTANA PRINCIPAL
    
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
Button(text="Mostrar usuarios", fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command=mostrarUsuarios).pack()

saltoDeLinea(root)
Button(text="Salir", fg=color_blanco, bg=color_negro_btn, activebackground=color_background, borderwidth=0, font=(font_label, 14), height="2", width="40", command=salir).pack()

root.mainloop()