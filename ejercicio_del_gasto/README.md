# Ejercicio del Gasto Federalizado (México)

---

## Descripción

Este conjunto de datos contiene el **registro detallado de cómo se ejercieron los recursos federales transferidos a los estados y municipios de México**, trimestre a trimestre. Los datos fueron publicados por la **Secretaría de Hacienda y Crédito Público (SHCP)** a través del Portal de Transparencia Presupuestaria y se reportan en el marco del artículo 85 de la Ley Federal de Presupuesto y Responsabilidad Hacendaria.

Esta base es especialmente útil para rastrear a qué programa, función, partida de gasto y estado terminaron llegando los recursos federales. Permite saber, por ejemplo, cuánto gastó Oaxaca en infraestructura educativa con recursos del Ramo 33, o qué parte del presupuesto aprobado para salud en Guerrero efectivamente se pagó.

---

## Diccionario de Datos

Cada registro de esta base de datos incluye las siguientes columnas:

| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| **`CICLO`** | `Integer` | Año fiscal al que corresponde el reporte del gasto. |
| **`TRIMESTRE`** | `Integer` | Trimestre del año en que se reporta (1 al 4). Los montos son acumulados desde enero. |
| **`ID_ENTIDAD_FEDERATIVA`** | `Integer` | Clave numérica INEGI del estado que ejerció los recursos. |
| **`ENTIDAD_FEDERATIVA`** | `String` | Nombre del estado o entidad federativa que ejerció los recursos. |
| **`ID_MUNICIPIO`** | `Integer` | Clave numérica INEGI del municipio. El valor `0` indica que el gasto corresponde al gobierno estatal en su conjunto. |
| **`MUNICIPIO`** | `String` | Nombre del municipio que ejerció los recursos. Si es `Gobierno de la Entidad`, el gasto es del gobierno estatal. |
| **`ID_TIPO_DE_REGISTRO`** | `Integer` | Código que indica el nivel de detalle del registro. |
| **`TIPO_DE_REGISTRO`** | `String` | Indica si la fila corresponde al nivel de *Programa Presupuestario* o de *Partida Genérica*. |
| **`CICLO_RECURSO`** | `Integer` | Año fiscal de origen de los recursos (puede diferir de `CICLO` si son recursos de ejercicios anteriores). |
| **`ID_TIPO_RECURSO`** | `Integer` | Clave del tipo de recurso federal transferido. |
| **`TIPO_RECURSO`** | `String` | Clasificación del recurso: *Participaciones*, *Aportaciones Federales*, *Subsidios y Convenios*, etc. |
| **`ID_RAMO`** | `Integer` | Clave del ramo presupuestario federal de origen (ej. `28` = Participaciones, `33` = Aportaciones). |
| **`DESC_RAMO`** | `String` | Nombre del ramo presupuestario (ej. *Educación Pública*, *Salud*, *Gobernación*). |
| **`MODALIDAD_PP`** | `String` | Clave de modalidad del programa presupuestario (ej. `U` = Otros de apoyo, `K` = Proyectos de inversión). |
| **`DESC_PP`** | `String` | Nombre del programa presupuestario federal que originó la transferencia (ej. *Subsidios para organismos descentralizados estatales*). |
| **`PROG_FONDO_CONVENIO_ESPECIFICO`** | `String` | Clave específica del fondo, convenio o programa (ej. folio del proyecto o número de convenio). |
| **`INSTITUCION_EJECUTORA`** | `String` | Nombre del organismo o institución que ejecutó el gasto a nivel local. |
| **`ID_TIPO_GASTO`** | `Integer` | Clave que clasifica el gasto según su naturaleza económica. |
| **`DESC_TIPO_GASTO`** | `String` | Descripción del tipo de gasto: *Gasto corriente* (operación y servicios) o *Gasto de inversión* (obra e infraestructura). |
| **`ID_PARTIDA_GENERICA`** | `Integer` | Clave del capítulo y concepto del Clasificador por Objeto del Gasto (ej. `1000` = Servicios personales, `6000` = Inversión pública). |
| **`DESC_PARTIDA_GENERICA`** | `String` | Descripción de la partida genérica (ej. *Aportaciones de seguridad social*, *Obra pública en bienes propios*). |
| **`MONTO_APROBADO`** | `Numeric` | Presupuesto original autorizado por la Cámara de Diputados para el programa, en pesos. |
| **`MONTO_MODIFICADO`** | `Numeric` | Presupuesto vigente tras adecuaciones presupuestarias al monto original, en pesos. |
| **`MONTO_RECAUDADO`** | `Numeric` | Recursos efectivamente recibidos por el estado o municipio desde la federación, en pesos. |
| **`MONTO_COMPROMETIDO`** | `Numeric` | Recursos para los que ya existe un acto administrativo o contrato firmado, pero aún no se han pagado, en pesos. |
| **`MONTO_DEVENGADO`** | `Numeric` | Recursos cuya obligación de pago ya fue reconocida (el bien o servicio fue entregado o la obra ejecutada), en pesos. |
| **`MONTO_EJERCIDO`** | `Numeric` | Recursos devengados más los pagos realizados a cuenta de ejercicios anteriores, en pesos. |
| **`MONTO_PAGADO`** | `Numeric` | Recursos efectivamente desembolsados (cheque cobrado o transferencia realizada), en pesos. Es el dato más representativo del gasto real. |
| **`OBSERVACIONES_CAPTURISTA`** | `String` | Notas o comentarios libres capturados por el responsable del reporte en la entidad federativa. Puede estar vacío. |

---

## Fuente de los Datos

* **Institución:** Secretaría de Hacienda y Crédito Público (SHCP) — Portal de Transparencia Presupuestaria
* **Enlace Oficial:** [transparenciapresupuestaria.gob.mx — Datos Abiertos](https://www.transparenciapresupuestaria.gob.mx/Datos-Abiertos)