import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry  # Necesitarás instalar tkcalendar (pip install tkcalendar)

class AgendaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Agenda Personal")
        self.root.geometry("600x400")

        # Frame para mostrar los eventos
        self.frame_eventos = tk.Frame(self.root)
        self.frame_eventos.pack(pady=10)

        # Treeview para listar eventos
        self.tree = ttk.Treeview(self.frame_eventos, columns=("Fecha", "Hora", "Descripción"), show='headings')
        self.tree.heading("Fecha", text="Fecha")
        self.tree.heading("Hora", text="Hora")
        self.tree.heading("Descripción", text="Descripción")
        self.tree.pack()

        # Frame para entrada de datos
        self.frame_datos = tk.Frame(self.root)
        self.frame_datos.pack(pady=10)

        # Etiquetas y entradas para fecha, hora, descripción
        tk.Label(self.frame_datos, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
        self.date_entry = DateEntry(self.frame_datos, date_pattern="dd/mm/yyyy")
        self.date_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_datos, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
        self.time_entry = tk.Entry(self.frame_datos)
        self.time_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_datos, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
        self.desc_entry = tk.Entry(self.frame_datos)
        self.desc_entry.grid(row=2, column=1, padx=5, pady=5)

        # Frame para los botones de acción
        self.frame_botones = tk.Frame(self.root)
        self.frame_botones.pack(pady=10)

        # Botones: Agregar, Eliminar, Salir
        self.btn_agregar = tk.Button(self.frame_botones, text="Agregar Evento", command=self.agregar_evento)
        self.btn_agregar.grid(row=0, column=0, padx=10)

        self.btn_eliminar = tk.Button(self.frame_botones, text="Eliminar Evento Seleccionado", command=self.eliminar_evento)
        self.btn_eliminar.grid(row=0, column=1, padx=10)

        self.btn_salir = tk.Button(self.frame_botones, text="Salir", command=self.root.quit)
        self.btn_salir.grid(row=0, column=2, padx=10)

    def agregar_evento(self):
        # Obtener datos de los campos de entrada
        fecha = self.date_entry.get()
        hora = self.time_entry.get()
        descripcion = self.desc_entry.get()

        if fecha and hora and descripcion:
            # Insertar en el TreeView
            self.tree.insert("", "end", values=(fecha, hora, descripcion))
            # Limpiar campos
            self.limpiar_campos()
        else:
            messagebox.showwarning("Advertencia", "Por favor, completa todos los campos.")

    def eliminar_evento(self):
        selected_item = self.tree.selection()
        if selected_item:
            confirm = messagebox.askyesno("Confirmar", "¿Estás seguro de que deseas eliminar este evento?")
            if confirm:
                self.tree.delete(selected_item)
        else:
            messagebox.showwarning("Advertencia", "Selecciona un evento para eliminar.")

    def limpiar_campos(self):
        self.date_entry.set_date('')
        self.time_entry.delete(0, 'end')
        self.desc_entry.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = AgendaApp(root)
    root.mainloop()
