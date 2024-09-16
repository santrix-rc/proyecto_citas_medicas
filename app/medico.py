# Autor: Santiago
class Medico:
    def __init__(self, nombre, fechas_disponibles, horarios):
        self.nombre = nombre
        self.fechas_disponibles = fechas_disponibles
        self.horarios = horarios

    def __str__(self):
        return self.nombre
