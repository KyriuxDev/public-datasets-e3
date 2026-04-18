# Incidencia Delictiva Estatal

Datos sobre la incidencia de delitos por entidad federativa en México, publicados mensualmente por el Secretariado Ejecutivo del Sistema Nacional de Seguridad Pública (SESNSP).

## Diccionario de Datos

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `entidad` | `String` | Nombre de la entidad federativa |
| `año` | `Int` | Año del registro |
| `mes` | `String` | Mes del registro |
| `bien_juridico` | `String` | Bien jurídico afectado (ej. vida, patrimonio) |
| `tipo_delito` | `String` | Clasificación general del delito |
| `subtipo_delito` | `String` | Clasificación específica del delito |
| `modalidad` | `String` | Modalidad o variante del delito |
| `carpetas_investigacion` | `Int` | Número de carpetas de investigación abiertas |

## Fuente

[datos.gob.mx — Incidencia Delictiva](https://www.datos.gob.mx/dataset/incidencia_delictiva/resource/d9b2792a-33a2-4ea8-8527-210d9e99de5e)
