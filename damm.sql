PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS Distribuidor(
       ID CHAR PRIMARY KEY,
       nombre CHAR
);

CREATE TABLE IF NOT EXISTS Establecimiento(
       nombre CHAR PRIMARY KEY,
       coordenades CHAR default null,
       id_distribuidor CHAR,
       FOREIGN KEY (id_distribuidor) REFERENCES Distribuidor(ID)
);

CREATE TABLE IF NOT EXISTS Productos(
       codigo TEXT PRIMARY KEY,
       sector CHAR
);

-- Taula creada a partir de la relació entre productos, establecimiento i la data. En funció d'aquests tres tenim la cantitat de productes.
CREATE TABLE IF NOT EXISTS Prod_esta(
       nombre_establecimiento CHAR,
       codigo_producto TEXT,
       año_mes CHAR,
       cantidad INT,
       PRIMARY KEY(nombre_establecimiento, codigo_producto, año_mes),
       FOREIGN KEY (nombre_establecimiento) REFERENCES Establecimiento(nombre),
       FOREIGN KEY (codigo_producto) REFERENCES Productos(codigo)
);

--Taula creada a partir de la relació entre productos i establecimiento per saber el total de cada producte en funció de l'establiment en l'any sencer. "Potser faltaria també identificar l'any d'on extreiem les dades."
CREATE TABLE IF NOT EXISTS Total_Prod_estable(
       nombre_establecimiento CHAR,
       codigo_producto TEXT,
       total INT,
       PRIMARY KEY(codigo_producto, nombre_establecimiento),
       FOREIGN KEY (nombre_establecimiento) REFERENCES Establecimiento(nombre),
       FOREIGN KEY (codigo_producto) REFERENCES Productos(codigo)
);
