# Stats NZ — Annual Enterprise Survey 2024

Encuesta anual de empresas de Nueva Zelanda correspondiente al año fiscal 2024 (datos provisionales), publicada por **Statistics New Zealand (Stats NZ)**. Contiene indicadores financieros desagregados por industria, clasificados según el estándar **NZSIOC** (New Zealand Standard Industry Output Categories).

El dataset cuenta con **55,620 registros** y cubre métricas de rendimiento financiero, posición financiera y ratios financieros para todos los sectores de la economía neozelandesa.

## Niveles de Agregación

| Nivel | Descripción |
| :--- | :--- |
| `Level 1` | Todas las industrias en conjunto |
| `Level 3` | Agrupaciones de sectores |
| `Level 4` | Industrias específicas |

## Categorías de Variables

| Categoría | Ejemplos |
| :--- | :--- |
| `Financial performance` | Total income, Total expenditure, Salaries and wages |
| `Financial position` | Total assets, Current liabilities, Shareholders funds |
| `Financial ratios` | Current ratio, Quick ratio, Return on equity |

## Diccionario de Datos

| Columna | Tipo | Descripción |
| :--- | :--- | :--- |
| `Year` | `Int` | Año fiscal del registro |
| `Industry_aggregation_NZSIOC` | `String` | Nivel de agregación (Level 1, 3 o 4) |
| `Industry_code_NZSIOC` | `String` | Código de industria según clasificación NZSIOC |
| `Industry_name_NZSIOC` | `String` | Nombre de la industria |
| `Units` | `String` | Unidad de medida (Dollars, Dollars (millions), Percentage) |
| `Variable_code` | `String` | Código de la variable financiera (H01–H41) |
| `Variable_name` | `String` | Nombre descriptivo de la variable |
| `Variable_category` | `String` | Categoría de la variable financiera |
| `Value` | `Float` | Valor numérico del indicador |
| `Industry_code_ANZSIC06` | `String` | Código de industria según clasificación ANZSIC06 |

## Fuente

[stats.govt.nz — Large Datasets CSV](https://www.stats.govt.nz/large-datasets/csv-files-for-download/)
