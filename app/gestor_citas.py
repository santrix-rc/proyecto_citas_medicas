# Autor: Santiago
from cita import Cita

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
        return [str(cita) for cita in self.citas]
