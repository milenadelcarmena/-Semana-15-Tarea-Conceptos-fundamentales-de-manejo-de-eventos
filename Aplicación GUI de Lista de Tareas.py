import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")
        self.root.geometry("400x300")

        # Lista para almacenar las tareas
        self.tasks = []

        # Crear y posicionar los componentes de la interfaz
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.mark_completed)
        self.complete_button.grid(row=2, column=0, padx=5, pady=10)

        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=10)

        # Manejar la tecla Enter para añadir tareas
        self.root.bind('<Return>', lambda event: self.add_task())

    def add_task(self):
        """Añade una tarea a la lista."""
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea válida.")

    def mark_completed(self):
        """Marca la tarea seleccionada como completada."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.task_listbox.get(selected_index)
            self.task_listbox.delete(selected_index)
            self.task_listbox.insert(selected_index, f"✔ {task}")
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para marcar como completada.")

    def delete_task(self):
        """Elimina la tarea seleccionada de la lista."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.task_listbox.delete(selected_index)
            del self.tasks[selected_index]
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
