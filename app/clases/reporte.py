class Reporte:
    def __init__(self, citas):
        self.citas = citas

    def generar_reporte(self):
        for cita in self.citas:
            print(f"Cita de {cita.paciente} con {cita.medico} el {cita.fecha} a las {cita.hora}.")
