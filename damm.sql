PRAGMA foreign_keys=ON;

CREATE TABLE IF NOT EXISTS Distribuidor(
       ID CHAR PRIMARY KEY,
       nombre CHAR
);

CREATE TABLE IF NOT EXISTS Productos(
       ID CHAR PRIMARY KEY,
       nombre CHAR,
       sector CHAR
);

-- Taula creada a partir de la relació entre productos, establecimiento i la data. En funció d'aquests tres tenim la cantitat de productes.
CREATE TABLE IF NOT EXISTS Prod_esta(
       id_establecimiento CHAR,
       id_producto CHAR,
       año_mes CHAR,
       cantidad INT,
       PRIMARY KEY(id_establecimiento, id_producto, año_mes),
       FOREIGN KEY (id_establecimiento) REFERENCES Establecimiento(ID),
       FOREIGN KEY (id_producto) REFERENCES Productos(ID)
);

--Taula creada a partir de la relació entre productos i establecimiento per saber el total de cada producte en funció de l'establiment en l'any sencer. "Potser faltaria també identificar l'any d'on extreiem les dades."
CREATE TABLE IF NOT EXISTS Total_Prod_estable(
       id_establecimiento CHAR,
       id_producto TEXT,
       total INT,
       PRIMARY KEY(id_producto, id_establecimiento),
       FOREIGN KEY (id_establecimiento) REFERENCES Establecimiento(ID),
       FOREIGN KEY (id_producto) REFERENCES Productos(ID)
);

---------------- TO BE REVIEWED  -------------------------
CREATE TABLE IF NOT EXISTS Leaderboard(
       position INT PRIMARY KEY,
       bar_name CHAR,
       total_sales INT, --  Parametre d'exemple per omplir
       rating_online INT, -- Mitjana nota online
       grade INT, -- Nota del cabra
       progress INT, -- A partir del trigger
       FOREIGN KEY (rating_online) REFERENCES Establecimiento(average_grade)
       FOREIGN KEY (bar_name) REFERENCES Establecimiento(nombre)
);


CREATE TABLE IF NOT EXISTS Establecimiento(
       ID CHAR PRIMARY KEY,
       nombre CHAR,
       coordenades CHAR default null,
       id_distribuidor CHAR,
       average_grade INT, -- Mitjana trip advisor, google, etc etc
       FOREIGN KEY (id_distribuidor) REFERENCES Distribuidor(ID)
);


--CREATE TRIGGER UpdateLeaderboard
--AFTER INSERT ON Leaderboard
--FOR EACH ROW
--BEGIN
--    DECLARE new_position INT;
--    DECLARE existing_grade INT;
--    DECLARE existing_position INT;
--    DECLARE existing_progress INT;
    
--    SET new_position = NEW.position;
--    SET existing_grade = NEW.grade;
--    SET existing_position = 0;
--    SET existing_progress = 0;

    -- Update the progress and position for existing bars
--    UPDATE Leaderboard
--    SET progress = progress + 1
--    WHERE position < new_position;
    
    -- Update the progress and position for the bar with the same grade
--    SELECT position, progress INTO existing_position, existing_progress
--    FROM Leaderboard
--    WHERE grade = existing_grade
--    LIMIT 1;
    
--    IF existing_position > 0 THEN
--        UPDATE Leaderboard
--        SET progress = existing_progress + 1
--        WHERE position = existing_position;
--    END IF;
    
    -- Update the position and progress for the new bar
--    UPDATE Leaderboard
--    SET position = new_position, progress = 0
--    WHERE bar_name = NEW.bar_name;
--END;
