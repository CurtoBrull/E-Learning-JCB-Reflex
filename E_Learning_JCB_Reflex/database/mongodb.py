"""Configuración de conexión a la base de datos MongoDB."""

import os
from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# URI de MongoDB desde las variables de entorno
MONGODB_URI = os.getenv("MONGODB_URI")

if not MONGODB_URI:
    raise ValueError("MONGODB_URI environment variable is not set")


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
        """Conectar a MongoDB."""
        if cls.client is None:
            cls.client = AsyncIOMotorClient(MONGODB_URI)
            # Extraer nombre de la base de datos del URI o usar la predeterminada
            cls.db = cls.client.get_default_database()
            print(f"Connected to MongoDB: {cls.db.name}")

    @classmethod
    async def disconnect(cls):
        """Desconectar de MongoDB."""
        if cls.client:
            cls.client.close()
            cls.client = None
            cls.db = None
            print("Disconnected from MongoDB")

    @classmethod
    def get_db(cls):
        """Obtener instancia de la base de datos."""
        if cls.db is None:
            raise RuntimeError("Database not connected. Call connect() first.")
        return cls.db


# Cliente síncrono para configuración inicial/pruebas
def get_sync_client():
    """Obtener cliente síncrono de MongoDB."""
    return MongoClient(MONGODB_URI)
