--
-- Archivo generado con SQLiteStudio v3.4.4 el vie. oct. 4 18:35:26 2024
--
-- Codificación de texto usada: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Tabla: Comentarios
CREATE TABLE IF NOT EXISTS Comentarios (
    ID_comentario    INTEGER PRIMARY KEY AUTOINCREMENT,
    Comentario       TEXT,
    Fecha_comentario REAL,
    ID_solicitud     INTEGER REFERENCES Solicitud (ID_solicitud),
    ID_encargado     INTEGER REFERENCES Encargados (ID_encargado) 
);


-- Tabla: Documentos
CREATE TABLE IF NOT EXISTS Documentos (
    ID_documento   INTEGER PRIMARY KEY AUTOINCREMENT
                           UNIQUE,
    Tipo           BLOB,
    Nombre         TEXT,
    Descripción    TEXT,
    Fecha_creación REAL
);


-- Tabla: Encargados
CREATE TABLE IF NOT EXISTS Encargados (
    ID_encargado INTEGER PRIMARY KEY AUTOINCREMENT,
    Nombres      TEXT,
    Apellido     TEXT,
    Rol          TEXT
);

INSERT INTO Encargados (
                           ID_encargado,
                           Nombres,
                           Apellido,
                           Rol
                       )
                       VALUES (
                           1,
                           'Rosa',
                           'Melano',
                           'Gestora'
                       );


-- Tabla: Solicitud
CREATE TABLE IF NOT EXISTS Solicitud (
    ID_solicitud    INTEGER PRIMARY KEY AUTOINCREMENT,
    ID_user         INTEGER REFERENCES Usuarios (ID),
    ID_documento    INTEGER REFERENCES Documentos (ID_documento),
    ID_encargado    INTEGER REFERENCES Encargados (ID_encargado),
    Fecha_solicitud REAL,
    Estado          TEXT    DEFAULT Finalizado
                            DEFAULT Proceso
                            DEFAULT Entregado
);


-- Tabla: Usuarios
CREATE TABLE IF NOT EXISTS Usuarios (
    ID              INTEGER PRIMARY KEY AUTOINCREMENT
                            UNIQUE,
    Nombres         TEXT,
    Apellido        TEXT,
    Correo          TEXT,
    Fecha_registro  REAL,
    contraseña_hash TEXT
);

INSERT INTO Usuarios (
                         ID,
                         Nombres,
                         Apellido,
                         Correo,
                         Fecha_registro,
                         contraseña_hash
                     )
                     VALUES (
                         1,
                         'Jhoan',
                         'Cuesta',
                         'jhoancuesta034@gmail.com',
                         '4/10/2024',
                         'Jhoan2006'
                     );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
