import tkinter as tk
from tkinter import messagebox
from gestion_citas import GestionCitas

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Citas Médicas")
        self.gestion_citas = GestionCitas()

        # Label y entrada para el nombre del paciente
        self.label_paciente = tk.Label(root, text="Nombre del Paciente")
        self.label_paciente.pack()
        self.entry_paciente = tk.Entry(root)
        self.entry_paciente.pack()

        # Lista desplegable para seleccionar médico
        self.label_medico = tk.Label(root, text="Selecciona el Médico")
        self.label_medico.pack()
        self.medico_var = tk.StringVar()
        self.medico_var.set(list(self.gestion_citas.medicos.keys())[0])
        self.medico_menu = tk.OptionMenu(root, self.medico_var, *self.gestion_citas.medicos.keys(), command=self.actualizar_fecha)
        self.medico_menu.pack()

        # Lista desplegable para seleccionar fecha y hora
        self.label_fecha = tk.Label(root, text="Selecciona la Fecha")
        self.label_fecha.pack()
        self.fecha_var = tk.StringVar()
        self.fecha_menu = tk.OptionMenu(root, self.fecha_var, "")
        self.fecha_menu.pack()

        self.label_hora = tk.Label(root, text="Selecciona la Hora")
        self.label_hora.pack()
        self.hora_var = tk.StringVar()
        self.hora_menu = tk.OptionMenu(root, self.hora_var, "")
        self.hora_menu.pack()

        # Botones
        self.button_agendar = tk.Button(root, text="Agendar Cita", command=self.agendar_cita)
        self.button_agendar.pack()

        self.button_reporte = tk.Button(root, text="Generar Reporte JSON", command=self.generar_reporte)
        self.button_reporte.pack()

    def actualizar_fecha(self, medico):
        self.fecha_var.set(list(self.gestion_citas.medicos[medico].horarios.keys())[0])
        menu = self.fecha_menu["menu"]
        menu.delete(0, "end")
        for fecha in self.gestion_citas.medicos[medico].horarios:
            menu.add_command(label=fecha, command=tk._setit(self.fecha_var, fecha))

        self.hora_var.set(self.gestion_citas.medicos[medico].horarios[self.fecha_var.get()][0])
        menu_horas = self.hora_menu["menu"]
        menu_horas.delete(0, "end")
        for hora in self.gestion_citas.medicos[medico].horarios[self.fecha_var.get()]:
            menu_horas.add_command(label=hora, command=tk._setit(self.hora_var, hora))

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

    def generar_reporte(self):
        reporte_json = self.gestion_citas.generar_reporte()
        messagebox.showinfo("Reporte JSON", reporte_json)
        print("Reporte JSON generado:\n", reporte_json)

# Iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
