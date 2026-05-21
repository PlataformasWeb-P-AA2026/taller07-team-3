from sqlalchemy.orm import sessionmaker
from clases import engine, Curso

Session = sessionmaker(bind=engine)
session = Session()

cursos = session.query(Curso).all()

for c in cursos:
    print(f"\nCurso: {c.titulo}")
    print(f"Tareas asociadas:")
    if not c.tareas:
        print("  - No hay tareas asignadas a este curso.")
    else:
        for t in c.tareas:
            print(f"  * Tarea: {t.titulo} (Fecha de entrega: {t.fecha_entrega})")
    print("-" * 50)

session.close()
