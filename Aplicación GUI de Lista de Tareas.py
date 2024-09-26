import tkinter as tk
from tkinter import messagebox, simpledialog

# Función para añadir una nueva tarea
def add_task(event=None):
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Entrada vacía", "Por favor, escribe una tarea.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"[Completada] {task}")
    except IndexError:
        messagebox.showwarning("No seleccionado", "Por favor, selecciona una tarea para marcarla como completada.")

# Función para eliminar una tarea seleccionada
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("No seleccionado", "Por favor, selecciona una tarea para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Campo de entrada para nuevas tareas
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

# Botón para añadir una nueva tarea
add_task_button = tk.Button(root, text="Añadir Tarea", width=20, command=add_task)
add_task_button.pack(pady=5)

# Listbox para mostrar las tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Botón para marcar la tarea como completada
mark_completed_button = tk.Button(root, text="Marcar como Completada", width=20, command=mark_completed)
mark_completed_button.pack(pady=5)

# Botón para eliminar la tarea seleccionada
delete_task_button = tk.Button(root, text="Eliminar Tarea", width=20, command=delete_task)
delete_task_button.pack(pady=5)

# Bind para que la tecla Enter añada la tarea
root.bind('<Return>', add_task)

# Iniciar el loop de la aplicación
root.mainloop()
