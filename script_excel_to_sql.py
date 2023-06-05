import pandas as pd
import math
import sqlite3
import glob

DATABASE = "damm.bd"

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
            producto = row["Material Precio"]
            sector_producto = row["Sector"]
            total_producto = row["TOTAL"]

            existing_distribuidor = cursor.execute(f"SELECT ID FROM Distribuidor WHERE ID = {codi_dist}").fetchone()
            existing_establecimiento = cursor.execute("SELECT nombre FROM Establecimiento WHERE nombre = (?)", (establecimiento,)).fetchone()
            existing_producto = cursor.execute("SELECT codigo FROM Productos WHERE codigo = (?)", (producto,)).fetchone()
            existing_total_producto = cursor.execute("SELECT codigo_producto, nombre_establecimiento FROM Total_Prod_estable  WHERE codigo_producto = (?) and nombre_establecimiento = (?) ", (producto,establecimiento)).fetchone()
            
            if existing_distribuidor is None:
                cursor.execute("INSERT INTO Distribuidor (ID, nombre) VALUES (?, ?)", (codi_dist, agrup_nivel_2))
            
            if existing_establecimiento is None:
                cursor.execute("INSERT INTO Establecimiento (nombre, id_distribuidor) VALUES (?, ?)", (establecimiento, codi_dist))
            
            if existing_producto is None:
                cursor.execute("INSERT INTO Productos (codigo, sector) VALUES (?, ?)", (producto, sector_producto))

            if existing_total_producto is None:
                cursor.execute("INSERT INTO Total_Prod_estable (nombre_establecimiento, codigo_producto, total) VALUES (?, ?, ?)", (establecimiento, producto, total_producto))

            for mes in df.columns[5:17]:
                cantidad = row[mes]
                if isinstance(cantidad, float) and math.isnan(cantidad):
                    cantidad = 0
                
                # Verificar si ja existeix un registre a la taula Prod_esta
                if cursor.execute("SELECT nombre_establecimiento, codigo_producto, año_mes FROM Prod_esta WHERE nombre_establecimiento = ? AND codigo_producto = ? AND año_mes = ?", (establecimiento, producto, mes)).fetchone() is None:
                    cursor.execute("INSERT INTO Prod_esta (nombre_establecimiento, codigo_producto, año_mes, cantidad) VALUES (?, ?, ?, ?)", (establecimiento, producto, mes, cantidad))

    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()



