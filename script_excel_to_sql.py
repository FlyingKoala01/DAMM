import pandas as pd
import sqlite3, glob, random, sys, math
from datetime import datetime

DATABASE = "app/damm.db"

def convert_string_to_date(string):
    # Define the month abbreviations and their corresponding numbers
    month_abbreviations = {
        "Ene.": "01",
        "Feb.": "02",
        "Mar.": "03",
        "Abr.": "04",
        "May.": "05",
        "Jun.": "06",
        "Jul.": "07",
        "Ago.": "08",
        "Sep.": "09",
        "Oct.": "10",
        "Nov.": "11",
        "Dic.": "12"
    }
    
    # Extract the month and year from the given string
    month = month_abbreviations[string[:4]]
    year = "20" + string[4:]
    
    # Create a datetime object representing the first day of the month
    date_string = f"01-{month}-{year}"
    date = datetime.strptime(date_string, "%d-%m-%Y").date()
    
    return date


def main():
    # Lista de todos los archivos excel en la carpeta actual
    files = glob.glob("db/*.xlsx")
    print(f"Se han encontrado {len(files)} archivos .xlsx para entrar en la base de datos.")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    for file in files:
        print(f"Leyendo archivo {file} ...")
        df = pd.read_excel(file, engine='openpyxl')

        print(f"Processando archivo {file} ", end="")
        sys.stdout.flush()

        for i, row in df.iterrows():
            # Para evitar spam mostramos menos puntos
            if i%50==0:
                print('.', end="")
                sys.stdout.flush()

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

            existing_distribuidor = cursor.execute(f"SELECT id FROM distribuidor WHERE id = {codi_dist}").fetchone()
            existing_establecimiento = cursor.execute("SELECT id FROM establecimiento WHERE id = (?)", (id_establecimiento,)).fetchone()
            existing_producto = cursor.execute("SELECT id FROM producto WHERE id = (?)", (id_producto,)).fetchone()
            
            if existing_distribuidor is None:
                cursor.execute("INSERT INTO distribuidor (id, nombre) VALUES (?, ?)", (codi_dist, agrup_nivel_2))
            
            if existing_establecimiento is None:
                cursor.execute("INSERT INTO establecimiento (id, nombre, id_distribuidor) VALUES (?, ?, ?)", (id_establecimiento, nombre_establecimiento, codi_dist))
            
            if existing_producto is None:
                cursor.execute("INSERT INTO producto (id, nombre, sector, peso) VALUES (?, ?, ?, ?)", (id_producto, nombre_producto ,sector_producto,random.randint(1,10)*0.1))

            # A partir de aqui solo falta entrar en la base de datos las ventas

            for mes in df.columns[5:17]:
                if not (isinstance(mes, (float, int)) and not math.isnan(mes)): continue

                cantidad = round(mes)
                parsed_mes = convert_string_to_date(mes)
                
                # Verificar si ya existe registro
                if cursor.execute("SELECT 't' FROM venta WHERE id_establecimiento = ? AND id_producto = ? AND mes = ?", (id_establecimiento, id_producto, parsed_mes)).fetchone() is None:
                    cursor.execute("INSERT INTO venta (id_establecimiento, id_producto, mes, cantidad) VALUES (?, ?, ?, ?)", (id_establecimiento, id_producto, parsed_mes, cantidad))

        print("\nArchivo procesado correctamente.")

    print("Guardando todos los datos en la base de datos ...")
    conn.commit()
    conn.close()
    print("Guardado correctamente.")

if __name__ == "__main__":
    main()



