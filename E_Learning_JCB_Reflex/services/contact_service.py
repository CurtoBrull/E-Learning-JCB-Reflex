"""Contact service for database operations."""

from typing import List
from E_Learning_JCB_Reflex.models.contact import Contact
from E_Learning_JCB_Reflex.database import MongoDB


async def create_contact(name: str, email: str, message: str) -> bool:
    """Crear un nuevo mensaje de contacto en la base de datos."""
    try:
        # Asegurar la conexión
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de contactos
        contacts_collection = db["contacts"]

        # Crear el objeto de contacto
        contact = Contact(name=name, email=email, message=message)

        # Insertar en la base de datos
        result = await contacts_collection.insert_one(contact.to_dict())

        return result.acknowledged
    except Exception as e:
        print(f"Error creating contact: {e}")
        return False


async def get_all_contacts() -> List[Contact]:
    """Obtener todos los mensajes de contacto de la base de datos."""
    try:
        # Asegurar la conexión
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de contactos
        contacts_collection = db["contacts"]

        # Recuperar todos los contactos ordenados por fecha (más recientes primero)
        cursor = contacts_collection.find().sort("createdAt", -1)
        contacts_data = await cursor.to_list(length=None)

        # Convertir los documentos a objetos Contact
        contacts = [Contact.from_dict(contact_data) for contact_data in contacts_data]

        return contacts
    except Exception as e:
        print(f"Error fetching contacts: {e}")
        return []


async def get_contact_by_email(email: str) -> List[Contact]:
    """Obtener mensajes de contacto por email."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        contacts_collection = db["contacts"]
        cursor = contacts_collection.find({"email": email}).sort("createdAt", -1)
        contacts_data = await cursor.to_list(length=None)

        contacts = [Contact.from_dict(contact_data) for contact_data in contacts_data]

        return contacts
    except Exception as e:
        print(f"Error fetching contacts by email: {e}")
        return []
