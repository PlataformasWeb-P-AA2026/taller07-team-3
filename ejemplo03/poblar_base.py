import csv
from datetime import datetime
from sqlalchemy.orm import sessionmaker
# Asegúrate de que tu modelo esté guardado como clases.py o el nombre que uses
from clases import engine, Departamento, Instructor, Curso, Estudiante, Inscripcion, Tarea, Entrega

# Crear la sesión
Session = sessionmaker(bind=engine)
session = Session()

def parse_fecha(fecha_str):
    """Función auxiliar para convertir texto a datetime"""
    if not fecha_str:
        return None
    # Ajusta el formato '%Y-%m-%d %H:%M:%S' según cómo vengan tus CSV
    try:
        return datetime.strptime(fecha_str.strip(), '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return datetime.strptime(fecha_str.strip(), '%Y-%m-%d')

try:
    # 01_departamento.csv (id, nombre)
    with open('01_departamento.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',') # Cambia el delimiter si es necesario
        for row in reader:
            session.add(Departamento(id=int(row['id']), nombre=row['nombre']))
    print("Departamentos cargados.")

    # 02_instructor.csv (id, nombre)
    with open('02_instructor.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            session.add(Instructor(id=int(row['id']), nombre=row['nombre']))
    print("Instructores cargados.")

    # 03_curso.csv (id, titulo, departamento_id, instructor_id)
    with open('03_curso.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            session.add(Curso(
                id=int(row['id']),
                titulo=row['titulo'],
                departamento_id=int(row['departamento_id']),
                instructor_id=int(row['instructor_id'])
            ))
    print("Cursos cargados.")

    # 04_estudiante.csv (id, nombre)
    with open('04_estudiante.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            session.add(Estudiante(id=int(row['id']), nombre=row['nombre']))
    print("Estudiantes cargados.")

    # 05_inscripcion.csv (estudiante_id, curso_id, fecha_inscripcion)
    with open('05_inscripcion.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            session.add(Inscripcion(
                estudiante_id=int(row['estudiante_id']),
                curso_id=int(row['curso_id']),
                fecha_inscripcion=parse_fecha(row['fecha_inscripcion'])
            ))
    print("Inscripciones cargadas.")

    # 06_tarea.csv (id, curso_id, titulo, fecha_entrega)
    with open('06_tarea.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            session.add(Tarea(
                id=int(row['id']),
                curso_id=int(row['curso_id']),
                titulo=row['titulo'],
                fecha_entrega=parse_fecha(row['fecha_entrega'])
            ))
    print("Tareas cargadas.")

    # 07_entrega.csv (id, tarea_id, estudiante_id, fecha_envio, calificacion)
    with open('07_entrega.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            session.add(Entrega(
                id=int(row['id']),
                tarea_id=int(row['tarea_id']),
                estudiante_id=int(row['estudiante_id']),
                fecha_envio=parse_fecha(row['fecha_envio']),
                calificacion=float(row['calificacion']) if row['calificacion'] else None
            ))
    print("Entregas cargadas.")

    # Guardar cambios en la base de datos
    session.commit()
    print("¡Base de datos poblada con éxito!")

except Exception as e:
    session.rollback()
    print(f"Error durante la carga, se hizo rollback: {e}")
finally:
    session.close()