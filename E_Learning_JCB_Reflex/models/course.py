"""Modelo de curso para la plataforma E-Learning."""

from datetime import datetime, timezone
from typing import Optional


class Course:
    """Modelo simple de curso para MongoDB."""

    def __init__(
        self,
        title: str,
        description: str,
        instructor_name: str,
        price: float = 0.0,
        thumbnail: str = "/placeholder-course.jpg",
        level: str = "beginner",
        _id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        self.id = str(_id) if _id else None
        self.title = title
        self.description = description
        self.instructor_name = instructor_name
        self.price = price
        self.thumbnail = thumbnail
        self.level = level
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Course":
        """Crear instancia de Course desde un documento de MongoDB."""
        return cls(
            _id=data.get("_id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            instructor_name=data.get("instructor_name", "Unknown"),
            price=data.get("price", 0.0),
            thumbnail=data.get("thumbnail", "/placeholder-course.jpg"),
            level=data.get("level", "beginner"),
            created_at=data.get("created_at"),
        )

    def to_dict(self) -> dict:
        """Convertir instancia de Course a diccionario."""
        return {
            "title": self.title,
            "description": self.description,
            "instructor_name": self.instructor_name,
            "price": self.price,
            "thumbnail": self.thumbnail,
            "level": self.level,
            "created_at": self.created_at,
        }
