# gestion_citas.py
class GestionCitas:
    def __init__(self):
        self.medicos = {
            "Dr. Pérez": ["2024-09-17", "2024-09-18"],
            "Dr. García": ["2024-09-19", "2024-09-20"]
        }
        self.horas_disponibles = {
            ("Dr. Pérez", "2024-09-17"): ["10:00", "11:00", "12:00"],
            ("Dr. Pérez", "2024-09-18"): ["09:00", "10:00", "14:00"],
            ("Dr. García", "2024-09-19"): ["08:00", "12:00", "16:00"],
            ("Dr. García", "2024-09-20"): ["09:00", "11:00", "15:00"]
        }

    def obtener_fechas_disponibles(self, medico):
        return self.medicos.get(medico, [])

    def obtener_horas_disponibles(self, medico, fecha):
        return self.horas_disponibles.get((medico, fecha), [])

    def agendar_cita(self, paciente, medico, fecha, hora):
        return f"Cita agendada para {paciente} con {medico} el {fecha} a las {hora}."
