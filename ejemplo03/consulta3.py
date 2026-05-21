from sqlalchemy.orm import sessionmaker
from clases import engine, Inscripcion, Curso, Departamento

Session = sessionmaker(bind=engine)
session = Session()

# Entramos por Inscripcion, unimos con Curso y luego con Departamento para filtrar
inscripciones = session.query(Inscripcion)\
    .join(Curso)\
    .join(Departamento)\
    .filter(Departamento.nombre == "Ciencias de la Computación")\
    .all()

print(f"{'Estudiante':<30} | {'Curso':<40} | {'Profesor':<30}")
print("-" * 106)

for i in inscripciones:
    print(f"{i.estudiante.nombre:<30} | {i.curso.titulo:<40} | {i.curso.instructor.nombre:<30}")

session.close()