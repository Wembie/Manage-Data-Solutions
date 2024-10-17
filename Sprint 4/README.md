Equipo Front-End (Juan Daza y Henry Steven)

Historia de Usuario 4: Implementar la Interfaz Basada en el Diseño Escogido

Descripción: Como desarrolladores frontend, queremos implementar la interfaz de usuario basada en el diseño previamente escogido, utilizando React y Tailwind CSS, para que los usuarios interactúen fácilmente con la aplicación.

Criterios de Aceptación:

* Organizar el proyecto de acuerdo con el diseño escogido, estructurando los componentes de la interfaz: menú de navegación, barra lateral, página de inicio y panel de carga de archivos.
* Desarrollar componentes reutilizables para secciones del diseño que se repitan, como tarjetas de archivo, botones de acción, y formularios.
* Implementar Tailwind CSS para estilizar la interfaz según el diseño, asegurando que sea visualmente atractiva y responsiva.
* Crear una página inicial con las secciones básicas de la aplicación (subida de archivos, visualización de archivos, y búsqueda).
* Añadir mensajes de validación visual para guiar al usuario al momento de cargar archivos o navegar en la aplicación.

Historia de Usuario 5: Conectar Frontend con API del Backend para Gestión de Archivos

Descripción: Como desarrolladores frontend, queremos conectar la interfaz de usuario con la API del backend para que el usuario pueda gestionar archivos directamente desde la aplicación.

Criterios de Aceptación:

* Configurar el cliente HTTP en React (por ejemplo, Axios) para realizar peticiones a la API del backend.
* Crear una interfaz que permita al usuario subir un archivo, consultando el endpoint de subida del backend.
* Implementar una vista donde se listen todos los archivos almacenados, obteniéndolos desde el endpoint correspondiente en el backend.
* Añadir funcionalidad para visualizar los detalles de un archivo al seleccionarlo de la lista.
* Implementar un botón de eliminación en cada archivo de la lista, enlazando con el endpoint de borrado en el backend.

Equipo Back-End (Maicol Stiven)

Historia de Usuario 4: Crear Endpoints CRUD para la Gestión de Archivos

Descripción: Como desarrollador backend, quiero implementar los endpoints necesarios para crear, leer, actualizar y eliminar (CRUD) archivos en la base de datos, para permitir al usuario gestionar los documentos en la aplicación.

Criterios de Aceptación:

* Crear el endpoint de subida de archivos, permitiendo almacenar un archivo y sus metadatos en la base de datos.
* Desarrollar un endpoint para listar todos los archivos disponibles en la base de datos.
* Crear un endpoint para obtener los detalles de un archivo específico a partir de su ID.
* Implementar el endpoint de eliminación de archivos, verificando que se eliminen tanto el archivo como sus metadatos asociados.
* Documentar los endpoints utilizando Swagger o ReDoc para que el frontend tenga claro cómo interactuar con la API.

Historia de Usuario 5: Conectar el Backend con la Base de Datos en la Nube

Descripción: Como desarrollador backend, quiero conectar FastAPI con la base de datos SQLite en la nube para que el equipo pueda trabajar de forma colaborativa sobre los datos del proyecto.

Criterios de Aceptación:

* Configurar la conexión entre FastAPI y la base de datos SQLite alojada en un servicio en la nube (como Amazon RDS, Heroku o Supabase).
* Implementar un archivo de configuración para almacenar los parámetros de conexión de manera segura y accesible para el equipo.
* Probar la conexión y realizar peticiones de prueba para asegurarse de que la base de datos responde correctamente.
* Documentar el proceso de conexión para que otros miembros del equipo puedan replicar o modificar la configuración si es necesario.

Equipo de Base de Datos (Jhoan)

Historia de Usuario 4: Subir la Base de Datos a la Nube para Integración con Backend

Descripción: Como administrador de base de datos, quiero subir el esquema de base de datos a un servicio en la nube para que el equipo backend pueda conectarse y gestionar los datos de manera colaborativa.

Criterios de Aceptación:

* Elegir un servicio en la nube adecuado para alojar la base de datos SQLite (como Amazon RDS, Heroku, o Supabase) y configurar la instancia.
* Migrar el esquema de la base de datos a la instancia en la nube, asegurando que las tablas y relaciones se mantengan intactas.
* Crear credenciales de acceso seguro para el backend, incluyendo permisos de lectura y escritura.
* Probar la conexión desde un cliente SQL externo para asegurar que la base de datos esté disponible y funcional.

Historia de Usuario 6: Optimizar y Documentar el Esquema de Base de Datos

Descripción: Como administrador de base de datos, quiero optimizar el esquema y documentarlo para asegurar que cumpla con los requisitos del proyecto y facilite el trabajo del equipo backend.

Criterios de Aceptación:

* Revisar el esquema en busca de posibles optimizaciones, como añadir índices en campos de búsqueda y definir relaciones foráneas necesarias.
* Documentar las tablas y relaciones en un archivo README para el equipo de backend, explicando los campos clave y restricciones.
* Asegurarse de que el esquema esté normalizado y sea eficiente para operaciones de carga y lectura.
* Realizar pruebas de carga en la base de datos para identificar cuellos de botella y verificar el rendimiento.

Duración de Trabajo: Hasta 22/10/2024 11:59 pm. (Si acaban antes lo pueden enviar antes, y asi entregarles el siguiente trabajo para hacerlo) RECUERDEN SUBIR TODO A GITHUB

Entregables: Me deberian enviar por este medio o por privado los avances que tuvieron cada uno. (GITHUB)

Recomendaciones: No usar IA para la resolución de estos trabajos ya que para eso es, para aprender, al usarla no aprenderian y no seria lo ideal ya que esto les servira muchisimo para su carrera profesional, obviamente la pueden usar pero pues ya a consiencia de ustedes, el daño se lo hacen ustedes mismo entonces asi quedamos.

PD-1: Yo se cuando se usa IA, Jajajaja

PD-2: Cada vez el trabajo a aprender se va a poner mas denso entonces para que lo tengan en cuenta, si necesitan mas tiempo o algo asi me avisan

PD-3: Los que faltan por enviarme no se les olvide que luego se les va acumulando el trabajo y es peor

PD IMPORTANTE: EL QUE ACABE ANTES ME DICE PARA COLOCARLE MAS TRABAJO Y IR AVANZANDO

Estare pendiente por si necesitan ayuda en algo o si tienen alguna pregunta no duden en escribirme.
