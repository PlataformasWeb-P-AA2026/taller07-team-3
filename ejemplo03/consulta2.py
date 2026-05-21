from sqlalchemy.orm import sessionmaker
from clases import engine, Curso, Instructor

Session = sessionmaker(bind=engine)
session = Session()

# Filtramos usando un JOIN con Instructor y el operador LIKE
cursos = session.query(Curso).join(Instructor).filter(Instructor.nombre.like('%Zam%')).all()

print(f"{'Curso':<40} | {'Profesor (Contiene Zam)':<30}")
print("-" * 75)

for c in cursos:
    print(f"{c.titulo:<40} | {c.instructor.nombre:<30}")

session.close()