# Directorio Estadístico Nacional de Unidades Económicas (DENUE - INEGI)

---

##  Descripción
Este repositorio contiene la base de datos completa del **DENUE** (Directorio Estadístico Nacional de Unidades Económicas), proporcionada por el **INEGI**. Este dataset es una herramienta fundamental para conocer la geografía económica de México, ya que permite identificar y ubicar todos los establecimientos que realizan actividades económicas en el territorio nacional.

---

##  Estructura de los Datos 

El archivo presenta una estructura de valores separados por comas (CSV) con información detallada de cada unidad económica:

| Columna | Descripción |
| :--- | :--- |
| **`id`** | Identificador único y permanente del establecimiento. |
| **`clee`** | Clave de Llave de Establecimiento Económico (estándar INEGI). |
| **`nom_estab`** | Nombre comercial o denominación de la unidad económica. |
| **`nombre_act`** | Descripción detallada de la actividad económica (SCIAN). |
| **`per_ocu`** | Rango de personal que labora en el lugar (ej. 0-5, 6-10 personas). |
| **`codigo_act`** | Código de actividad según el Sistema de Clasificación Industrial de América del Norte. |
| **`municipio`** | Municipio o demarcación territorial de ubicación. |
| **`entidad`** | Estado de la República Mexicana al que pertenece. |
| **`latitud / longitud`** | Coordenadas geográficas de alta precisión para georreferenciación. |
| **`fecha_alta`** | Mes y año en el que el establecimiento se incorporó al directorio. |

---

## Detalles Técnicos
* **Fuente:** [INEGI - Directorio Estadístico Nacional de Unidades Económicas](https://www.inegi.org.mx/app/descarga/default.html)
* **Formato:** CSV / Texto enriquecido.
* **Cobertura:** Nacional (México).
* **Utilidad:** Ideal para análisis estadísticos, estudios de mercado, logística de suministros y planeación urbana.

---

##  Sobre la Fuente
El **INEGI** es el organismo encargado de captar y difundir información de México. El DENUE es uno de sus productos más utilizados por investigadores y empresas para entender la dinámica empresarial del país.
