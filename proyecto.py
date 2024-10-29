from tkinter import *
from tkinter import ttk

ventana = Tk()

#ventana.geometry("470x470")
ventana.minsize(470, 470)
ventana.title("Project Tkinter - Python")
ventana.resizable(1,1)

def home():
    global addSuccess
    limpiarPantalla()
    # Configuración de pantalla de inicio
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=190,
        pady=20
    )
    home_label.grid(row=0, column=0, columnspan=2,sticky="nsew")
    
    # products_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")
    # for product in products:
    #     if len(product) == 3:
    #         product.append("Añadido")
    #         Label(products_frame, text=product[0]).grid()
    #         Label(products_frame, text=product[1]).grid()
    #         Label(products_frame, text=product[2]).grid()
    #         Label(products_frame, text="----------------").grid()
    
    products_table.grid(row=2, column=0, columnspan=2)
    products_table.heading("#0", text="Producto", anchor=W)
    products_table.heading("#1", text="Precio", anchor=W)
    
    for product in products:
        if len(product) == 3:
            product.append("Añadido")
            products_table.insert('', 0, text=product[0], values= (product[1]))
            
    if(addSuccess):
        add_add_success_label.grid(row=3, column=0, columnspan=2, sticky="nsew")
        addSuccess = False
            
    
    return True

def add():
    limpiarPantalla()    
    # Limpiar las variables de entrada
    limpiarDatosProducto()
    
    # Configuración del encabezado centrado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=90,
        pady=20
    )
    
    # Instrucciones de centrado de formulario
    add_label.grid(row=0, column=0, columnspan=5, sticky="nsew")
    
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="w")
    
    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky="w")
    
    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky="ne")
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky="w")
    add_description_entry.config(
        width=25,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )
    
    add_divisor.grid(row=4)
    
    button_to_save.grid(row= 5, column=1, sticky= "nw")
    button_to_save.config(
        padx=15,
        bg="green",
        fg="white"
    )
    
    return True

def add_product():
    global addSuccess
    #print("Valores antes de agregar:", name_data.get(), price_data.get(), add_description_entry.get("1.0", "end-1c"))
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    # name_data.set("")
    # price_data.set("")
    # add_description_entry.delete("1.0", END)
    addSuccess = True
    home()
    
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
    add_add_success_label.grid_remove()
    products_frame.grid_remove()
    products_table.grid_remove()
    add_name_label.grid_remove()
    add_name_entry.grid_remove()
    add_price_label.grid_remove()
    add_price_entry.grid_remove()
    add_description_entry.grid_remove()
    add_description_label.grid_remove()
    add_divisor.grid_remove()
    button_to_save.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def limpiarDatosProducto():
    name_data.set("")  # Limpia el nombre
    price_data.set("")  # Limpia el precio
    add_description_entry.delete("1.0", END)  # Limpia la descripción
    return True

# Variables accesorias
addSuccess = False 

# Variables de datos
products = []
name_data = StringVar()
price_data = StringVar()

# Pantalla de inicio
home_label = Label(ventana, text="Inicio")
products_frame = Frame(ventana)
products_frame.columnconfigure(0, weight=1)
Label(ventana).grid(row=1)

Label(products_frame).grid(row=0)
products_table = ttk.Treeview(height=12, columns=2)

# Pantalla de añadir producto
add_label = Label(ventana, text="Añadir producto")
add_add_success_label = Label(ventana, text="¡Producto añadido exitosamente!")

# Formulario: Etiquetas y entradas de datos 
add_frame = Frame(ventana)
add_name_label = Label(ventana, text="Nombre del producto: ")
add_name_entry = Entry(ventana, textvariable=name_data, width=30)

add_price_label = Label(ventana, text="Precio del producto: ")
add_price_entry = Entry(ventana, textvariable=price_data, width=30)

add_description_label = Label(ventana, text="Descripción del producto: ")
add_description_entry = Text(ventana)

add_divisor = Label(ventana)

button_to_save = Button(ventana, text="Guardar", command=add_product)

# Pantalla de información
info_label = Label(ventana, text="Información")
data_label = Label(ventana, text="Create by Marco Avaria(Author)")

home()

menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir producto", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

ventana.config(menu=menu_superior)

ventana.mainloop()