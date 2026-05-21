from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from genera_tablas import Club, Jugador
from configuracion import cadena_base_datos

# configuracion de la conexion a la base de datos y creacion de la sesion
engine = create_engine(cadena_base_datos)
Session = sessionmaker(bind=engine)
session = Session()

# se abre el archivo de texto que contiene los datos de los clubes en modo lectura
with open("data/datos_clubs.txt", "r", encoding="utf-8") as archivo_clubs:
    for linea in archivo_clubs:
        datos = linea.strip().split(";")
        
        if len(datos) == 3:
            nombre_club = datos[0].strip()
        
            club_existe = session.query(Club).filter_by(nombre=nombre_club).first()
            
            # si el club no existe, recien ahi se crea y se agrega
            if not club_existe:
                club = Club(
                    nombre=nombre_club,
                    deporte=datos[1].strip(),
                    fundacion=int(datos[2].strip())
                )
                session.add(club)

# se guardan los clubes para que el metodo .one() de abajo los pueda encontrar
session.commit()

# se abre el archivo de texto de los jugadores en modo lectura
with open("data/datos_jugadores.txt", "r", encoding="utf-8") as archivo_jugadores:
    for linea in archivo_jugadores:
        datos = linea.strip().split(";")
        
        if len(datos) == 4:
            nombre_club_buscado = datos[0].strip()
            
            # se busca el club de forma segura garantizando que exista un unico registro previo
            club_asociado = session.query(Club).filter_by(nombre=nombre_club_buscado).one()
            
            # creacion del objeto jugador vinculandolo directamente con el club
            jugador = Jugador(
                nombre=datos[3].strip(),     # nombre en la posicion 3
                posicion=datos[1].strip(),   # posicion en la posicion 1
                dorsal=int(datos[2].strip()),# dorsal en la posicion 2
                club=club_asociado           # usa la relacion configurada en tu genera_tablas
            )
            session.add(jugador)
            
# se confirman y guardan definitivamente todas las transacciones de los jugadores
session.commit()