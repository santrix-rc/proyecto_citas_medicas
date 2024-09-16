from clases.cita import Cita
from clases.medico import Medico
from clases.reporte import Reporte

class GestionCitas:
    def __init__(self):
        self.citas = []
        self.medicos = {
            "Dr. Gómez": Medico("Dr. Gómez", "Cardiología"),
            "Dra. Herrera": Medico("Dra. Herrera", "Neurología"),
            "Dr. Ramírez": Medico("Dr. Ramírez", "Pediatría")
        }

        # Añadir horarios predefinidos
        self.medicos["Dr. Gómez"].agregar_horario("2024-09-15", ["10:00", "11:00", "12:00"])
        self.medicos["Dra. Herrera"].agregar_horario("2024-09-16", ["09:00", "11:00", "13:00"])
        self.medicos["Dr. Ramírez"].agregar_horario("2024-09-17", ["08:00", "10:00", "12:00"])

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

    def generar_reporte(self):
        reporte = Reporte(self.citas)
        return reporte.generar_reporte_json()
