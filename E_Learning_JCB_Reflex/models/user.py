"""
Modelo de usuario para la plataforma E-Learning.

Este módulo define la clase User que representa a todos los tipos de usuarios
del sistema: estudiantes, instructores y administradores.
"""

from datetime import datetime, timezone
from typing import Optional


class User:
    """
    Modelo de usuario para la plataforma E-Learning.

    Representa a estudiantes, instructores y administradores del sistema.
    Los usuarios pueden tener diferentes roles que determinan sus permisos
    y funcionalidades disponibles.

    Atributos:
        id (str): Identificador único del usuario (ObjectId de MongoDB convertido a string)
        first_name (str): Nombre del usuario
        last_name (str): Apellido del usuario
        email (str): Correo electrónico único del usuario
        role (str): Rol del usuario - puede ser "student", "instructor" o "admin"
        password (str): Contraseña hasheada con bcrypt
        instructor_profile (dict): Perfil adicional para instructores (bio, especialidad, etc.)
        enrollments (list): Lista de inscripciones del estudiante a cursos
        courses_created (list): Lista de IDs de cursos creados por el instructor
        created_at (datetime): Fecha y hora de creación de la cuenta
    """

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
        """
        Inicializa una nueva instancia de User.

        Args:
            first_name: Nombre del usuario
            last_name: Apellido del usuario
            email: Correo electrónico único del usuario
            role: Rol del usuario ("student", "instructor" o "admin"). Por defecto "student"
            password: Contraseña hasheada (generada con bcrypt)
            instructor_profile: Perfil adicional para instructores
            enrollments: Lista de inscripciones a cursos
            courses_created: Lista de IDs de cursos creados
            _id: ID de MongoDB (ObjectId)
            created_at: Fecha de creación de la cuenta
        """
        self.id = str(_id) if _id else None
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.role = role  # "student", "instructor", "admin"
        self.password = password  # Hash bcrypt
        self.instructor_profile = instructor_profile or {}
        self.enrollments = enrollments or []  # Solo para estudiantes
        self.courses_created = courses_created or []  # Solo para instructores
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "User":
        """
        Crear instancia de User desde un documento de MongoDB.

        Este método de clase convierte un documento de MongoDB (en formato camelCase)
        a una instancia de la clase User con atributos en snake_case.

        Args:
            data: Diccionario con los datos del usuario desde MongoDB

        Returns:
            User: Nueva instancia de User con los datos proporcionados

        Ejemplo:
            >>> user_doc = {"_id": ObjectId(...), "firstName": "Juan", "email": "juan@email.com"}
            >>> user = User.from_dict(user_doc)
        """
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
        """
        Convertir instancia de User a diccionario para MongoDB.

        Convierte los atributos snake_case de la clase a formato camelCase
        compatible con el esquema de MongoDB. Solo incluye campos con valores
        para evitar guardar datos innecesarios.

        Returns:
            dict: Diccionario con los datos del usuario en formato MongoDB (camelCase)

        Ejemplo:
            >>> user = User(first_name="Juan", last_name="Pérez", email="juan@email.com")
            >>> user_dict = user.to_dict()
            >>> # {"firstName": "Juan", "lastName": "Pérez", "email": "juan@email.com", ...}
        """
        user_dict = {
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "role": self.role,
            "createdAt": self.created_at,
        }

        # Añadir _id si existe (para actualizaciones)
        if self.id:
            user_dict["_id"] = self.id

        # Añadir password solo si existe (no se incluye en respuestas al cliente)
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
        """
        Obtener nombre completo del usuario.

        Returns:
            str: Nombre y apellido concatenados y sin espacios extra

        Ejemplo:
            >>> user = User(first_name="Juan", last_name="Pérez", email="juan@email.com")
            >>> user.get_full_name()
            'Juan Pérez'
        """
        return f"{self.first_name} {self.last_name}".strip()

    @property
    def is_instructor(self) -> bool:
        """
        Verificar si el usuario es instructor.

        Returns:
            bool: True si el rol es "instructor", False en caso contrario
        """
        return self.role == "instructor"

    @property
    def is_student(self) -> bool:
        """
        Verificar si el usuario es estudiante.

        Returns:
            bool: True si el rol es "student", False en caso contrario
        """
        return self.role == "student"

    @property
    def is_admin(self) -> bool:
        """
        Verificar si el usuario es administrador.

        Returns:
            bool: True si el rol es "admin", False en caso contrario
        """
        return self.role == "admin"
