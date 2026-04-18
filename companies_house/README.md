# Producto de Datos Empresariales Gratuito

## Descripción

El producto gratuito de datos empresariales es una **instantánea descargable** que contiene información básica de las empresas registradas.

Esta instantánea:
- Se distribuye en archivos **ZIP**.
- Contiene datos en formato **CSV**.
- Está dividida en varios archivos para facilitar su descarga.

Nota: Este producto se proporciona de forma gratuita y **no cuenta con soporte técnico**.

---

##  Actualización de los Datos

- La instantánea se actualiza en un plazo de **5 días hábiles** después de finalizar cada mes.
- El contenido incluye información recopilada **hasta finales del mes anterior**.

---

##  Estructura de la Base de Datos

Los datos también pueden presentarse como un **dump de PostgreSQL**, incluyendo la tabla principal:

### Tabla: `company_data`

| Columna                                      | Tipo de Dato | Descripción |
|---------------------------------------------|-------------|-------------|
| _pk                                         | BigInt      | Identificador único de la empresa (clave primaria). |
| companyname                                 | Text        | Nombre de la empresa. |
| companynumber                               | Text        | Número de registro de la empresa. |
| regaddress_careof                           | Text        | Información adicional del domicilio (a cargo de). |
| regaddress_pobox                            | Text        | Apartado postal. |
| regaddress_addressline1                     | Text        | Dirección principal. |
| regaddress_addressline2                     | Text        | Segunda línea de dirección. |
| regaddress_posttown                         | Text        | Ciudad. |
| regaddress_county                           | Text        | Condado o región. |
| regaddress_country                          | Text        | País. |
| regaddress_postcode                         | Text        | Código postal. |
| companycategory                             | Text        | Tipo de empresa (ej. Private Limited Company). |
| companystatus                               | Text        | Estado de la empresa (ej. Active). |
| countryoforigin                             | Text        | País de origen. |
| dissolutiondate                             | Text        | Fecha de disolución (si aplica). |
| incorporationdate                           | Text        | Fecha de constitución. |
| accounts_accountrefday                      | Integer     | Día de referencia contable. |
| accounts_accountrefmonth                    | Integer     | Mes de referencia contable. |
| accounts_nextduedate                        | Text        | Próxima fecha de entrega de cuentas. |
| accounts_lastmadeupdate                     | Text        | Última actualización de cuentas. |
| accounts_accountcategory                    | Text        | Categoría de cuentas. |
| returns_nextduedate                         | Text        | Próxima fecha de declaración. |
| returns_lastmadeupdate                      | Text        | Última actualización de declaración. |
| mortgages_nummortcharges                    | Integer     | Número de cargos hipotecarios. |
| mortgages_nummortoutstanding                | Integer     | Hipotecas pendientes. |
| mortgages_nummortpartsatisfied              | Integer     | Hipotecas parcialmente satisfechas. |
| mortgages_nummortsatisfied                  | Integer     | Hipotecas satisfechas. |
| siccode_sictext_1 a _4                      | Text        | Códigos SIC (clasificación industrial). |
| limitedpartnerships_numgenpartners          | Integer     | Número de socios generales. |
| limitedpartnerships_numlimpartners          | Integer     | Número de socios limitados. |
| uri                                         | Text        | Enlace único a información actualizada de la empresa. |
| previousname_*                              | Text        | Historial de nombres anteriores de la empresa. |
| confstmtnextduedate                         | Text        | Próxima fecha de confirmación. |
| confstmtlastmadeupdate                      | Text        | Última confirmación realizada. |
| _cargado_en                                 | Timestamp   | Fecha de carga del registro. |

---

##  Información Adicional

- Existe un documento PDF con la lista completa de campos incluidos.
- Se puede obtener información actualizada mediante los enlaces **URI** presentes en los datos.
- Para visualizar correctamente los archivos en Excel, se recomienda usar **Microsoft Excel 2007 o superior**.

---

##  Formato de los Datos

- Archivos comprimidos: `.zip`
- Formato de datos: `.csv`
- También disponible como:
  - Dump de base de datos **PostgreSQL**

---

##  Notas

- Los datos representan información básica de empresas registradas.
- Algunos campos pueden contener valores nulos (`NULL`).
- La estructura puede variar ligeramente entre versiones de la instantánea.

---
