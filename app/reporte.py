
import json

class Reporte:
    @staticmethod
    def generar_reporte_json(citas):
        reporte = [{"paciente": cita.paciente, "medico": cita.medico, "fecha": cita.fecha, "hora": cita.hora}
                   for cita in citas]
        return json.dumps(reporte, indent=4)
