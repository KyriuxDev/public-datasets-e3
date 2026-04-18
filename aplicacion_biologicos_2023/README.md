# Aplicación de Biológicos 2023

Registro de vacunas y biológicos aplicados en México durante 2023, publicado por la Secretaría de Salud a través del portal de Datos Abiertos del Gobierno Federal.

## Diccionario de Datos

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `entidad_federativa` | `String` | Estado donde se aplicó el biológico |
| `municipio` | `String` | Municipio o alcaldía correspondiente |
| `unidad_medica` | `String` | Nombre de la unidad de salud |
| `tipo_biologico` | `String` | Nombre del biológico o vacuna aplicada |
| `dosis` | `String` | Número o tipo de dosis (primera, segunda, refuerzo) |
| `grupo_edad` | `String` | Rango etario del paciente |
| `sexo` | `String` | Sexo del paciente (M/F) |
| `fecha_aplicacion` | `Date` | Fecha en que se realizó la aplicación |
| `cantidad` | `Int` | Total de dosis aplicadas en el registro |

## Fuente

[datos.gob.mx — Aplicación de Vacunas](https://www.datos.gob.mx/dataset/aplicacion_vacunas/resource/aab4dbaf-a4e7-4078-85bb-0998ae842463)
