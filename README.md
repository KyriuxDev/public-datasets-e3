# Public Datasets

Coleccion de bases de datos publicas en formato CSV, junto con un migrador
universal para cargarlas en PostgreSQL.

## Índice

1. [Equipo 3](#equipo-3)
2. [Requisitos](#requisitos)
3. [Configuracion](#configuracion)
4. [Uso](#uso)
5. [Conjuntos de datos](#conjuntos-de-datos)

## **Equipo 3**

- Almaraz Vásquez Alonso David
- Cruz Alonso Kelly Adanari
- Delgado Molina Karla Rocío
- Martínez Martínez Jesús Alexander
- Martínez Guzmán Julián
- Roque Hernández Diego Misael


## Requisitos

- Python 3.9 o superior
- Una instancia de PostgreSQL accesible

---

## Configuracion

1. Clona el repositorio:

```bash
git clone <url-del-repositorio>
cd public-datasets
```

2. Copia el archivo de ejemplo y ajusta tus credenciales:

```bash
cp .env.example .env
```

Edita `.env` con los valores de tu instancia de PostgreSQL:

```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=tu_contrasena
DB_SCHEMA=public
```

3. Instala las dependencias Python:

```bash
pip install psycopg2-binary python-dotenv
```

---

## Uso

```bash
python csv_to_postgres.py <ruta/al/archivo.csv> [nombre_tabla]
```

Ejemplos:

```bash
python csv_to_postgres.py denue_inegi/denue_inegi_20_.csv
python csv_to_postgres.py ejercicio_del_gasto/ejercicio_del_gasto.csv gasto_2024
python csv_to_postgres.py uber_fares/uber.csv uber_fares
```

El script detecta encoding y delimitador, infiere tipos de datos, crea la
tabla si no existe y carga los datos en lotes. Solicita confirmacion antes
de insertar.

---

## Conjuntos de datos

| Carpeta                         | Fuente                                                                    |
|---------------------------------|---------------------------------------------------------------------------|
| `amazon_video_games/`           | Kaggle - Amazon Mexico Top 50 Best Sellers                                |
| `aplicacion_biologicos_2023/`   | datos.gob.mx - Aplicacion de vacunas 2023                                 |
| `companies_house/`              | Companies House UK - Basic Company Data                                   |
| `denue_inegi/`                  | INEGI - Directorio Estadistico Nacional de Unidades Economicas            |
| `ejercicio_del_gasto/`          | Transparencia Presupuestaria - Datos Abiertos                             |
| `incidencia_delectiva_estatal/` | datos.gob.mx - Incidencia delictiva estatal                               |
| `stats_govt_nz/`                | Stats NZ - Annual Enterprise Survey 2024                                  |
| `transferencias_federales/`     | datos.gob.mx - Transferencias a entidades federativas                     |
| `uber_fares/`                   | Kaggle - Uber Fares                                                       |

---