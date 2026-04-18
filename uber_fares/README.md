# Uber Fares Dataset (Nueva York)

---

## Descripción

Este conjunto de datos contiene el registro de **200,000 viajes de Uber realizados en la ciudad de Nueva York**, incluyendo la tarifa cobrada, la ubicación de origen y destino, la fecha y hora del viaje, y el número de pasajeros. Es un dataset de uso libre publicado en **Kaggle** y se utiliza principalmente para ejercicios de análisis de datos y aprendizaje automático, en particular para construir modelos de predicción de tarifas (*regresión*).

---

## Diccionario de Datos

Cada registro de esta base de datos incluye las siguientes columnas:

| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| **`Unnamed: 0`** | `Integer` | Índice numérico autogenerado al exportar el dataset. No tiene significado propio, es solo el número de fila. |
| **`key`** | `String` | Identificador único del viaje. Generalmente tiene el formato de una marca de tiempo con microsegundos (ej. `2009-06-15 17:26:21.0000001`). |
| **`fare_amount`** | `Float` | Tarifa cobrada por el viaje en dólares americanos (USD). Puede incluir valores negativos o cercanos a cero que son errores de captura. |
| **`pickup_datetime`** | `Datetime` | Fecha y hora en que el taxímetro fue activado, es decir, cuando inició el viaje (formato `YYYY-MM-DD HH:MM:SS UTC`). |
| **`pickup_longitude`** | `Float` | Longitud geográfica del punto donde se recogió al pasajero. Para NYC, los valores válidos están aproximadamente entre `-74.5` y `-72.8`. |
| **`pickup_latitude`** | `Float` | Latitud geográfica del punto donde se recogió al pasajero. Para NYC, los valores válidos están aproximadamente entre `40.5` y `41.8`. |
| **`dropoff_longitude`** | `Float` | Longitud geográfica del punto donde se dejó al pasajero al final del viaje. |
| **`dropoff_latitude`** | `Float` | Latitud geográfica del punto donde se dejó al pasajero al final del viaje. |
| **`passenger_count`** | `Integer` | Número de pasajeros en el vehículo. Es un valor capturado manualmente por el conductor, por lo que puede haber errores (ej. valores de `0` o superiores a `6`). |

---

## Fuente de los Datos

* **Autor Original:** Yassir H.
* **Enlace Oficial:** [Kaggle — Uber Fares Dataset](https://www.kaggle.com/datasets/yasserh/uber-fares-dataset)