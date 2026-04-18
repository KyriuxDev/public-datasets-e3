# Producto de Datos Empresariales Gratuito

## Descripción
Este conjunto de datos corresponde a una instantánea descargable que contiene información básica de empresas registradas. Los datos incluyen información de identificación, dirección, estado legal, cuentas financieras, hipotecas y clasificación industrial.

El producto está diseñado para facilitar el análisis empresarial, la consulta de registros corporativos y la integración en sistemas de información.

La información se distribuye en archivos comprimidos y estructurados para su uso en herramientas de análisis o sistemas gestores de bases de datos.

---

## Actualización de los Datos
La instantánea se actualiza dentro de los 5 días hábiles posteriores al cierre de cada mes.

El contenido incluye información recopilada hasta el final del mes anterior, por lo que representa un corte mensual de los registros empresariales.

---

## Diccionario de Datos

Cada registro incluye las siguientes columnas:

| Columna | Tipo de Dato | Descripción |
|--------|-------------|------------|
| _paquete | Bigint | Identificador único de la empresa (clave primaria). |
| company_name | Text | Nombre de la empresa. |
| company_number | Text | Número de registro de la empresa. |
| regaddress_careof | Text | Información adicional del domicilio. |
| regaddress_pobox | Text | Apartado postal. |
| regaddress_addressline1 | Text | Dirección principal. |
| regaddress_addressline2 | Text | Segunda línea de dirección. |
| regaddress_posttown | Text | Ciudad. |
| regaddress_county | Text | Región o estado. |
| regaddress_country | Text | País. |
| regaddress_postcode | Text | Código postal. |
| company_category | Text | Tipo de empresa (ej. Sociedad Limitada Privada). |
| company_status | Text | Estado de la empresa (ej. Activa, Disuelta). |
| country_of_origin | Text | País de origen. |
| dissolution_date | Date | Fecha de disolución (si aplica). |
| incorporation_date | Date | Fecha de constitución. |
| accounts_account_ref_day | Integer | Día de referencia contable. |
| accounts_account_ref_month | Integer | Mes de referencia contable. |
| accounts_next_due_date | Date | Próxima fecha de entrega de cuentas. |
| accounts_last_made_up_date | Date | Última actualización de cuentas. |
| accounts_category | Text | Categoría de cuentas. |
| returns_next_due_date | Date | Próxima fecha de declaración. |
| returns_last_made_up_date | Date | Última declaración realizada. |
| mortgages_num_charges | Integer | Número total de hipotecas registradas. |
| mortgages_num_outstanding | Integer | Hipotecas pendientes. |
| mortgages_num_part_satisfied | Integer | Hipotecas parcialmente satisfechas. |
| mortgages_num_satisfied | Integer | Hipotecas liquidadas. |
| sic_code_1 | Text | Código SIC principal. |
| sic_code_2 | Text | Código SIC secundario. |
| sic_code_3 | Text | Código SIC adicional. |
| sic_code_4 | Text | Código SIC adicional. |
| limited_partnerships_num_gen_partners | Integer | Número de socios generales. |
| limited_partnerships_num_ltd_partners | Integer | Número de socios limitados. |
| uri | Text | Enlace único a información actualizada de la empresa. |
| previous_name_1 | Text | Nombre anterior de la empresa. |
| previous_name_2 | Text | Nombre anterior adicional. |
| previous_name_3 | Text | Nombre anterior adicional. |
| previous_name_4 | Text | Nombre anterior adicional. |
| previous_name_5 | Text | Nombre anterior adicional. |
| confirmation_statement_next_due_date | Date | Próxima fecha de confirmación. |
| confirmation_statement_last_made_up_date | Date | Última confirmación realizada. |
| _cargado_en | Timestamp | Fecha y hora de carga del registro. |

---

## Notas

Los enlaces URI incluidos permiten consultar información actualizada de cada empresa.

Este dataset puede ser utilizado tanto en formato CSV como mediante su restauración en PostgreSQL para análisis más avanzados.
