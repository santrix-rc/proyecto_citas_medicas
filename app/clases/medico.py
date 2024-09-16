class Medico:
    def __init__(self, nombre, especialidades=None, disponibilidad=None):
        self.nombre = nombre
        self.especialidades = especialidades if especialidades else []  # Lista de especialidades
        self.disponibilidad = disponibilidad if disponibilidad else []  # Lista de objetos de Disponibilidad

    def agregar_especialidad(self, especialidad):
        self.especialidades.append(especialidad)

    def agregar_disponibilidad(self, fecha, horas):
        self.disponibilidad.append(Disponibilidad(self.nombre, fecha, horas))
