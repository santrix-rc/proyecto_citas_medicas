# Autor: Santiago
class Medico:
    def __init__(self, nombre, especialidad):
        self.nombre = nombre
        self.especialidad = especialidad
        self.horarios = {}

    def agregar_horario(self, fecha, horas):
        self.horarios[fecha] = horas
