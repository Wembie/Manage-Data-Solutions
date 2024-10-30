BASE DE DATOS gestion de Docs

## Descripción
Esta base de datos almacena información relacionada con la gestión de usuarios, documentos y solicitudes en un sistema. Incluye tablas para usuarios, encargados, documentos y comentarios asociados a las solicitudes de documentos.

## Estructura de la base de datos

La base de datos está compuesta por las siguientes tablas:
-   Usuarios  : Contiene los datos de los usuarios registrados en el sistema.
-   Encargados  : Almacena los datos de las personas encargadas de procesar las solicitudes.
-   Documentos  : Registra los documentos gestionados por el sistema.
-   Datos_usuario  : Almacena información adicional de autenticación para los usuarios.
-   Solicitudes  : Guarda las solicitudes realizadas por los usuarios para obtener documentos.
-   Comentarios  : Incluye los comentarios de los encargados relacionados con las solicitudes.

   Tablas y Claves

    1. Tabla: Usuarios
| Columna          | Tipo de Dato  | Descripción                          |
|------------------|---------------|--------------------------------------|
| ID               | SERIAL        | Clave primaria, identificador único  |
| Usuario          | INTEGER       | Identificador único del usuario      |
| contraseña_hash  | TEXT          | Hash de la contraseña                |
| Nombres          | TEXT          | Nombre del usuario                   |
| Apellido         | TEXT          | Apellido del usuario                 |
| Correo           | TEXT          | Correo electrónico del usuario       |
| Fecha_registro   | TIMESTAMP     | Fecha de registro del usuario        |

  Claves  :   
  Clave primaria  : `ID`

    2. Tabla: Encargados
| Columna          | Tipo de Dato  | Descripción                          |
|------------------|---------------|--------------------------------------|
| ID               | SERIAL        | Clave primaria, identificador único  |
| Nombres          | TEXT          | Nombre del encargado                 |
| Apellido         | TEXT          | Apellido del encargado               |
| Rol              | TEXT          | Rol del encargado en el sistema      |

  Claves  :   
  Clave primaria  : `ID`

    3. Tabla: Documentos
| Columna          | Tipo de Dato  | Descripción                          |
|------------------|---------------|--------------------------------------|
| ID               | SERIAL        | Clave primaria, identificador único  |
| Tipo             | BYTEA         | Tipo de documento                    |
| Nombre           | TEXT          | Nombre del documento                 |
| Descripción      | TEXT          | Descripción del documento            |
| Fecha_creación   | TIMESTAMP     | Fecha de creación del documento      |

  Claves  :   
  Clave primaria  : `ID`

    4. Tabla: Datos_usuario
| Columna          | Tipo de Dato  | Descripción                          |
|------------------|---------------|--------------------------------------|
| Usuario          | INTEGER       | Identificador del usuario (foránea)  |
| Contraseña       | TEXT          | Contraseña del usuario               |

  Claves  :   
  Clave foránea  : `Usuario` que referencia `Usuarios(ID)`

    5. Tabla: Solicitudes
| Columna          | Tipo de Dato  | Descripción                                  |
|------------------|---------------|----------------------------------------------|
| ID               | SERIAL        | Clave primaria, identificador único          |
| ID_usuario       | INTEGER       | Clave foránea que referencia `Usuarios(ID)`  |
| ID_documento     | INTEGER       | Clave foránea que referencia `Documentos(ID)`|
| ID_encargado     | INTEGER       | Clave foránea que referencia `Encargados(ID)`|
| Fecha_solicitud  | TIMESTAMP     | Fecha de la solicitud                        |
| Estado           | TEXT          | Estado de la solicitud                      |

  Claves: 
  Clave primaria: `ID` 
  Claves foráneas: 
  `ID_usuario` que referencia `Usuarios(ID)` //
  `ID_documento` que referencia `Documentos(ID)` //
  `ID_encargado` que referencia `Encargados(ID)` //

    6. Tabla: Comentarios
| Columna           | Tipo de Dato  | Descripción                                      |
|-------------------|---------------|--------------------------------------------------|
| ID                | SERIAL        | Clave primaria, identificador único              |
| Comentario        | TEXT          | Comentario realizado por el encargado            |
| Fecha_comentario  | TIMESTAMP     | Fecha en que se realizó el comentario            |
| ID_solicitud      | INTEGER       | Clave foránea que referencia `Solicitudes(ID)`    |
| ID_encargado      | INTEGER       | Clave foránea que referencia `Encargados(ID)`     |

  Claves:
  Clave primaria  : `ID`
  Claves foráneas  : 
  `ID_solicitud` que referencia `Solicitudes(ID)`
  `ID_encargado` que referencia `Encargados(ID)`

   Relaciones entre tablas
-   Usuarios   y   Solicitudes  : Un usuario puede realizar múltiples solicitudes.
-   Encargados   y   Solicitudes  : Un encargado puede estar asignado a varias solicitudes.
-   Solicitudes   y   Comentarios  : Las solicitudes pueden tener múltiples comentarios asociados, realizados por los encargados.

## Instrucciones de implementación
Para implementar esta base de datos, ejecuta el archivo SQL que contiene la definición de las tablas y asegúrate de asignar los permisos necesarios a los usuarios que interactuarán con la base de datos.

