"""
Configuración de conexión a la base de datos MongoDB.

Este módulo gestiona la conexión a MongoDB utilizando Motor (driver asíncrono)
para operaciones asíncronas con Reflex. También proporciona un cliente síncrono
para operaciones de configuración inicial o pruebas.

Variables de entorno requeridas:
- MONGODB_URI: URI de conexión a MongoDB (ejemplo: mongodb://localhost:27017/elearning)

Ejemplo de MONGODB_URI:
- Local: mongodb://localhost:27017/elearning
- MongoDB Atlas: mongodb+srv://usuario:password@cluster.mongodb.net/elearning
"""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno desde archivo .env
load_dotenv()

# URI de MongoDB desde las variables de entorno
MONGODB_URI = os.getenv("MONGODB_URI")

# Validar que la URI de MongoDB esté configurada
if not MONGODB_URI:
    raise ValueError(
        "MONGODB_URI environment variable is not set. "
        "Please create a .env file with MONGODB_URI=your_mongodb_connection_string"
    )


class MongoDB:
    """
    Gestor de conexión a MongoDB.

    Clase utilitaria que administra una conexión asíncrona a MongoDB usando Motor
    (motor.motor_asyncio.AsyncIOMotorClient). Proporciona métodos de clase para
    establecer y cerrar la conexión, y para obtener la instancia de la base de datos
    para su uso en el resto de la aplicación.

    Atributos de clase
    ------------------
    client : AsyncIOMotorClient | None
        Instancia del cliente asíncrono de Motor. Es None hasta que se llama a connect().
    db : Database | None
        Instancia de la base de datos obtenida del cliente. Es None hasta que se llama a connect().

    Métodos de clase
    ----------------
    connect()
        Crea el cliente asíncrono si aún no existe, configura la propiedad `db`
        extrayendo el nombre de la base de datos del URI o usando la base por defecto.
        Debe llamarse antes de realizar operaciones contra la base de datos.
        No retorna valor; puede imprimir información de conexión para depuración.

    disconnect()
        Cierra el cliente si existe, y restablece `client` y `db` a None.
        Liberar recursos de conexión y dejar la clase en estado inicial.

    get_db() -> Database
        Devuelve la instancia de la base de datos (`db`). Si la conexión no está establecida
        lanza RuntimeError invitando a llamar a connect() primero.

    Parámetros externos
    -------------------
    MONGODB_URI : str
        URI de conexión a MongoDB que se utiliza para inicializar AsyncIOMotorClient.
        Debe estar definido en el contexto de ejecución (por ejemplo, variable de entorno
        o configuración de la aplicación).

    Ejemplo de uso
    --------------
    await MongoDB.connect()
    db = MongoDB.get_db()
    # ... operaciones asíncronas sobre `db` ...
    await MongoDB.disconnect()

    Consideraciones adicionales
    ---------------------------
    - Diseñada para un patrón de conexión a nivel de clase (singleton simple). Si la aplicación
      requiere múltiples clientes o diferentes bases de datos simultáneas, adaptar el diseño.
    - No implementa lógica de reintento ni gestión avanzada de fallos; añadir manejo de errores
      y backoff si es necesario en entornos de producción.
    - Requiere un bucle de eventos asíncrono (asyncio) para ejecutar correctamente los métodos.
    """

    client: AsyncIOMotorClient = None
    db = None

    @classmethod
    async def connect(cls):
        """
        Establecer conexión asíncrona a MongoDB.

        Crea un cliente de Motor (AsyncIOMotorClient) si aún no existe y
        obtiene la base de datos predeterminada del URI de conexión.

        Esta función es idempotente: si ya existe una conexión, no crea una nueva.
        Se debe llamar antes de realizar cualquier operación de base de datos.

        Raises:
            Exception: Si hay un error al conectar con MongoDB

        Ejemplo:
            >>> await MongoDB.connect()
            Connected to MongoDB: elearning
        """
        if cls.client is None:
            # Crear cliente asíncrono de Motor
            cls.client = AsyncIOMotorClient(MONGODB_URI)

            # Extraer nombre de la base de datos del URI o usar la predeterminada
            cls.db = cls.client.get_default_database()

            print(f"Connected to MongoDB: {cls.db.name}")

    @classmethod
    async def disconnect(cls):
        """
        Cerrar la conexión a MongoDB y liberar recursos.

        Cierra el cliente de Motor y restablece las variables de clase a None.
        Útil para limpiar recursos al finalizar la aplicación o en tests.

        Ejemplo:
            >>> await MongoDB.disconnect()
            Disconnected from MongoDB
        """
        if cls.client:
            cls.client.close()
            cls.client = None
            cls.db = None
            print("Disconnected from MongoDB")

    @classmethod
    def get_db(cls):
        """
        Obtener la instancia de la base de datos MongoDB.

        Retorna la instancia de la base de datos para realizar operaciones.
        La conexión debe estar establecida previamente con connect().

        Returns:
            Database: Instancia de la base de datos de Motor

        Raises:
            RuntimeError: Si no se ha llamado a connect() previamente

        Ejemplo:
            >>> await MongoDB.connect()
            >>> db = MongoDB.get_db()
            >>> users = db["users"]  # Obtener colección de usuarios
        """
        if cls.db is None:
            raise RuntimeError(
                "Database not connected. Call MongoDB.connect() first."
            )
        return cls.db


# Cliente síncrono para configuración inicial/pruebas
def get_sync_client():
    """
    Obtener cliente síncrono de MongoDB.

    Crea y retorna un cliente síncrono de PyMongo. Útil para operaciones
    de configuración inicial, scripts de migración o pruebas que no requieren
    async/await.

    Returns:
        MongoClient: Cliente síncrono de PyMongo

    Ejemplo:
        >>> client = get_sync_client()
        >>> db = client.get_default_database()
        >>> users = list(db.users.find({}))

    Nota:
        Para operaciones normales de la aplicación Reflex, usar la clase
        MongoDB con async/await en lugar de este cliente síncrono.
    """
    return MongoClient(MONGODB_URI)
