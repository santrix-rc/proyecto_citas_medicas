class Especialidad:
    def __init__(self, nombre):
        self.nombre = nombre


class Disponibilidad:
    def __init__(self, medico, fecha, horas):
        self.medico = medico
        self.fecha = fecha
        self.horas = horas  # Lista de horas disponibles
