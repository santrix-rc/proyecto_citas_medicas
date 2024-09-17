class Recordatorio:
    def __init__(self, cita, mensaje):
        self.cita = cita
        self.mensaje = mensaje

    def enviar(self):
        print(f"Recordatorio enviado a {self.cita.paciente}: {self.mensaje}")
