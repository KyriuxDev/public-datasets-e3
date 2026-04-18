#  Amazon Top 50 Best Sellers (México y Brasil)

---

##  Descripción
Este conjunto de datos contiene el registro histórico del **Top 50 de los productos más vendidos** en Amazon para los mercados de México y Brasil. Los datos fueron obtenidos mediante *web scraping* y capturan las tendencias de ventas hora tras hora.

> **Nota:** En este repositorio se incluye un ejemplo procesado de la categoría de videojuegos (`mx-videogames.txt`), el cual está estructurado con valores separados por barras verticales (`|`).

---

##  Diccionario de Datos

Cada archivo de esta base de datos incluye las siguientes columnas, detalladas a continuación:

| Columna | Tipo de Dato | Descripción |
| :--- | :--- | :--- |
| **`time`** | `Datetime` | Fecha y hora exacta (`%Y-%m-%d %H-%M`) en la que se realizó la extracción de datos. |
| **`Rank`** | `Float` | Posición del producto en la lista del Top 50. |
| **`Product Names`** | `String` | Nombre completo del producto tal como lo publicó el vendedor. |
| **`Stars`** | `Float` | Promedio de calificación otorgado por las reseñas de los clientes. |
| **`Reviews`** | `Int` | Número total de reseñas acumuladas desde que el producto está a la venta. |
| **`Authors/Company`** | `String` | Autor de la obra (libros/música) o la empresa fabricante del artículo. |
| **`Edition/Console`** | `String` | Especificación de plataforma para videojuegos (ej. *Xbox One, PS4*), tipo de pasta para libros o formato para música. |
| **`Price_std_or_min`** | `Float` | Precio estándar del producto. Si Amazon muestra un rango, representa el precio mínimo. |
| **`Max_prices`** | `Float` | Precio máximo asignado por el algoritmo de Amazon (si tiene un rango variable). |

---

## 🔗 Fuente de los Datos

* **Autor Original:** Edward Toledo López
* **Enlace Oficial:** [Kaggle - Amazon Mexico Top 50 Best Sellers](https://www.kaggle.com/datasets/edwardtoledolpez/amazon-mexico-top-50-best-sellers)
