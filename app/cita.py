# Autor: Santiago
class Cita:
    def __init__(self, paciente, medico, fecha, hora):
        self.paciente = paciente
        self.medico = medico
        self.fecha = fecha
        self.hora = hora

    def __str__(self):
        return f"{self.paciente} con {self.medico} el {self.fecha} a las {self.hora}"
