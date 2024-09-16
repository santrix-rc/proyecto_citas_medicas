import tkinter as tk
from tkinter import messagebox
from gestion_citas import GestionCitas

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Citas Médicas")

        self.gestion_citas = GestionCitas()

        # Entrada para el nombre del paciente
        self.label_paciente = tk.Label(root, text="Nombre del Paciente")
        self.label_paciente.pack()
        self.entry_paciente = tk.Entry(root)
        self.entry_paciente.pack()

        # Menú de selección del médico
        self.label_medico = tk.Label(root, text="Selecciona el Médico")
        self.label_medico.pack()
        self.medico_var = tk.StringVar()
        self.medico_var.set(list(self.gestion_citas.medicos.keys())[0])  # Selección por defecto
        self.medico_menu = tk.OptionMenu(root, self.medico_var, *self.gestion_citas.medicos.keys(), command=self.actualizar_fecha)
        self.medico_menu.pack()

        # Menú de selección de fecha
        self.label_fecha = tk.Label(root, text="Selecciona la Fecha")
        self.label_fecha.pack()
        self.fecha_var = tk.StringVar()
        self.fecha_menu = tk.OptionMenu(root, self.fecha_var, "")
        self.fecha_menu.pack()

        # Menú de selección de hora
        self.label_hora = tk.Label(root, text="Selecciona la Hora")
        self.label_hora.pack()
        self.hora_var = tk.StringVar()
        self.hora_menu = tk.OptionMenu(root, self.hora_var, "")
        self.hora_menu.pack()

        # Botón para agendar citas
        self.button_agendar = tk.Button(root, text="Agendar Cita", command=self.agendar_cita)
        self.button_agendar.pack()

        # Campo para agregar disponibilidad de médico
        self.label_fecha_nueva = tk.Label(root, text="Fecha nueva disponibilidad")
        self.label_fecha_nueva.pack()
        self.entry_fecha_nueva = tk.Entry(root)
        self.entry_fecha_nueva.pack()

        self.label_hora_nueva = tk.Label(root, text="Horas nuevas (separadas por coma)")
        self.label_hora_nueva.pack()
        self.entry_hora_nueva = tk.Entry(root)
        self.entry_hora_nueva.pack()

        self.button_disponibilidad = tk.Button(root, text="Agregar Disponibilidad", command=self.agregar_disponibilidad)
        self.button_disponibilidad.pack()

        # Actualizar fecha y hora al seleccionar el médico
        self.actualizar_fecha(self.medico_var.get())

    def actualizar_fecha(self, medico):
        medico_obj = self.gestion_citas.medicos[medico]
        fechas_disponibles = [dispo.fecha for dispo in medico_obj.disponibilidad]
        
        # Actualizamos el menú de fechas
        self.fecha_var.set(fechas_disponibles[0])
        menu_fecha = self.fecha_menu["menu"]
        menu_fecha.delete(0, "end")
        for fecha in fechas_disponibles:
            menu_fecha.add_command(label=fecha, command=tk._setit(self.fecha_var, fecha))

        # Actualizamos el menú de horas
        horas_disponibles = medico_obj.disponibilidad[0].horas
        self.hora_var.set(horas_disponibles[0])
        menu_hora = self.hora_menu["menu"]
        menu_hora.delete(0, "end")
        for hora in horas_disponibles:
            menu_hora.add_command(label=hora, command=tk._setit(self.hora_var, hora))

    def agregar_disponibilidad(self):
        medico = self.medico_var.get()
        fecha_nueva = self.entry_fecha_nueva.get()
        horas_nuevas = self.entry_hora_nueva.get().split(",")  # Convertir las horas separadas por comas
        self.gestion_citas.agregar_disponibilidad_medico(medico, fecha_nueva, horas_nuevas)
        messagebox.showinfo("Disponibilidad Agregada", f"Disponibilidad agregada para {medico} en {fecha_nueva}.")

