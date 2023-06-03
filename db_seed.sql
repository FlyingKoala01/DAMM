-- Create the bars table
CREATE TABLE bars (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    bar_name TEXT,
    latitude INTEGER,
    longitude INTEGER,
    ranking INTEGER,
    total_sales INTEGER,
    progress INTEGER
);

-- Insert sample data // COORDINATES MULTIPLED AND DIVIDED BY 10000 (chatgpt has spoken 'increased precision')
INSERT INTO bars (bar_name, latitude, longitude, ranking, total_sales, progress) VALUES
    ('Bar 1', 413879, 21699, 3, 1500, 1),
    ('Bar 2', 413976, 21900, 5, 1200, -2),
    ('Bar 3', 414036, 21744, 1, 2500, 0),
    ('Bar 4', 413826, 21770, 7, 900, -3),
    ('Bar 5', 413945, 21633, 2, 1800, 2),
    ('Bar 6', 413942, 21833, 4, 1350, 0),
    ('Bar 7', 413962, 21709, 6, 1050, -1);
