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
        self.medicos = {
            "Dr. Gómez": ["2024-09-15", "2024-09-16"],
            "Dra. Herrera": ["2024-09-16", "2024-09-17"],
            "Dr. Ramírez": ["2024-09-17", "2024-09-18"]
        }
        self.horarios = {
            "Dr. Gómez": ["10:00", "11:00", "12:00"],
            "Dra. Herrera": ["09:00", "11:00", "13:00"],
            "Dr. Ramírez": ["08:00", "10:00", "12:00"]
        }

    def agendar_cita(self, paciente, medico, fecha, hora):
        nueva_cita = Cita(paciente, medico, fecha, hora)
        self.citas.append(nueva_cita)
        return f"Cita agendada para {paciente} con {medico} el {fecha} a las {hora}."

    def cancelar_cita(self, cita_seleccionada):
        if cita_seleccionada:
            self.citas.remove(cita_seleccionada)
            return f"Cita de {cita_seleccionada.paciente} con {cita_seleccionada.medico} ha sido cancelada."
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

        # Label y entrada para el nombre del paciente
        self.label_paciente = tk.Label(root, text="Nombre del Paciente")
        self.label_paciente.pack()
        self.entry_paciente = tk.Entry(root)
        self.entry_paciente.pack()

        # Lista desplegable para seleccionar médico
        self.label_medico = tk.Label(root, text="Selecciona el Médico")
        self.label_medico.pack()
        self.medico_var = tk.StringVar()
        self.medico_var.set(list(self.gestion_citas.medicos.keys())[0])  # Valor por defecto
        self.medico_menu = tk.OptionMenu(root, self.medico_var, *self.gestion_citas.medicos.keys(), command=self.actualizar_fecha)
        self.medico_menu.pack()

        # Lista desplegable para seleccionar fecha (se actualiza según el médico)
        self.label_fecha = tk.Label(root, text="Selecciona la Fecha")
        self.label_fecha.pack()
        self.fecha_var = tk.StringVar()
        self.fecha_menu = tk.OptionMenu(root, self.fecha_var, *self.gestion_citas.medicos[self.medico_var.get()])
        self.fecha_menu.pack()

        # Lista desplegable para seleccionar hora
        self.label_hora = tk.Label(root, text="Selecciona la Hora")
        self.label_hora.pack()
        self.hora_var = tk.StringVar()
        self.hora_menu = tk.OptionMenu(root, self.hora_var, *self.gestion_citas.horarios[self.medico_var.get()])
        self.hora_menu.pack()

        # Botón para agendar citas
        self.button_agendar = tk.Button(root, text="Agendar Cita", command=self.agendar_cita)
        self.button_agendar.pack()

        # Botón para cancelar citas
        self.button_cancelar = tk.Button(root, text="Cancelar Cita", command=self.mostrar_citas_para_cancelar)
        self.button_cancelar.pack()

        # Botón para generar reporte en JSON
        self.button_reporte = tk.Button(root, text="Generar Reporte JSON", command=self.generar_reporte)
        self.button_reporte.pack()

    def actualizar_fecha(self, medico):
        # Actualizar la lista de fechas y horarios según el médico seleccionado
        self.fecha_var.set(self.gestion_citas.medicos[medico][0])
        menu = self.fecha_menu["menu"]
        menu.delete(0, "end")
        for fecha in self.gestion_citas.medicos[medico]:
            menu.add_command(label=fecha, command=tk._setit(self.fecha_var, fecha))

        self.hora_var.set(self.gestion_citas.horarios[medico][0])
        menu_horas = self.hora_menu["menu"]
        menu_horas.delete(0, "end")
        for hora in self.gestion_citas.horarios[medico]:
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

    def mostrar_citas_para_cancelar(self):
        citas = self.gestion_citas.citas
        if len(citas) == 0:
            messagebox.showinfo("Cancelar Cita", "No hay citas para cancelar.")
            return

        # Crear una ventana para mostrar las citas y seleccionar cuál cancelar
        cancel_window = tk.Toplevel(self.root)
        cancel_window.title("Selecciona una Cita para Cancelar")
        cancel_window.geometry("400x300")

        citas_var = tk.StringVar(value=[f"{cita.paciente} con {cita.medico} el {cita.fecha} a las {cita.hora}" for cita in citas])
        listbox = tk.Listbox(cancel_window, listvariable=citas_var, height=10)
        listbox.pack(fill=tk.BOTH, expand=True)

        def cancelar_seleccionada():
            index = listbox.curselection()
            if index:
                cita_seleccionada = citas[index[0]]
                mensaje = self.gestion_citas.cancelar_cita(cita_seleccionada)
                messagebox.showinfo("Cancelar Cita", mensaje)
                cancel_window.destroy()
            else:
                messagebox.showwarning("Advertencia", "Seleccione una cita para cancelar.")

        cancelar_button = tk.Button(cancel_window, text="Cancelar Cita", command=cancelar_seleccionada)
        cancelar_button.pack()

    def generar_reporte(self):
        reporte_json = self.gestion_citas.generar_reporte_json()
        messagebox.showinfo("Reporte JSON", reporte_json)
        print("Reporte JSON generado:\n", reporte_json)

# Autor: Santiago
# Fecha: 2024-09-10
# Versión: 1.0.2

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
