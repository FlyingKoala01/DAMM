import pandas as pd
import math
import sqlite3
import glob
import random

DATABASE = "app/damm.db"

def main():
    files = glob.glob("*.xlsx")  # Obtinc la llista de tots els arxius Excel que tinc dins la carpeta actual

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    for file in files:
        df = pd.read_excel(file, engine='openpyxl')

        for _, row in df.iterrows():
            codi_dist = row["CODI DIST (AGRUPACION 2)"]
            agrup_nivel_2 = row["Agrup. Nivel 2"]
            establecimiento = row["Establecimiento"]
            esta = establecimiento.split(" ",1)
            id_establecimiento = esta[0]
            nombre_establecimiento = esta[1]
            producto = row["Material Precio"]
            prod = producto.split(" ",1)
            id_producto = prod[0]
            nombre_producto = prod[1]
            sector_producto = row["Sector"]
            total_producto = row["TOTAL"]

            existing_distribuidor = cursor.execute(f"SELECT id FROM Distribuidor WHERE id = {codi_dist}").fetchone()
            existing_establecimiento = cursor.execute("SELECT id FROM Establecimiento WHERE id = (?)", (id_establecimiento,)).fetchone()
            existing_producto = cursor.execute("SELECT id FROM Productos WHERE id = (?)", (id_producto,)).fetchone()
            existing_total_producto = cursor.execute("SELECT id_producto, id_establecimiento FROM Total__Prod_estable  WHERE id_producto = (?) and id_establecimiento = (?) ", (id_producto,id_establecimiento)).fetchone()
            
            if existing_distribuidor is None:
                cursor.execute("INSERT INTO Distribuidor (id, nombre) VALUES (?, ?)", (codi_dist, agrup_nivel_2))
            
            if existing_establecimiento is None:
                cursor.execute("INSERT INTO Establecimiento (id, nombre, id_distribuidor) VALUES (?, ?, ?)", (id_establecimiento, nombre_establecimiento, codi_dist))
            
            if existing_producto is None:
                cursor.execute("INSERT INTO Productos (id, nombre, sector, peso) VALUES (?, ?, ?, ?)", (id_producto, nombre_producto ,sector_producto,random.randint(1,10)*0.1))

            if existing_total_producto is None:
                cursor.execute("INSERT INTO Total__Prod_estable (id_establecimiento, id_producto, total) VALUES (?, ?, ?)", (id_establecimiento, id_producto, total_producto))

            for mes in df.columns[5:17]:
                cantidad = row[mes]
                if isinstance(cantidad, float) and math.isnan(cantidad):
                    cantidad = 0
                
                # Verificar si ja existeix un registre a la taula Prod_esta
                if cursor.execute("SELECT id_establecimiento, id_producto, year_month FROM Prod_esta WHERE id_establecimiento = ? AND id_producto = ? AND year_month = ?", (id_establecimiento, id_producto, mes)).fetchone() is None:
                    cursor.execute("INSERT INTO Prod_esta (id_establecimiento, id_producto, year_month, cantidad) VALUES (?, ?, ?, ?)", (id_establecimiento, id_producto, mes, cantidad))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()



