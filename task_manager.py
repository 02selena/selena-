import tkinter as tk
from tkinter import messagebox, simpledialog

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")

        # Crear un marco para la entrada y los botones
        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(frame, width=40)
        self.task_entry.pack(side=tk.LEFT)

        # Botón para añadir tareas
        add_task_button = tk.Button(frame, text="Añadir Tarea", command=self.add_task)
        add_task_button.pack(side=tk.LEFT)

        # Botón para marcar tarea como completada
        complete_task_button = tk.Button(frame, text="Marcar como Completada", command=self.complete_task)
        complete_task_button.pack(side=tk.LEFT)

        # Botón para eliminar tarea
        delete_task_button = tk.Button(frame, text="Eliminar Tarea", command=self.delete_task)
        delete_task_button.pack(side=tk.LEFT)

        # Lista de tareas
        self.task_listbox = tk.Listbox(self.root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Configurar atajos de teclado
        self.root.bind('<Return>', lambda event: self.add_task())
        self.root.bind('<c>', lambda event: self.complete_task())
        self.root.bind('<Delete>', lambda event: self.delete_task())
        self.root.bind('<Escape>', lambda event: self.root.quit())

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)  # Limpiar el campo de entrada

    def complete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            selected_task = self.task_listbox.get(selected_task_index)
            self.task_listbox.delete(selected_task_index)
            self.task_listbox.insert(selected_task_index, f"{selected_task} - Completada")
            self.task_listbox.itemconfig(selected_task_index, {'fg': 'gray'})  # Cambiar color de texto
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_task_index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
