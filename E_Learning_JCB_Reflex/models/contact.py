"""Modelo de contacto para la plataforma E-Learning."""

from datetime import datetime, timezone
from typing import Optional


class Contact:
    """Modelo de mensaje de contacto."""

    def __init__(
        self,
        name: str,
        email: str,
        message: str,
        _id: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ):
        self.id = str(_id) if _id else None
        self.name = name
        self.email = email
        self.message = message
        self.created_at = created_at or datetime.now(timezone.utc)
        self.updated_at = updated_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Contact":
        """Crear instancia de Contact desde un documento de MongoDB."""
        return cls(
            _id=data.get("_id"),
            name=data.get("name", ""),
            email=data.get("email", ""),
            message=data.get("message", ""),
            created_at=data.get("createdAt"),
            updated_at=data.get("updatedAt"),
        )

    def to_dict(self) -> dict:
        """Convertir instancia de Contact a diccionario para MongoDB."""
        contact_dict = {
            "name": self.name,
            "email": self.email,
            "message": self.message,
            "createdAt": self.created_at,
            "updatedAt": self.updated_at,
        }

        if self.id:
            contact_dict["_id"] = self.id

        return contact_dict
