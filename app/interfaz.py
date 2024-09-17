# interfaz.py
import tkinter as tk
from tkinter import messagebox
from gestion_citas import GestionCitas

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Citas Médicas")
        self.gestion_citas = GestionCitas()

        # Campos de entrada para la información del paciente
        self.label_paciente = tk.Label(root, text="Nombre del Paciente")
        self.label_paciente.pack()
        self.entry_paciente = tk.Entry(root)
        self.entry_paciente.pack()

        # Lista desplegable para seleccionar médico
        self.label_medico = tk.Label(root, text="Selecciona el Médico")
        self.label_medico.pack()
        self.medico_var = tk.StringVar()
        self.medico_var.set(list(self.gestion_citas.medicos.keys())[0])
        self.medico_menu = tk.OptionMenu(root, self.medico_var, *self.gestion_citas.medicos.keys(), command=self.actualizar_fechas)
        self.medico_menu.pack()

        # Lista desplegable para seleccionar fecha
        self.label_fecha = tk.Label(root, text="Selecciona la Fecha")
        self.label_fecha.pack()
        self.fecha_var = tk.StringVar()
        self.fecha_menu = tk.OptionMenu(root, self.fecha_var, "")
        self.fecha_menu.pack()

        # Lista desplegable para seleccionar hora
        self.label_hora = tk.Label(root, text="Selecciona la Hora")
        self.label_hora.pack()
        self.hora_var = tk.StringVar()
        self.hora_menu = tk.OptionMenu(root, self.hora_var, "")
        self.hora_menu.pack()

        # Botón para agendar la cita
        self.button_agendar = tk.Button(root, text="Agendar Cita", command=self.agendar_cita)
        self.button_agendar.pack()

        # Inicializar las fechas para el médico seleccionado por defecto
        self.actualizar_fechas(self.medico_var.get())

    def actualizar_fechas(self, medico):
        # Obtener las fechas disponibles para el médico seleccionado
        fechas_disponibles = self.gestion_citas.obtener_fechas_disponibles(medico)

        # Actualizar la lista de fechas
        self.fecha_var.set('')  # Resetear selección
        menu = self.fecha_menu["menu"]
        menu.delete(0, "end")  # Eliminar opciones anteriores
        for fecha in fechas_disponibles:
            menu.add_command(label=fecha, command=tk._setit(self.fecha_var, fecha, self.actualizar_horas))

        # Limpiar las horas disponibles cuando se cambia el médico
        self.hora_var.set('')  # Resetear selección
        hora_menu = self.hora_menu["menu"]
        hora_menu.delete(0, "end")

    def actualizar_horas(self, *args):
        # Obtener las horas disponibles para el médico y la fecha seleccionada
        medico = self.medico_var.get()
        fecha = self.fecha_var.get()
        print(f"Medico: {medico}, Fecha: {fecha}")  # Para depuración
        horas_disponibles = self.gestion_citas.obtener_horas_disponibles(medico, fecha)
        print(f"Horas disponibles: {horas_disponibles}")  # Para depuración

        # Actualizar la lista de horas
        self.hora_var.set('')  # Resetear selección
        hora_menu = self.hora_menu["menu"]
        hora_menu.delete(0, "end")  # Eliminar opciones anteriores
        if horas_disponibles:  # Verificar si hay horas disponibles
            for hora in horas_disponibles:
                print(f"Agregando hora: {hora}")  # Para depuración
                hora_menu.add_command(label=hora, command=tk._setit(self.hora_var, hora))
        else:
            print("No hay horas disponibles.")  # Para depuración

    def agendar_cita(self):
        paciente = self.entry_paciente.get()
        medico = self.medico_var.get()
        fecha = self.fecha_var.get()
        hora = self.hora_var.get()

        if not paciente or not medico or not fecha or not hora:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        else:
            mensaje = self.gestion_citas.agendar_cita(paciente, medico, fecha, hora)
            messagebox.showinfo("Cita Agendada", mensaje)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
