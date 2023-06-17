from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import sqlite3, sys
from datetime import datetime

DB_PATH='app/damm.db'

def monthly_review(months=None):
    if months is None:
        current_date = datetime.now()
        months = [datetime(current_date.year, current_date.month, 1)]
    if not isinstance(months, list):
        months = [months]

    print(f"Número de meses para valorar: {len(months)}")

    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # Obtengo bares que tienen una direccion definida
    cursor.execute("SELECT id, direccion FROM establecimiento WHERE direccion IS NOT NULL")
    rows = cursor.fetchall()

    print(f"Numero de establecimientos para valorar: {len(rows)}")

    # Inicio firefox
    options = Options()
    # In headless mode JS is not executed (needed because google does weird things).
    #options.headless = True
    driver = Firefox(options=options, executable_path='./geckodriver')

    for est_id, direccion in rows:
        cursor.execute(f"SELECT COUNT(*) FROM valoracion WHERE id_establecimiento = ? AND mes IN ({','.join(['?'] * len(months))})", (est_id, *months))
        count = cursor.fetchone()[0]

        if count >= len(months): continue

        driver.get(f"https://www.google.com/search?q={direccion.replace(' ', '+')}")

        try:
            grade_span = driver.find_element_by_css_selector('span.yi40Hd.YrbPuc')
            grade_float = float(grade_span.text.replace(',','.'))

            print(".", end="")
            sys.stdout.flush()
        except:
            print("E", end="")
            sys.stdout.flush()
            continue

        if len(months) == 1:
            cursor.execute("INSERT INTO valoracion (id_establecimiento, mes, valoracion) VALUES (?, ?, ?)", (est_id, months[0], grade_float))
            continue

        for month in months:
            cursor.execute("SELECT COUNT(*) FROM valoracion WHERE id_establecimiento = ? AND mes = ?", (est_id, month))
            count = cursor.fetchone()[0]

            if count >= 1: continue

            cursor.execute("INSERT INTO valoracion (id_establecimiento, mes, valoracion) VALUES (?, ?, ?)", (est_id, month, grade_float))

    print("\nValoración terminada.")
    driver.quit()
    conn.commit()
    conn.close()

def monthly_review_all_months():
    """
    Mira todos los meses en los que ha habido ventas y pone la misma valoración
    en todos. Útil para tener valores de ejemplo al principio de todo.
    """
    print("Llenando valoraciones de google para todos los meses ...")

    conn=sqlite3.connect(DB_PATH)
    cursor=conn.cursor()

    # Obtengo bares que tienen una direccion definida
    cursor.execute("SELECT DISTINCT mes FROM venta")
    months = cursor.fetchall()

    conn.close()

    monthly_review([month[0] for month in months])
