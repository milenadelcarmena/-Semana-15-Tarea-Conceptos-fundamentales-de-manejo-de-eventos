# -Semana-15-Tarea-Conceptos-fundamentales-de-manejo-de-eventos
Tarea: Aplicación GUI de Lista de Tareas

Explicación de mí tarea

Interfaz Gráfica

Utilize tk.Entry para ingresar nuevas tareas.

Los botones Añadir Tarea, Marcar como Completada y Eliminar Tarea están creados con tk.Button.

Las tareas se muestran en un tk.Listbox.


Manejo de Eventos

El botón Añadir Tarea y la tecla Enter llaman a la función add_task para agregar una tarea.

El botón Marcar como Completada llama a mark_completed para marcar la tarea seleccionada con un símbolo de check (✔).

El botón Eliminar Tarea llama a delete_task para eliminar la tarea seleccionada.


Lógica de la Aplicación

Las tareas se almacenan en una lista (self.tasks) y se muestran en el Listbox.

Al marcar una tarea como completada, se modifica visualmente en el Listbox.

Al eliminar una tarea, se elimina tanto del Listbox como de la lista self.tasks.


Manejo de Errores

Se utiliza try-except para evitar errores cuando el usuario no selecciona una tarea antes de marcarla como completada o eliminarla.
