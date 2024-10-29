from tkinter import *

ventana = Tk()

ventana.geometry("470x470")
ventana.title("Project Tkinter - Python")
ventana.resizable(1, 1)

def home():
    limpiarPantalla()
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    return True

def add():
    limpiarPantalla()
    # Configuración del encabezado centrado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=100,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    
    # Centrar los elementos del formulario
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky="e")
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    
    return True

def info():
    limpiarPantalla()
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    info_label.grid(row=0, column=0, columnspan=2, sticky="nsew")
    data_label.grid(row=1, column=0, columnspan=2, sticky="nsew")
    return True

def limpiarPantalla():
    add_label.grid_remove()
    add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_description_label.grid_remove()
    add_description_entry.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

# Variables de datos
name_data = StringVar()
price_data = StringVar()
description_data = StringVar()

# Etiquetas y campos de entrada
home_label = Label(ventana, text="Inicio")
add_label = Label(ventana, text="Añadir producto")
add_name_label = Label(ventana, text="Nombre del producto")
add_name_entry = Entry(ventana, textvariable=name_data, width=30)
add_price_label = Label(ventana, text="Precio del producto")
add_price_entry = Entry(ventana, textvariable=price_data)
add_description_label = Label(ventana, text="Descripción del producto")
add_description_entry = Entry(ventana, textvariable=description_data)

info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Create by Marco Avaria(Author)")

# Mostrar pantalla inicial
home()

# Menú superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir producto", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()