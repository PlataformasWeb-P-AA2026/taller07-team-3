## Indicaciones

1. Crear las entidades en función de clases.py
2. Crear un archivo que permita poblar la base de datos; usar los csv's dados

Orden sugerido de carga:

- 01_departamento.csv
- 02_instructor.csv
- 03_curso.csv
- 04_estudiante.csv
- 05_inscripcion.csv
- 06_tarea.csv
- 07_entrega.csv

3. Generar los siguiente archivos

* consulta1.py: Listas las entregas, presentar por cada entrega: nombre del estudiantes, titulo, nombre del profesor
* consulta2.py: Listar los cursos, obtener los cursos profesores en su nombre tengan la cadena "Zam"
* consulta3.py: Listar las inscripciones del departamento de Ciencias de la Computación. Por cada inscripción, presentar el nombre del estudiante, el nombre del curso y el nombre del profesor
* consulta4.py: Por cada curso, presentar sus tareas asociadas.

# Evidencias de Taller: Modelado de Datos y Consultas Complejas (Ejemplo03)

Este repositorio contiene la solución a las actividades del taller práctico sobre el manejo de relaciones múltiples y carga de datos desde archivos CSV utilizando SQLAlchemy ORM.

## Actividades Realizadas

1. **Creación de Entidades:** Configuración del esquema relacional en la base de datos a partir de los modelos definidos en `clases.py`.
2. **Población de la Base de Datos:** Desarrollo del script de automatización para cargar y procesar los archivos `.csv` en el orden secuencial sugerido.
3. **Desarrollo de Consultas:** Creación de scripts específicos (`consulta1.py` a `consulta4.py`) para extraer información combinada mediante filtros y uniones (Joins).

---

##  Orden de Ejecución y Evidencias

A continuación se detalla el orden estricto de ejecución de los scripts junto con los espacios asignados para adjuntar las capturas de pantalla como evidencia.

Evidencia:

### 1. Ejecución y Verificación de Consultas
### Consulta 1
Listar las entregas presentando por cada una: nombre del estudiante, título de la tarea y nombre del profesor.

```bash
python3 consulta1.py
```
Evidencia:
![Captura de pantalla](/capturas/1.png)

### Consulta 2
Listar los cursos cuyos profesores tengan la cadena "Zam" en su nombre.
```bash
python3 consulta2.py
```
Evidencia:
![Captura de pantalla](/capturas/2.png)

### Consulta 3
Listar las inscripciones pertenecientes al departamento de "Ciencias de la Computación", presentando: nombre del estudiante, nombre del curso y nombre del profesor.
```bash
python3 consulta3.py
```
Evidencia:
![Captura de pantalla](/capturas/3.png)

### Consulta 4
Listar las tareas asociadas a cada uno de los cursos registrados.

```bash
python3 consulta4.py
```
Evidencia:
![Captura de pantalla](/capturas/4.png)

