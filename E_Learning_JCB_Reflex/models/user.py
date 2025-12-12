"""Modelo de usuario para la plataforma E-Learning."""

from datetime import datetime, timezone
from typing import Optional


class User:
    """Modelo de usuario (estudiantes, instructores, administradores)."""

    def __init__(
        self,
        first_name: str,
        last_name: str,
        email: str,
        role: str = "student",
        password: Optional[str] = None,
        instructor_profile: Optional[dict] = None,
        enrollments: Optional[list] = None,
        courses_created: Optional[list] = None,
        _id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        self.id = str(_id) if _id else None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role
        self.password = password
        self.instructor_profile = instructor_profile or {}
        self.enrollments = enrollments or []
        self.courses_created = courses_created or []
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """Crear instancia de User desde un documento de MongoDB."""
        return cls(
            _id=data.get("_id"),
            first_name=data.get("firstName", ""),
            last_name=data.get("lastName", ""),
            email=data.get("email", ""),
            role=data.get("role", "student"),
            password=data.get("password"),
            instructor_profile=data.get("instructorProfile"),
            enrollments=data.get("enrollments", []),
            courses_created=data.get("coursesCreated", []),
            created_at=data.get("createdAt"),
        )

    def to_dict(self) -> dict:
        """Convertir instancia de User a diccionario para MongoDB (camelCase)."""
        user_dict = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "role": self.role,
            "createdAt": self.created_at,
        }

        # Añadir _id si existe
        if self.id:
            user_dict["_id"] = self.id

        # Añadir password solo si existe
        if self.password:
            user_dict["password"] = self.password

        # Añadir campos opcionales solo si tienen contenido
        if self.instructor_profile:
            user_dict["instructorProfile"] = self.instructor_profile

        if self.enrollments:
            user_dict["enrollments"] = self.enrollments

        if self.courses_created:
            user_dict["coursesCreated"] = self.courses_created

        return user_dict

    def get_full_name(self) -> str:
        """Obtener nombre completo del usuario."""
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_instructor(self) -> bool:
        """Verificar si el usuario es instructor."""
        return self.role == "instructor"

    @property
    def is_student(self) -> bool:
        """Verificar si el usuario es estudiante."""
        return self.role == "student"

    @property
    def is_admin(self) -> bool:
        """Verificar si el usuario es administrador."""
        return self.role == "admin"
