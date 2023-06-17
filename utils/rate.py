"""
Computes the grade of each local according to data stored in the database. 
"""

import sqlite3, sys
from math import log
from datetime import datetime
from .time_utils import *
from .script_excel_to_sql import SAFE_MODE

DB_PATH='app/damm.db'

SOCIAL_NETWORKS_WEIGHT=0.5
DATABASE_SALES_WEIGHT=0.1

WEIGHTS = None

def set_weigths():
    global WEIGHTS

    if WEIGHTS is not None: return

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Haciendo la query una unica vez y pasando los resultados como parámetros.
    WEIGHTS=dict(cursor.execute("select id,peso from producto;").fetchall())

    conn.close()

def cache_last_note():
    """
    Puts the last note of a bar into its cache, so queries are faster.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute("CREATE INDEX IF NOT EXISTS idx_nota_id_establecimiento ON nota (id_establecimiento);")
    conn.commit()

    cursor.execute("\
        UPDATE establecimiento \
        SET nota = (\
            SELECT nota \
            FROM nota \
            WHERE id_establecimiento = establecimiento.id \
            ORDER BY mes DESC \
            LIMIT 1\
        ),\
        nota_anterior = (\
            SELECT nota \
            FROM nota \
            WHERE id_establecimiento = establecimiento.id \
            ORDER BY mes DESC \
            LIMIT 1 OFFSET 1\
        );")

    conn.commit()
    conn.close()

def weightLocal(bar_id, month):
    """
    Returns a weighting from the indicated bar in the indicated month. 
    If the month is not specified, a global score is returned.
    """
    con=sqlite3.connect(DB_PATH)
    cur=con.cursor()

    def weight_in_month(month):
        data = cur.execute("SELECT id_producto, cantidad FROM venta WHERE id_establecimiento = ? AND mes = ?", (bar_id, month)).fetchall()
        return sum(WEIGHTS[p[0]]*p[1] for p in data)/len(data) if len(data) > 0 else 0
    def social_in_month(month):
        data = cur.execute("SELECT valoracion FROM valoracion WHERE id_establecimiento = ? AND mes = ?", (bar_id, month)).fetchone()
        return data[0] if data is not None else 0

    sales_weight = sum([
        weight_in_month(month),
        weight_in_month(one_month_ago(month)),
        weight_in_month(one_year_ago(month))
    ])

    social_weigth = sum([
        social_in_month(month),
        social_in_month(one_month_ago(month)),
        social_in_month(one_year_ago(month))
    ])

    con.close()
    return social_weigth*SOCIAL_NETWORKS_WEIGHT+DATABASE_SALES_WEIGHT*sales_weight


def fromWeightToGrade(l):
    """
    Performs a logarithmic conversion of the given list to convert the values on a scale from 0 to 10.
    In other words, it normalizes the value between 0 and 10
    """
    grade_max=10
    grade_min=1
    max_value=max(l)
    if max_value==0:
        return [0 for i in range(len(l))]
    ret=[]
    for value in l:
        if value<0:
            ret.append(0)
        else:
            ret.append(grade_min+(grade_max-grade_min)*log(value+1)/log(max_value+1))
    return ret


def calc_rate(month):
    set_weigths()

    if month is None:
        current_date = datetime.now()
        month = datetime(current_date.year, current_date.month, 1)

    conn=sqlite3.connect(DB_PATH)
    cur=conn.cursor()

    data = cur.execute("SELECT id FROM establecimiento;").fetchall()
    output = []

    print(f"Calculando nota para {len(data)} establecimientos ")

    for i, b in enumerate(data):
        if i%25==0:
            print('.', end='')
            sys.stdout.flush()

        bar_id=b[0]
        output.append(weightLocal(bar_id, month))

    print("Normalizando valores.")
    normalized_output = fromWeightToGrade(output)

    print("Guardando valores en la base de datos ")
    for i, b in enumerate(data):
        if i%250==0:
            print('.', end='')
            sys.stdout.flush()

        bar_id=b[0]

        if (not SAFE_MODE) or cur.execute("SELECT COUNT(*) FROM nota WHERE id_establecimiento = ? AND mes = ?", (bar_id, month)).fetchone()[0] == 0:
            cur.execute("INSERT INTO nota (id_establecimiento, mes, nota) VALUES (?, ?, ?)", (bar_id, month, normalized_output[i]))

    conn.commit()
    conn.close()
    print(f"Notas para mes {month} calculadas correctamente.")

def calc_rate_all_months():
    """
    Mira todos los meses en los que ha habido ventas y pone la misma valoración
    en todos. Útil para tener valores de ejemplo al principio de todo.
    """
    print("Calculando nota para todos los meses ...")

    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # Obtengo bares que tienen una direccion definida
    cursor.execute("SELECT DISTINCT mes FROM venta")
    months = cursor.fetchall()

    conn.close()

    print(f"Número de meses para valorar: {len(months)}")

    for month in months:
        calc_rate(month[0])
