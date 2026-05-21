from sqlalchemy.orm import sessionmaker
from clases import engine, Entrega

Session = sessionmaker(bind=engine)
session = Session()

entregas = session.query(Entrega).all()

print(f"{'Estudiante':<30} | {'Tarea':<30} | {'Profesor':<30}")
print("-" * 96)

for e in entregas:
    nombre_estudiante = e.estudiante.nombre
    titulo_tarea = e.tarea.titulo
    # Accedemos al profesor/instructor a través de la relación de la tarea con el curso
    nombre_profesor = e.tarea.curso.instructor.nombre
    
    print(f"{nombre_estudiante:<30} | {titulo_tarea:<30} | {nombre_profesor:<30}")

session.close()