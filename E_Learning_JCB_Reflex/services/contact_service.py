"""
Servicio de contacto para operaciones de base de datos.

Este módulo proporciona funciones para gestionar mensajes de contacto
enviados por los usuarios a través del formulario de contacto.

Funciones principales:
- create_contact: Crear nuevo mensaje de contacto
- get_all_contacts: Obtener todos los mensajes
- get_contact_by_email: Buscar mensajes por email del remitente
"""

from typing import List
from E_Learning_JCB_Reflex.models.contact import Contact
from E_Learning_JCB_Reflex.database import MongoDB


async def create_contact(name: str, email: str, message: str) -> bool:
    """
    Crear un nuevo mensaje de contacto en la base de datos.

    Guarda un mensaje enviado por un usuario a través del formulario de contacto.
    Los campos de fecha se generan automáticamente.

    Args:
        name: Nombre de la persona que envía el mensaje
        email: Correo electrónico de contacto
        message: Contenido del mensaje

    Returns:
        bool: True si se creó exitosamente, False si hubo error

    Ejemplo:
        >>> success = await create_contact(
        ...     name="Juan Pérez",
        ...     email="juan@email.com",
        ...     message="Tengo una pregunta sobre el curso de Python"
        ... )
        >>> if success:
        ...     print("Mensaje enviado exitosamente")

    Nota:
        Los campos created_at y updated_at se establecen automáticamente
        en el modelo Contact.
    """
    try:
        # Asegurar la conexión a MongoDB
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de contactos
        contacts_collection = db["contacts"]

        # Crear el objeto de contacto (fechas automáticas)
        contact = Contact(name=name, email=email, message=message)

        # Insertar en la base de datos
        result = await contacts_collection.insert_one(contact.to_dict())

        return result.acknowledged
    except Exception as e:
        print(f"Error creating contact: {e}")
        return False


async def get_all_contacts() -> List[Contact]:
    """
    Obtener todos los mensajes de contacto de la base de datos.

    Recupera todos los mensajes ordenados por fecha de creación
    (más recientes primero). Útil para que los administradores
    revisen los mensajes recibidos.

    Returns:
        List[Contact]: Lista de objetos Contact ordenados por fecha descendente.
                       Retorna lista vacía si hay error.

    Ejemplo:
        >>> contacts = await get_all_contacts()
        >>> for contact in contacts:
        ...     print(f"{contact.name}: {contact.message[:50]}...")

    Nota:
        Los contactos se ordenan automáticamente por createdAt en orden
        descendente para mostrar los más recientes primero.
    """
    try:
        # Asegurar la conexión a MongoDB
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de contactos
        contacts_collection = db["contacts"]

        # Recuperar todos los contactos ordenados por fecha (más recientes primero)
        cursor = contacts_collection.find().sort("createdAt", -1)
        contacts_data = await cursor.to_list(length=None)

        # Convertir los documentos de MongoDB a objetos Contact
        contacts = [Contact.from_dict(contact_data) for contact_data in contacts_data]

        return contacts
    except Exception as e:
        print(f"Error fetching contacts: {e}")
        return []


async def get_contact_by_email(email: str) -> List[Contact]:
    """
    Obtener mensajes de contacto por email del remitente.

    Busca todos los mensajes enviados por un email específico,
    ordenados por fecha de creación descendente.

    Args:
        email: Correo electrónico a buscar

    Returns:
        List[Contact]: Lista de objetos Contact del email especificado.
                       Retorna lista vacía si no hay mensajes o hay error.

    Ejemplo:
        >>> messages = await get_contact_by_email("juan@email.com")
        >>> print(f"Total de mensajes: {len(messages)}")
        >>> for msg in messages:
        ...     print(f"- {msg.created_at}: {msg.message}")

    Nota:
        Útil para rastrear el historial de comunicación con un usuario
        específico o para detectar spam.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        contacts_collection = db["contacts"]

        # Buscar por email y ordenar por fecha descendente
        cursor = contacts_collection.find({"email": email}).sort("createdAt", -1)
        contacts_data = await cursor.to_list(length=None)

        # Convertir a objetos Contact
        contacts = [Contact.from_dict(contact_data) for contact_data in contacts_data]

        return contacts
    except Exception as e:
        print(f"Error fetching contacts by email: {e}")
        return []
