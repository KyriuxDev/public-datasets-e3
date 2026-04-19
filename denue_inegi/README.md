# Directorio Estadístico Nacional de Unidades Económicas (DENUE - INEGI)

---

## Descripción
Este repositorio contiene la base de datos completa del **DENUE** (Directorio Estadístico Nacional de Unidades Económicas), proporcionada por el **INEGI**. Este dataset es una herramienta fundamental para conocer la geografía económica de México, ya que permite identificar y ubicar todos los establecimientos que realizan actividades económicas en el territorio nacional.

---

## Estructura de los Datos

El archivo presenta una estructura de valores separados por comas (CSV) con 42 campos de información detallada:

### 1. Identificación y Actividad
| Columna | Descripción |
| :--- | :--- |
| **`id`** | Identificador único y permanente del establecimiento. |
| **`clee`** | Clave de Llave de Establecimiento Económico. |
| **`nom_estab`** | Nombre comercial de la unidad económica. |
| **`raz_social`** | Razón social de la empresa o nombre del propietario. |
| **`codigo_act`** | Código de actividad según el SCIAN. |
| **`nombre_act`** | Descripción de la actividad económica. |
| **`per_ocu`** | Estrato de personal ocupado (ej. 0 a 5 personas). |
| **`tipoUniEco`** | Tipo de unidad económica (Fijo o Semifijo). |

### 2. Ubicación Geográfica y Domicilio
| Columna | Descripción |
| :--- | :--- |
| **`tipo_vial` / `nom_vial`** | Tipo y nombre de la vialidad principal. |
| **`tipo_v_e_1,2,3`** | Tipos de vialidades entre las que se ubica (entre calles). |
| **`nom_v_e_1,2,3`** | Nombres de las vialidades colindantes. |
| **`numero_ext` / `letra_ext`** | Número exterior y letra (si aplica). |
| **`edificio` / `edificio_e`** | Nombre y piso del edificio o centro comercial. |
| **`numero_int` / `letra_int`** | Número interior y letra de la oficina/local. |
| **`tipo_asent` / `nomb_asent`** | Tipo y nombre del asentamiento (Colonia, Barrio, etc.). |
| **`tipoCenCom` / `nom_CenCom`** | Tipo y nombre del centro comercial. |
| **`num_local`** | Número de local dentro del centro comercial. |
| **`cod_postal`** | Código postal de 5 dígitos. |

### 3. Georreferenciación y Administración
| Columna | Descripción |
| :--- | :--- |
| **`cve_ent` / `entidad`** | Clave y nombre del estado de la República. |
| **`cve_mun` / `municipio`** | Clave y nombre del municipio o demarcación. |
| **`cve_loc` / `localidad`** | Clave y nombre de la localidad. |
| **`ageb` / `manzana`** | Claves de Áreas Geográficas Estadísticas Básicas. |
| **`latitud` / `longitud`** | Coordenadas geográficas para mapas. |

### 4. Contacto y Registro
| Columna | Descripción |
| :--- | :--- |
| **`telefono`** | Número telefónico de contacto. |
| **`correoelec`** | Correo electrónico del establecimiento. |
| **`www`** | Página de internet o red social oficial. |
| **`fecha_alta`** | Mes y año de incorporación al DENUE. |

---

## Detalles Técnicos
* **Fuente:** [INEGI - Directorio Estadístico Nacional de Unidades Económicas](https://www.inegi.org.mx/app/descarga/default.html)
* **Formato:** CSV (Delimitado por comas).
* **Cobertura:** Nacional (México).

---

## Sobre la Fuente
El **INEGI** es el organismo encargado de captar y difundir información de México. El DENUE es uno de sus productos más utilizados para entender la dinámica empresarial del país.
