from clases.cita import Cita
from clases.medico import Medico
from clases.reporte import Reporte

class GestionCitas:
    def __init__(self):
        self.citas = []
        self.medicos = {
            "Dr. Gómez": Medico("Dr. Gómez", [Especialidad("Cardiología")]),
            "Dra. Herrera": Medico("Dra. Herrera", [Especialidad("Dermatología")]),
            "Dr. Ramírez": Medico("Dr. Ramírez", [Especialidad("Pediatría")])
        }

        # Agregamos disponibilidad a los médicos
        self.medicos["Dr. Gómez"].agregar_disponibilidad("2024-09-15", ["10:00", "11:00", "12:00"])
        self.medicos["Dra. Herrera"].agregar_disponibilidad("2024-09-16", ["09:00", "11:00", "13:00"])
        self.medicos["Dr. Ramírez"].agregar_disponibilidad("2024-09-17", ["08:00", "10:00", "12:00"])

    def agregar_disponibilidad_medico(self, medico, fecha, horas):
        if medico in self.medicos:
            self.medicos[medico].agregar_disponibilidad(fecha, horas)

    def agendar_cita(self, paciente, medico, fecha, hora):
        nueva_cita = Cita(paciente, medico, fecha, hora)
        self.citas.append(nueva_cita)
        return f"Cita agendada para {paciente} con {medico} el {fecha} a las {hora}."

