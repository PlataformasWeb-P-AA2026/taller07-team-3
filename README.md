## Actividad

* Realizar las actividades descritas en el README de la carpeta **ejemplo02**


# Evidencias de Taller: Persistencia de Datos con SQLAlchemy

Este repositorio contiene la solución a las actividades del taller práctico sobre el manejo de bases de datos relacionales utilizando Python y SQLAlchemy ORM.

## Actividades Realizadas

1. **Migración de Archivos Base:** Se copiaron los archivos de configuración y consulta desde la carpeta `ejemplo01`.
2. **Desarrollo de `ingreso_datos.py`:** Creación del script para leer de forma dinámica los archivos de texto plano dentro de la carpeta `data` (`datos_clubs.txt` y `datos_jugadores.txt`) e insertar los registros en las entidades **Club** y **Jugador**.

---

##  Orden de Ejecución y Evidencias

### 1. Generación de Tablas
Crea la estructura de la base de datos basada en los modelos definidos.
```bash
python3 genera_tablas.py
```
![Captura del taller](./capturas/generar_tabla.png)

### 2.Ingreso de Datos
Pobla las tablas Club y Jugador procesando los archivos .txt de la carpeta data.
```bash
python3 ingreso_datos.py
```

![Captura del taller](./capturas/ingreso_datos.png)
### 3. Ejecución de Consultas de Datos
Validación de la información almacenada en el sistema mediante los scripts de consulta previstos.

### Consulta 1
```bash
python3 consulta_datos1.py
```

![Captura del taller](./capturas/consulta1.png)
### Consulta 2
```bash
python3 consulta_datos2.py
```

![Captura del taller](./capturas/consulta2.png)
### Consulta 3
```bash
python3 consulta_datos3.py
```

![Captura del taller](./capturas/consulta3.png)
### Consulta 4
```bash
python3 consulta_datos4.py
```
![Captura del taller](./capturas/consulta4.png)


# Evidencias de Taller: Modelado de Datos y Consultas Complejas (Ejemplo03)

Este repositorio contiene la solución a las actividades del taller práctico sobre el manejo de relaciones múltiples y carga de datos desde archivos CSV utilizando SQLAlchemy ORM.

## Actividades Realizadas

1. **Creación de Entidades:** Configuración del esquema relacional en la base de datos a partir de los modelos definidos en `clases.py`.
2. **Población de la Base de Datos:** Desarrollo del script de automatización para cargar y procesar los archivos `.csv` en el orden secuencial sugerido.
3. **Desarrollo de Consultas:** Creación de scripts específicos (`consulta1.py` a `consulta4.py`) para extraer información combinada mediante filtros y uniones (Joins).

---

##  Orden de Ejecución y Evidencias

A continuación se detalla el orden estricto de ejecución de los scripts junto con los espacios asignados para adjuntar las capturas de pantalla como evidencia.

### 1. Generación del Esquema de Base de Datos
Creación de las tablas basadas en las clases de mapeo.
```bash
python clases.py
