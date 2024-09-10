import tkinter as tk
from tkinter import messagebox
import json


class Cita:
    def __init__(self, paciente, medico, fecha, hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora


class GestionCitas:
    def __init__(self):
        # Datos quemados con citas y médicos predefinidos
        self.citas = [
            Cita("Juan Pérez", "Dr. Gómez", "2024-09-15", "10:00"),
            Cita("Laura Martínez", "Dra. Herrera", "2024-09-16", "11:00")
        ]
        self.medicos = ["Dr. Gómez", "Dra. Herrera", "Dr. Ramírez"]

    def agendar_cita(self, paciente, medico, fecha, hora):
        nueva_cita = Cita(paciente, medico, fecha, hora)
        self.citas.append(nueva_cita)
        return f"Cita agendada para {paciente} con {medico} el {fecha} a las {hora}."

    def cancelar_cita(self, paciente, fecha, hora):
        for cita in self.citas:
            if cita.paciente == paciente and cita.fecha == fecha and cita.hora == hora:
                self.citas.remove(cita)
                return f"Cita de {paciente} el {fecha} a las {hora} ha sido cancelada."
        return "Cita no encontrada."

    def mostrar_citas(self):
        if len(self.citas) == 0:
            return "No hay citas registradas."
        return [f"{cita.paciente} con {cita.medico} el {cita.fecha} a las {cita.hora}" for cita in self.citas]

    def generar_reporte_json(self):
        # Generar el reporte en formato JSON
        reporte = [{"paciente": cita.paciente, "medico": cita.medico, "fecha": cita.fecha, "hora": cita.hora}
                   for cita in self.citas]
        return json.dumps(reporte, indent=4)


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Citas Médicas")

        # Inicializar gestión de citas con datos predefinidos
        self.gestion_citas = GestionCitas()

        # Labels y entradas para agendar citas
        self.label_paciente = tk.Label(root, text="Nombre del Paciente")
        self.label_paciente.pack()
        self.entry_paciente = tk.Entry(root)
        self.entry_paciente.pack()

        self.label_fecha = tk.Label(root, text="Fecha (YYYY-MM-DD)")
        self.label_fecha.pack()
        self.entry_fecha = tk.Entry(root)
        self.entry_fecha.pack()

        self.label_hora = tk.Label(root, text="Hora (HH:MM)")
        self.label_hora.pack()
        self.entry_hora = tk.Entry(root)
        self.entry_hora.pack()

        self.label_medico = tk.Label(root, text="Nombre del Médico")
        self.label_medico.pack()
        self.entry_medico = tk.Entry(root)
        self.entry_medico.pack()

        # Botón para agendar citas
        self.button_agendar = tk.Button(root, text="Agendar Cita", command=self.agendar_cita)
        self.button_agendar.pack()

        # Botón para cancelar citas
        self.button_cancelar = tk.Button(root, text="Cancelar Cita", command=self.cancelar_cita)
        self.button_cancelar.pack()

        # Botón para mostrar citas
        self.button_mostrar = tk.Button(root, text="Mostrar Citas", command=self.mostrar_citas)
        self.button_mostrar.pack()

        # Botón para generar reporte en JSON
        self.button_reporte = tk.Button(root, text="Generar Reporte JSON", command=self.generar_reporte)
        self.button_reporte.pack()

    def agendar_cita(self):
        paciente = self.entry_paciente.get()
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        medico = self.entry_medico.get()
        if not paciente or not fecha or not hora or not medico:
            messagebox.showwarning("Advertencia", "Por favor, complete todos los campos.")
        else:
            mensaje = self.gestion_citas.agendar_cita(paciente, medico, fecha, hora)
            messagebox.showinfo("Cita Agendada", mensaje)

    def cancelar_cita(self):
        paciente = self.entry_paciente.get()
        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        if not paciente or not fecha or not hora:
            messagebox.showwarning("Advertencia", "Por favor, complete el nombre, fecha y hora para cancelar.")
        else:
            mensaje = self.gestion_citas.cancelar_cita(paciente, fecha, hora)
            messagebox.showinfo("Cancelar Cita", mensaje)

    def mostrar_citas(self):
        citas = self.gestion_citas.mostrar_citas()
        if isinstance(citas, list):
            citas_mensaje = "\n".join(citas)
        else:
            citas_mensaje = citas
        messagebox.showinfo("Citas Registradas", citas_mensaje)

    def generar_reporte(self):
        reporte_json = self.gestion_citas.generar_reporte_json()
        messagebox.showinfo("Reporte JSON", reporte_json)
        print("Reporte JSON generado:\n", reporte_json)


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
