"""
Modelo de contacto para la plataforma E-Learning.

Este módulo define la clase Contact que representa los mensajes de contacto
enviados por los usuarios a través del formulario de contacto.
"""

from datetime import datetime, timezone
from typing import Optional


class Contact:
    """
    Modelo de mensaje de contacto.

    Representa un mensaje enviado por un usuario a través del formulario de contacto.
    Los mensajes se almacenan en la colección 'contacts' de MongoDB.

    Atributos:
        id (str): Identificador único del mensaje (ObjectId de MongoDB)
        name (str): Nombre de la persona que envía el mensaje
        email (str): Correo electrónico de contacto
        message (str): Contenido del mensaje
        created_at (datetime): Fecha y hora de creación del mensaje
        updated_at (datetime): Fecha y hora de última actualización
    """

    def __init__(
        self,
        name: str,
        email: str,
        message: str,
        _id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        """
        Inicializa una nueva instancia de Contact.

        Args:
            name: Nombre de la persona que envía el mensaje
            email: Correo electrónico de contacto
            message: Contenido del mensaje
            _id: ID de MongoDB (ObjectId)
            created_at: Fecha de creación del mensaje
            updated_at: Fecha de última actualización
        """
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.message = message
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        """
        Crear instancia de Contact desde un documento de MongoDB.

        Args:
            data: Diccionario con los datos del mensaje desde MongoDB

        Returns:
            Contact: Nueva instancia con los datos proporcionados

        Ejemplo:
            >>> contact_doc = db.contacts.find_one({"email": "usuario@email.com"})
            >>> contact = Contact.from_dict(contact_doc)
        """
        return cls(
            _id=data.get("_id"),
            name=data.get("name", ""),
            email=data.get("email", ""),
            message=data.get("message", ""),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
        )

    def to_dict(self) -> dict:
        """
        Convertir instancia de Contact a diccionario para MongoDB.

        Returns:
            dict: Diccionario con los datos del mensaje en formato MongoDB (camelCase)

        Ejemplo:
            >>> contact = Contact(name="Juan", email="juan@email.com", message="Hola")
            >>> contact_dict = contact.to_dict()
        """
        contact_dict = {
            "name": self.name,
            "email": self.email,
            "message": self.message,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

        # Añadir _id si existe (para actualizaciones)
        if self.id:
            contact_dict["_id"] = self.id

        return contact_dict
