#!/usr/bin/env python3
"""
csv_to_postgres.py — Migrador universal CSV → PostgreSQL
Uso:
    python csv_to_postgres.py archivo.csv [nombre_tabla]
"""

import sys
import os
import csv
import io
import re
import unicodedata
import argparse

# ─── CONFIGURACIÓN DE CONEXIÓN ────────────────────────────────────────────────
DB_HOST     = "localhost"
DB_PORT     = 5432
DB_NAME     = "uber_fares"
DB_USER     = "postgres"
DB_PASSWORD = "oaxaca.21"
DB_SCHEMA   = "public"
# ─────────────────────────────────────────────────────────────────────────────

VACIOS = {"", "-", "n/a", "N/A", "NA", "null", "NULL", "ninguno", "NINGUNO", "nd", "ND"}


def normalizar_columna(nombre: str, usados: dict) -> str:
    nombre = nombre.strip().lower()
    nombre = unicodedata.normalize("NFD", nombre)
    nombre = "".join(c for c in nombre if unicodedata.category(c) != "Mn")
    nombre = re.sub(r"[^a-z0-9]+", "_", nombre).strip("_") or "columna"
    if nombre[0].isdigit():
        nombre = "col_" + nombre
    base = nombre
    n = usados.get(base, 0)
    if n > 0:
        nombre = f"{base}_{n}"
    usados[base] = n + 1
    return nombre


def es_entero(v: str) -> bool:
    return re.fullmatch(r"-?\d+", v) is not None

def es_decimal(v: str) -> bool:
    return re.fullmatch(r"-?\d+\.\d+", v) is not None

def es_fecha(v: str) -> bool:
    return re.fullmatch(
        r"\d{4}[-/]\d{2}[-/]\d{2}([ T]\d{2}:\d{2}(:\d{2})?)?", v
    ) is not None


def inferir_tipo(valores: list) -> str:
    """Evalúa TODOS los valores no vacíos para decidir el tipo."""
    no_vacios = [v.strip().replace(",", "") for v in valores if v.strip() not in VACIOS]
    if not no_vacios:
        return "TEXT"
    if all(es_entero(v) for v in no_vacios):
        maxval = max(abs(int(v)) for v in no_vacios)
        return "INTEGER" if maxval < 2_147_483_647 else "BIGINT"
    if all(es_decimal(v) or es_entero(v) for v in no_vacios):
        return "NUMERIC(20,6)"
    if all(es_fecha(v) for v in no_vacios):
        return "TIMESTAMP" if any("T" in v or " " in v for v in no_vacios) else "DATE"
    return "TEXT"


def leer_csv(ruta: str):
    print(f"\n📂 Leyendo: {ruta}")
    if not os.path.exists(ruta):
        print(f"✗  Archivo no encontrado: {ruta}")
        sys.exit(1)

    contenido = None
    encoding_usado = None
    for enc in ("utf-8-sig", "utf-8", "latin-1", "cp1252"):
        try:
            with open(ruta, encoding=enc, errors="strict") as f:
                contenido = f.read()
            encoding_usado = enc
            break
        except (UnicodeDecodeError, ValueError):
            continue

    if contenido is None:
        print("✗  No se pudo leer el archivo.")
        sys.exit(1)

    print(f"   Encoding    : {encoding_usado}")

    muestra = contenido[:8192]
    try:
        dialect = csv.Sniffer().sniff(muestra, delimiters=",;\t|")
        delimitador = dialect.delimiter
    except csv.Error:
        delimitador = ","

    print(f"   Delimitador : {repr(delimitador)}")

    reader = csv.reader(io.StringIO(contenido), delimiter=delimitador)
    filas = list(reader)

    if len(filas) < 2:
        print("✗  El CSV no tiene suficientes filas.")
        sys.exit(1)

    return filas[0], filas[1:]


def analizar(encabezados: list, datos: list):
    usados = {}
    columnas_pg = [normalizar_columna(h, usados) for h in encabezados]
    n = len(columnas_pg)

    print(f"   Analizando tipos en {len(datos):,} filas completas… ", end="", flush=True)

    # Una sola pasada para recolectar todos los valores por columna
    columnas_vals = [[] for _ in range(n)]
    for fila in datos:
        for i in range(n):
            columnas_vals[i].append(fila[i] if i < len(fila) else "")

    tipos = [inferir_tipo(vals) for vals in columnas_vals]
    print("✓")

    print(f"\n📋 {n} columnas detectadas:")
    print(f"   {'CSV':35} {'PostgreSQL':35} {'Tipo'}")
    print(f"   {'-'*35} {'-'*35} {'-'*14}")
    for orig, pg, tipo in zip(encabezados, columnas_pg, tipos):
        print(f"   {orig[:35]:35} {pg[:35]:35} {tipo}")
    print(f"\n   Filas de datos: {len(datos):,}")

    return columnas_pg, tipos


def migrar(tabla: str, columnas_pg: list, tipos: list, datos: list):
    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        print("\n✗  Falta psycopg2.  Instala con:  pip install psycopg2-binary")
        sys.exit(1)

    print(f"\n🔌 Conectando a {DB_HOST}:{DB_PORT}/{DB_NAME}…")
    conn = psycopg2.connect(
        host=DB_HOST, port=DB_PORT, dbname=DB_NAME,
        user=DB_USER, password=DB_PASSWORD,
    )
    conn.autocommit = False
    cur = conn.cursor()

    tabla_fq = f'"{DB_SCHEMA}"."{tabla}"'

    col_defs = ",\n    ".join(
        f'"{col}" {tipo}' for col, tipo in zip(columnas_pg, tipos)
    )
    ddl = f"""
CREATE TABLE IF NOT EXISTS {tabla_fq} (
    _pk BIGSERIAL PRIMARY KEY,
    {col_defs},
    _cargado_en TIMESTAMPTZ DEFAULT NOW()
);
"""
    print(f"🏗  Creando tabla {tabla_fq}…")
    cur.execute(ddl)

    # Índices automáticos en columnas comunes
    candidatos = {
        "id", "clave", "cve_ent", "cve_mun", "cve_loc",
        "entidad", "municipio", "estado", "anio", "ano",
        "mes", "fecha", "fecha_alta", "codigo_act",
    }
    for col in columnas_pg:
        if col in candidatos:
            cur.execute(
                f'CREATE INDEX IF NOT EXISTS "idx_{tabla}_{col}" '
                f'ON {tabla_fq} ("{col}");'
            )

    cols_num = {
        col for col, t in zip(columnas_pg, tipos)
        if t in ("INTEGER", "BIGINT", "NUMERIC(20,6)")
    }

    def limpiar_fila(fila):
        resultado = []
        for i, col in enumerate(columnas_pg):
            val = fila[i].strip() if i < len(fila) else ""
            if val in VACIOS:
                resultado.append(None)
            elif col in cols_num:
                resultado.append(val.replace(",", "") or None)
            else:
                resultado.append(val or None)
        return resultado

    LOTE = 5_000
    cols_sql   = ", ".join(f'"{c}"' for c in columnas_pg)
    valores_ph = ", ".join(["%s"] * len(columnas_pg))
    sql = f"INSERT INTO {tabla_fq} ({cols_sql}) VALUES ({valores_ph})"

    print(f"⬆  Insertando {len(datos):,} filas (lotes de {LOTE:,})…")
    lote, total = [], 0

    for fila in datos:
        lote.append(limpiar_fila(fila))
        if len(lote) >= LOTE:
            psycopg2.extras.execute_batch(cur, sql, lote, page_size=LOTE)
            total += len(lote)
            print(f"   {total:,} / {len(datos):,}", end="\r")
            lote.clear()

    if lote:
        psycopg2.extras.execute_batch(cur, sql, lote, page_size=LOTE)
        total += len(lote)

    conn.commit()
    cur.close()
    conn.close()

    print(f"\n✅ {total:,} filas insertadas en {tabla_fq}")


def nombre_tabla_desde_archivo(ruta: str) -> str:
    base = os.path.splitext(os.path.basename(ruta))[0].lower().strip()
    base = unicodedata.normalize("NFD", base)
    base = "".join(c for c in base if unicodedata.category(c) != "Mn")
    base = re.sub(r"[^a-z0-9]+", "_", base).strip("_") or "tabla_csv"
    return ("t_" + base) if base[0].isdigit() else base


def main():
    parser = argparse.ArgumentParser(description="Migrador universal CSV → PostgreSQL")
    parser.add_argument("csv",   help="Ruta al archivo CSV")
    parser.add_argument("tabla", nargs="?", default=None,
                        help="Nombre de la tabla destino (opcional)")
    args = parser.parse_args()

    tabla = args.tabla or nombre_tabla_desde_archivo(args.csv)

    print("=" * 60)
    print("  csv_to_postgres — Migrador Universal")
    print("=" * 60)
    print(f"  Archivo : {args.csv}")
    print(f"  Tabla   : {DB_SCHEMA}.{tabla}")
    print(f"  BD      : {DB_USER}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

    encabezados, datos = leer_csv(args.csv)
    columnas_pg, tipos = analizar(encabezados, datos)

    respuesta = input("\n¿Continuar con la migración? [S/n]: ").strip().lower()
    if respuesta in ("n", "no"):
        print("Cancelado.")
        sys.exit(0)

    migrar(tabla, columnas_pg, tipos, datos)

    print(f"""
💡 Verificar en PostgreSQL:
   docker exec -it some-postgres psql -U postgres -c \\
     "SELECT * FROM \\"{DB_SCHEMA}\\".\\"{tabla}\\" LIMIT 5;"
""")


if __name__ == "__main__":
    main()