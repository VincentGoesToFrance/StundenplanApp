-- -- Für MariaDB:
-- CREATE DATABASE IF NOT EXISTS test_stundenplanDB;

-- USE test_stundenplanDB;

-- DROP TABLE IF EXISTS dozenten;

-- CREATE TABLE IF NOT EXISTS dozenten (
--     id INT AUTO_INCREMENT PRIMARY KEY,
--     vorname VARCHAR(100) UNIQUE NOT NULL,
--     nachname VARCHAR(100) UNIQUE NOT NULL,
--     fachrichtung VARCHAR(255) NOT NULL
-- );

-- INSERT INTO dozenten (vorname, nachname, fachrichtung) VALUES ('Lautz', 'Weise', 'Systemintegrator'); --absichtlich Latz, wegen SQLite
-- INSERT INTO dozenten (vorname, nachname, fachrichtung) VALUES ('Fritz-Rainer', 'Döbbelin', 'Anwendungsentwickler');


-- Für SQLITE: 

DROP TABLE IF EXISTS dozenten;
CREATE TABLE dozenten (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vorname TEXT UNIQUE NOT NULL,
    nachname TEXT NOT NULL,
    fachrichtung TEXT NOT NULL
);

INSERT INTO dozenten (vorname, nachname, fachrichtung) VALUES ('Lutz', 'Weise', 'Systemintegrator');
INSERT INTO dozenten (vorname, nachname, fachrichtung) VALUES ('Fritz-Rainer', 'Döbbelin', 'Anwendungsentwickler');