import tkinter as tk
from tkinter import ttk

# Función para agregar información a la lista
def agregar_info():
    info = campo_texto.get()
    if info:
        lista_datos.insert(tk.END, info)
        campo_texto.delete(0, tk.END)

# Función para limpiar la lista
def limpiar_info():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear y colocar los componentes
etiqueta = tk.Label(ventana, text="Ingrese la información:")
etiqueta.pack(pady=5)

campo_texto = tk.Entry(ventana, width=50)
campo_texto.pack(pady=5)

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_info)
boton_agregar.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_info)
boton_limpiar.pack(pady=5)

lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Iniciar el bucle de eventos
ventana.mainloop()
