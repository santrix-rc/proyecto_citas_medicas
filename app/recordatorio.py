
class Recordatorio:
    def __init__(self, cita, mensaje):
        self.cita = cita
        self.mensaje = mensaje

    def enviar(self):
        return f"Recordatorio: {self.mensaje} para la cita de {self.cita.paciente} con {self.cita.medico} el {self.cita.fecha} a las {self.cita.hora}."
