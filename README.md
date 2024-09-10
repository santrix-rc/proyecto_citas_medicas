# proyecto_citas_medicas
# Gestión de Citas Médicas

## Descripción

Este proyecto es una aplicación de escritorio sencilla para gestionar citas médicas utilizando la biblioteca `tkinter` en Python. La aplicación permite agendar, cancelar, mostrar y generar un reporte en formato JSON para las citas médicas.

## Clases y Métodos

### Clase `Cita`

La clase `Cita` representa una cita médica con los siguientes atributos:
- `paciente`: Nombre del paciente.
- `medico`: Nombre del médico.
- `fecha`: Fecha de la cita en formato `YYYY-MM-DD`.
- `hora`: Hora de la cita en formato `HH:MM`.

### Clase `GestionCitas`

La clase `GestionCitas` maneja la gestión de citas médicas. Contiene los siguientes métodos:
- `__init__()`: Inicializa la gestión de citas con citas y médicos predefinidos.
- `agendar_cita(paciente, medico, fecha, hora)`: Agrega una nueva cita a la lista de citas.
- `cancelar_cita(paciente, fecha, hora)`: Elimina una cita específica de la lista de citas.
- `mostrar_citas()`: Devuelve una lista de todas las citas registradas.
- `generar_reporte_json()`: Genera un reporte de todas las citas en formato JSON.

### Clase `App`

La clase `App` es la interfaz gráfica de la aplicación y utiliza `tkinter` para crear la ventana y los controles. Contiene los siguientes métodos:
- `__init__(root)`: Inicializa la interfaz gráfica, incluyendo etiquetas, campos de entrada y botones.
- `agendar_cita()`: Lee los datos de entrada y llama a `agendar_cita` de la clase `GestionCitas` para agregar una nueva cita.
- `cancelar_cita()`: Lee los datos de entrada y llama a `cancelar_cita` de la clase `GestionCitas` para cancelar una cita existente.
- `mostrar_citas()`: Muestra todas las citas registradas utilizando `mostrar_citas` de la clase `GestionCitas`.
- `generar_reporte()`: Genera un reporte en formato JSON utilizando `generar_reporte_json` de la clase `GestionCitas`.

## Uso

1. **Ejecutar la Aplicación**: Ejecuta el archivo `main.py` para iniciar la aplicación.
2. **Agendar una Cita**: Introduce el nombre del paciente, nombre del médico, fecha y hora, y haz clic en "Agendar Cita".
3. **Cancelar una Cita**: Introduce el nombre del paciente, fecha y hora de la cita que deseas cancelar, y haz clic en "Cancelar Cita".
4. **Mostrar Citas**: Haz clic en "Mostrar Citas" para ver todas las citas registradas.
5. **Generar Reporte JSON**: Haz clic en "Generar Reporte JSON" para obtener un reporte de todas las citas en formato JSON.

## Requisitos

- Python 3.x
- Tkinter 

## Autor

- Santiago Ruiz

