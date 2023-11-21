from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import font
import os
from Clases.Tree import Tree 
import shutil

path = "D:/Universidad de Caldas/Tercer Semestre/Estructura de Datos/C"

root = Tk()
root.geometry("1086x670")
root.resizable(False, False)
root.title("Administrador de Archivos.")
root.iconbitmap("D:/Universidad de Caldas/Tercer Semestre/Estructura de Datos/FilesManager/Imagenes/Imagenes Folder/sobre.ico")


fuente_personalizada = font.Font(family="Verdana", size=10)
estilo = ttk.Style()
estilo.configure("Button", font=fuente_personalizada)
estilo.configure("Treeview", font=fuente_personalizada)
root.option_add("*Toplevel*Font", fuente_personalizada)

# Cambiar la fuente de todos los widgets Label
root.option_add("*Label*Font", fuente_personalizada)

# Cambiar la fuente de todos los widgets Button
root.option_add("*Button*Font", fuente_personalizada)

e = Entry(root)
buscar = ttk.Button(root, text="Buscar", command=lambda: search(e.get(), arbol))


# Configura las filas y columnas para que se expandan correctamente
root.grid_rowconfigure(0, weight=1)  # Hace que la fila 0 se expanda para llenar todo el espacio vertical disponible
root.grid_columnconfigure(0, weight=7)  # Hace que la columna 0 se expanda para llenar el 70% del espacio horizontal disponible
root.grid_columnconfigure(1, weight=3)  # Hace que la columna 1 se expanda para llenar el 30% del espacio horizontal disponible


# Crea el canvas y el LabelFrame
center = LabelFrame(root, bg="white", width=200, height=50)

# Coloca los widgets en la cuadrícula
center.grid(row=1, column=1, sticky="nsew", ipadx=300)
center.grid_propagate(0)

e.grid(row=0, column=1, ipadx=100)
buscar.grid(row=0, column=2)

tv = ttk.Treeview(root, height=30)
tv.place(relwidth=1)  # Establece el ancho al 50% del ancho de la ventana

arbol = Tree.construir_arbol(path)

#Imagenes del Treeview
image = Image.open("Imagenes/Imagenes Tree/carpeta.png")
word_image = Image.open("Imagenes/Imagenes Tree/word.png")
rar_image = Image.open("Imagenes/Imagenes Tree/rar.png")
power_point_image = Image.open("Imagenes/Imagenes Tree/powerpoint.png")
text_image = Image.open("Imagenes/Imagenes Tree/txt.png")
rtf_image = Image.open("Imagenes/Imagenes Tree/rtf.png")
access_image = Image.open("Imagenes/Imagenes Tree/access.png")

word = ImageTk.PhotoImage(word_image)
photo = ImageTk.PhotoImage(image)
rar = ImageTk.PhotoImage(rar_image)
power_point = ImageTk.PhotoImage(power_point_image)
txt = ImageTk.PhotoImage(text_image)
rtf = ImageTk.PhotoImage(rtf_image)
access = ImageTk.PhotoImage(access_image)

#Imagenes de los archivos
word_image_folder = Image.open("Imagenes/Imagenes Folder/word.png")
word_image_folder = word_image_folder.resize((100, 100), Image.LANCZOS)
rar_image_folder = Image.open("Imagenes/Imagenes Folder/rar.png")
rar_image_folder = rar_image_folder.resize((100, 100), Image.LANCZOS)
access_image_folder = Image.open("Imagenes/Imagenes Folder/access.png")
access_image_folder = access_image_folder.resize((100, 100), Image.LANCZOS)
power_point_image_folder = Image.open("Imagenes/Imagenes Folder/powerpoint.png")
power_point_image_folder = power_point_image_folder.resize((100, 100), Image.LANCZOS)
rtf_image_folder = Image.open("Imagenes/Imagenes Folder/rtf.png")
rtf_image_folder = rtf_image_folder.resize((100, 100), Image.LANCZOS)
text_image_folder = Image.open("Imagenes/Imagenes Folder/txt.png")
text_image_folder = text_image_folder.resize((100, 100), Image.LANCZOS)
image_folder = Image.open("Imagenes/Imagenes Folder/carpeta.png")
image_folder = image_folder.resize((100, 100), Image.LANCZOS)

docx = ImageTk.PhotoImage(word_image_folder)
rarr = ImageTk.PhotoImage(rar_image_folder)
accdb = ImageTk.PhotoImage(access_image_folder)
pptx = ImageTk.PhotoImage(power_point_image_folder)
rtff = ImageTk.PhotoImage(rtf_image_folder)
text = ImageTk.PhotoImage(rtf_image_folder)
folder = ImageTk.PhotoImage(image_folder)
          
recorrido = list()
  
def back():   
    if len(recorrido) >= 1:
        path_back = recorrido[-1]
        update_content(path_back)
        recorrido.pop()
    else:
        for widget in center.winfo_children():
            widget.destroy()
    
atras = ttk.Button(root, text="Atras", command=back)
atras.grid(row=0, column=0)
            
rutas = {}            

def update_content(path):
    # Eliminar todos los widgets actuales en el frame del medio
    print(f"Dentro del update {path}")
    for widget in center.winfo_children():
        widget.destroy()

    contenido = os.listdir(path)
    
    print(contenido)
    
    i = 0
    j = 0
    
    # Diccionario para mapear las extensiones a las imágenes
    extensiones = {".docx": docx, ".rar": rarr, ".zip": rarr, ".accdb": accdb, ".pptx": pptx, ".rtf": rtff, ".txt": text}
    
    for elemento in contenido:
        file_path = os.path.join(path, elemento)
        if os.path.isfile(file_path):
            # Obtén la extensión del archivo
            _, ext = os.path.splitext(elemento)
            
            # Si la extensión está en el diccionario, crea un Label con la imagen correspondiente
            if ext in extensiones:
                label = Label(center, text=elemento, image=extensiones[ext], compound="top", bg="white")
                # Coloca el Label en la cuadrícula
                if j == 5:
                    i += 1
                    j = 0
                
                label.grid(row=i, column=j, padx=15, pady=10)
                j += 1
                
        elif os.path.isdir(path):
            label = Label(center, text=elemento, image=folder, compound="top", bg="white")
            
            rutas[label] = file_path
            print(elemento)
            # Coloca el Label en la cuadrícula
            if j == 4:
                i += 1
                j = 0
            
            label.bind("<Double-1>", doble_click)
            label.bind("<Button-3>", on_right_click)
            label.grid(row=i, column=j, padx=15, pady=10)
            j += 1
            
        else:
            Label(center, text=elemento).pack()


def doble_click(event):
    widget = event.widget

    # Obtener la ruta del widget
    path = rutas[widget]

    recorrido.append(path)
    update_content(path)


def on_right_click(event):   
    # Obtener el elemento bajo el cursor del ratón
    item_id = tv.identify('item', event.x, event.y)

    # Obtener la información del elemento
    item = tv.item(item_id)
    
    if "." not in item['text']:
        menu = Menu(tv, tearoff=0)
        menu.add_command(label='Cambiar Nombre', command=lambda: update(item))
        menu.add_command(label='Crear Carpeta', command=lambda: create(item))
        menu.add_command(label='Eliminar Carpeta', command=lambda: delete(item))
        menu.post(event.x_root, event.y_root)

def on_right_click_two(event):   
    # Obtener el elemento bajo el cursor del ratón
    item_id = tv.identify('item', event.x, event.y)

    # Obtener la información del elemento
    item = tv.item(item_id)
    
    selected = tv.selection()
    if selected:
        item = tv.item(selected)
        nombre = item['text']
        path_actual = item['values'][0] if item['values'] else None
    
    if "." in item['text']:
        menu = Menu(tv, tearoff=0)
        menu.add_command(label='Cambiar Nombre', command=lambda: rename_archive(nombre, path_actual))
        menu.add_command(label='Eliminar', command=lambda: delete_archive(nombre, path_actual))
        menu.add_command(label='Copiar', command=lambda: copy(nombre,path_actual))
        menu.add_command(label='Cortar', command=lambda: cut(nombre, path_actual))
        
        menu.post(event.x_root, event.y_root)
    
def on_right_click_center(event):   
    item = tv.selection()
    menu = Menu(tv, tearoff=0)
    menu.add_command(label="Pegar", command=lambda: paste(item))
    menu.post(event.x_root, event.y_root)
    
center.bind("<Button-3>", on_right_click_center)
    
    
def update(item):
    selected = tv.selection()
    if selected:
        item = tv.item(selected)
        path_actual = item['values'][0] if item['values'] else None
        update_folder(path_actual)

def create(item):
    selected = tv.selection()
    if selected:
        item = tv.item(selected)
        path_actual = item['values'][0] if item['values'] else None
        create_folder(path_actual)

def delete(item):
    selected = tv.selection()
    if selected:
        item = tv.item(selected)
        path_actual = item['values'][0] if item['values'] else None
        delete_folder(path_actual)

#NUEVOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO

name_copiado = None
path_copiado = None
case = None

def copy(nombre, path_actual):
    global name_copiado
    global path_copiado
    name_copiado = nombre
    path_copiado = path_actual
    global case
    case = "copy"
    print(f"Hola, este es el NOMBRE copiado: {name_copiado}")
    print(f"Hola, este es el PATH copiado: {path_copiado}")

def cut(nombre, path_actual):
    global name_copiado
    global path_copiado
    name_copiado = nombre
    path_copiado = path_actual
    global case
    case = "cut"
    print(f"Hola, este es el copiado: {name_copiado}")

def paste(item):
    if name_copiado is not None:
        if case == "copy":
            selected = tv.selection()
            if selected:
                item = tv.item(selected)
                path_actual = item['values'][0] if item['values'] else None
            
            parent_dir = os.path.join(path_actual, name_copiado)

            # Copia el archivo a la nueva ubicación
            shutil.copy2(path_copiado, parent_dir)
                
            tv.delete(*tv.get_children())
                
            arbol = Tree.construir_arbol(path)
            process_directory(arbol)
            update_content(path_actual)
            
            return
        elif case == "cut":
            if name_copiado is not None:
                selected = tv.selection()
                if selected:
                    item = tv.item(selected)
                    path_actual = item['values'][0] if item['values'] else None
                
                path_actual = path_actual.replace("\\", "/")
                    
                parent_dir = os.path.join(path_actual, name_copiado)
                    
                # Mover el archivo a la nueva ubicación
                shutil.move(path_copiado, parent_dir)
                    
                tv.delete(*tv.get_children())
                
                arbol = Tree.construir_arbol(path)
                process_directory(arbol)
                update_content(path_actual)
    
def rename_archive(nombre, path_actual):
    
    new_name = simpledialog.askstring("Cambio de nombre", "Ingrese el nuevo nombre del archivo.")

    extension = obtener_extension(nombre)
    
    new_name = new_name+"."+extension
       
    # Crea el nuevo path reemplazando la última parte por el nuevo texto
    ruta, _ = os.path.split(path_actual)
    
    new_file_path = os.path.join(ruta, new_name)

    os.rename(path_actual, new_file_path)
    
    tv.delete(*tv.get_children())
                    
    arbol = Tree.construir_arbol(path)
    process_directory(arbol)
    update_content(ruta)

def obtener_extension(nombre_archivo):
    partes = nombre_archivo.split('.')
    if len(partes) > 1:
        return partes[-1]
    else:
        return ''

def delete_archive(nombre, path_actual): 
    ruta, _ = os.path.split(path_actual)
    
    response = messagebox.askquestion("Advertencia", f"¿Desea eliminar el archivo {nombre}?")
    if response == "yes":
        os.remove(path_actual)
        tv.delete(*tv.get_children())
        
        global arbol
        
        arbol = Tree.construir_arbol(path)
        process_directory(arbol)
        update_content(ruta)
    
def search(nombre, nodo):
    resultado = search_in_tree(nombre, nodo)
    
    for widget in center.winfo_children():
        widget.destroy()
        
    i = 0
    j = 0
    
    # Diccionario para mapear las extensiones a las imágenes
    extensiones = {".docx": docx, ".rar": rarr, ".zip": rarr, ".accdb": accdb, ".pptx": pptx, ".rtf": rtff, ".txt": text}
    
    if resultado is not None:
        for res in resultado:
            # Obtén la extensión del archivo
            _, ext = os.path.splitext(res.nombre)
            
            # Si la extensión está en el diccionario, crea un Label con la imagen correspondiente
            if ext in extensiones:
                label = Label(center, text=res.nombre, image=extensiones[ext], compound="top", bg="white")
                
                # Coloca el Label en la cuadrícula
                if j == 5:
                    i += 1
                    j = 0
                
                label.grid(row=i, column=j, padx=15, pady=10)
                j += 1
                
                print(res.nombre)

    
def search_in_tree(nombre, nodo):
    coincidencias = []
    
    # Si el nombre del nodo contiene el nombre que estamos buscando, lo agregamos a la lista
    if nombre in nodo.nombre:
        coincidencias.append(nodo)

    # Si el nodo tiene hijos, buscamos en cada uno de ellos
    for hijo in nodo.hijos:
        coincidencias += search_in_tree(nombre, hijo)

    # Retornamos la lista de coincidencias
    return coincidencias


def process_directory(arbol, parent=""):
    for dir in arbol.hijos:
        if "." not in dir.nombre:
            pathActual = dir.path
            pathActual = pathActual.replace("/", "\\")
            item = tv.insert(parent, END, text=dir.nombre, values=[pathActual], image=photo)
            #tv.bind("<Button-3>", on_click)
            tv.bind("<Double-1>", double_click)
            tv.bind("<Button-3>", on_right_click)
            tv.bind("<Double-3>", on_right_click_two)
            process_directory(dir, item)
        else:
            pathActual = dir.path
            pathActual = pathActual.replace("/", "\\")
            if ".docx" in dir.nombre:
                tv.insert(parent, END, text=dir.nombre, values=[pathActual], image=word)
            elif ".rar" in dir.nombre or ".zip" in dir.nombre:
                tv.insert(parent, END, text=dir.nombre, values=[pathActual], image=rar)
            elif ".pptx" in dir.nombre:
                tv.insert(parent, END, text=dir.nombre, values=[pathActual],  image=power_point)
            elif ".txt" in dir.nombre:
                tv.insert(parent, END, text=dir.nombre, values=[pathActual],  image=txt)
            elif ".rtf" in dir.nombre:
                tv.insert(parent, END, text=dir.nombre, values=[pathActual],  image=rtf)
            elif ".accdb" in dir.nombre:
                tv.insert(parent, END, text=dir.nombre, values=[pathActual],  image=access)
            else: 
                tv.insert(parent, END, text=dir.nombre)
            
    tv.grid(row=1, column=0)
    
def update_folder(path_actual):
    # Obtiene el ID del elemento seleccionado
    selected = tv.selection()[0]
    
    print(f"Este es el padre: {selected}")
    print(path_actual)
    if selected:
        # Obtiene la información del elemento seleccionado
        item = tv.item(selected)
        
        # Pide al usuario el nuevo texto
        new_text = simpledialog.askstring("Cambio de nombre", "Ingrese el nuevo nombre de la carpeta")

        if new_text:
            # Cambia las barras invertidas por barras normales
            path_actual = path_actual.replace("\\", "/")
            
            # Encuentra el último /
            last_slash_index = path_actual.rfind("/")
            
            # Crea el nuevo path reemplazando la última parte por el nuevo texto
            new_path = path_actual[:last_slash_index+1] + new_text
            
            # Cambia el nombre de la carpeta en el sistema de archivos
            os.rename(path_actual, new_path)
            
            # Cambia el texto del elemento en el Treeview
            tv.item(selected, text=new_text, values=[new_path])
            
            
def create_folder(path_actual):
    # Obtiene el ID del elemento seleccionado
    selected = tv.selection()
    
    if selected:
        # Obtiene la información del elemento seleccionado
        item = tv.item(selected)
        
        # Pide al usuario el nuevo texto
        directory = simpledialog.askstring("Nueva Carpeta", "Ingrese el nombre de la carpeta")

        if directory:
            # Cambia las barras invertidas por barras normales
            path_actual = path_actual.replace("\\", "/")
            
            parent_dir = os.path.join(path_actual, directory)
            
            # Cambia el nombre de la carpeta en el sistema de archivos
            os.mkdir(parent_dir)
            
            # Cambia el texto del elemento en el Treeview
            tv.insert(selected, END, text=directory, image=photo)
            
            
            tv.delete(*tv.get_children())
            
            arbol = Tree.construir_arbol(path)
            process_directory(arbol)
            update_content(path_actual)


def delete_folder(path_actual):
    selected = tv.selection()
    
    carpeta = path_actual
    if os.path.exists(carpeta):
        print(path_actual)
        # Usar shutil.rmtree para eliminar la carpeta
        response = messagebox.askquestion("Advertencia", f"¿Desea eliminar la carpeta {carpeta}?")
        if response == "yes":
            shutil.rmtree(carpeta)
            tv.delete(selected)
            new_path = os.path.dirname(path_actual)
            print(f"Este es el nuevo path: {new_path}")
            update_content(new_path)

def double_click(event):
    selected = tv.selection()
    if selected:
        item = tv.item(selected)
        path_actual = item['values'][0] if item['values'] else None
        recorrido.append(path_actual)
        update_content(path_actual)
    
process_directory(arbol)

root.mainloop()