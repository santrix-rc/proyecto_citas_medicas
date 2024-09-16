import json

class Reporte:
    def __init__(self, citas):
        self.citas = citas

    def generar_reporte_json(self):
        reporte = [{"paciente": cita.paciente, "medico": cita.medico, "fecha": cita.fecha, "hora": cita.hora}
                   for cita in self.citas]
        return json.dumps(reporte, indent=4)
