"""
Modelos de curso para la plataforma E-Learning.

Este módulo define las clases necesarias para representar cursos en el sistema:
- Course: Modelo principal de curso
- Instructor: Información del instructor embebida en el curso
- Lesson: Lecciones individuales del curso
- Review: Reseñas y calificaciones de estudiantes
"""

from datetime import datetime, timezone
from typing import Optional, List


class Instructor:
    """
    Modelo de instructor embebido en un curso.

    Representa la información del instructor asociada a un curso específico.
    Esta información se almacena como un objeto embebido dentro del documento
    de curso en MongoDB para optimizar las consultas.

    Atributos:
        name (str): Nombre completo del instructor
        email (str): Correo electrónico del instructor
        user_id (str): ID del usuario instructor en la colección users
        avatar_url (str): URL del avatar/foto del instructor
        bio (str): Biografía o descripción del instructor
    """

    def __init__(
        self,
        name: str = "Unknown",
        email: str = "",
        user_id: Optional[str] = None,
        avatar_url: str = "/default-avatar.png",
        bio: str = "",
    ):
        """
        Inicializa una nueva instancia de Instructor.

        Args:
            name: Nombre completo del instructor
            email: Correo electrónico del instructor
            user_id: ID del usuario instructor (referencia a colección users)
            avatar_url: URL del avatar del instructor
            bio: Biografía del instructor
        """
        self.name = name
        self.email = email
        self.user_id = user_id
        self.avatar_url = avatar_url
        self.bio = bio

    @classmethod
    def from_dict(cls, data: dict) -> "Instructor":
        """
        Crear instancia de Instructor desde un diccionario.

        Args:
            data: Diccionario con los datos del instructor desde MongoDB

        Returns:
            Instructor: Nueva instancia con los datos proporcionados
        """
        return cls(
            name=data.get("name", "Unknown"),
            email=data.get("email", ""),
            user_id=data.get("userId"),
            avatar_url=data.get("avatarUrl", "/default-avatar.png"),
            bio=data.get("bio", ""),
        )

    def to_dict(self) -> dict:
        """
        Convertir instancia a diccionario.

        Returns:
            dict: Diccionario con los datos del instructor
        """
        return {
            "name": self.name,
            "email": self.email,
            "user_id": self.user_id,
            "avatar_url": self.avatar_url,
            "bio": self.bio,
        }


class Lesson:
    """
    Modelo de lección embebida en un curso.

    Representa una lección individual dentro de un curso. Las lecciones se
    almacenan como un array embebido en el documento de curso.

    Atributos:
        id (str): Identificador único de la lección
        title (str): Título de la lección
        content (str): Contenido de la lección (puede ser texto, HTML, markdown, etc.)
        order (int): Orden de la lección en el curso (para mantener secuencia)
        duration (int): Duración estimada de la lección en minutos
        video_url (str): URL del video de YouTube para la lección
    """

    def __init__(
        self,
        title: str = "",
        content: str = "",
        order: int = 0,
        duration: int = 0,
        video_url: str = "",
        _id: Optional[str] = None,
    ):
        """
        Inicializa una nueva instancia de Lesson.

        Args:
            title: Título de la lección
            content: Contenido de la lección
            order: Posición de la lección en el curso (1, 2, 3...)
            duration: Duración en minutos
            video_url: URL del video de YouTube
            _id: ID único de la lección
        """
        self.id = str(_id) if _id else None
        self.title = title
        self.content = content
        self.order = order  # Orden de la lección en el curso
        self.duration = duration  # Duración en minutos
        self.video_url = video_url  # URL del video de YouTube

    @classmethod
    def from_dict(cls, data: dict) -> "Lesson":
        """
        Crear instancia de Lesson desde un diccionario.

        Args:
            data: Diccionario con los datos de la lección

        Returns:
            Lesson: Nueva instancia con los datos proporcionados
        """
        return cls(
            _id=data.get("_id"),
            title=data.get("title", ""),
            content=data.get("content", ""),
            order=data.get("order", 0),
            duration=data.get("duration", 0),
            video_url=data.get("video_url", ""),
        )

    def to_dict(self) -> dict:
        """
        Convertir instancia a diccionario.

        Returns:
            dict: Diccionario con los datos de la lección
        """
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "order": self.order,
            "duration": self.duration,
            "video_url": self.video_url,
        }


class Review:
    """
    Modelo de reseña/calificación embebida en un curso.

    Representa una reseña y calificación que un estudiante hace de un curso.
    Las reseñas se almacenan como un array embebido en el documento de curso.

    Atributos:
        id (str): Identificador único de la reseña
        student (str): ID del estudiante que escribió la reseña
        rating (int): Calificación del curso (1-5 estrellas)
        comment (str): Comentario o reseña escrita por el estudiante
        created_at (datetime): Fecha y hora de creación de la reseña
    """

    def __init__(
        self,
        student: str = "",
        rating: int = 5,
        comment: str = "",
        created_at: Optional[datetime] = None,
        _id: Optional[str] = None,
    ):
        """
        Inicializa una nueva instancia de Review.

        Args:
            student: ID del estudiante que escribió la reseña
            rating: Calificación de 1 a 5 estrellas
            comment: Comentario del estudiante
            created_at: Fecha de creación de la reseña
            _id: ID único de la reseña
        """
        self.id = str(_id) if _id else None
        self.student = student  # ID del estudiante
        self.rating = rating  # Calificación de 1 a 5
        self.comment = comment
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Review":
        """
        Crear instancia de Review desde un diccionario.

        Args:
            data: Diccionario con los datos de la reseña

        Returns:
            Review: Nueva instancia con los datos proporcionados
        """
        return cls(
            _id=data.get("_id"),
            student=data.get("student", ""),
            rating=data.get("rating", 5),
            comment=data.get("comment", ""),
            created_at=data.get("createdAt"),
        )

    def to_dict(self) -> dict:
        """
        Convertir instancia a diccionario.

        Returns:
            dict: Diccionario con los datos de la reseña
        """
        return {
            "id": self.id,
            "student": self.student,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
        }


class Course:
    """
    Modelo completo de curso para MongoDB.

    Representa un curso en la plataforma E-Learning con toda su información:
    datos básicos, instructor, lecciones, estudiantes inscritos y reseñas.

    Atributos:
        id (str): Identificador único del curso (ObjectId de MongoDB)
        title (str): Título del curso
        description (str): Descripción detallada del curso
        instructor (Instructor): Objeto con información del instructor
        price (float): Precio del curso en la moneda configurada
        thumbnail (str): URL de la imagen de portada del curso
        level (str): Nivel del curso ("beginner", "intermediate", "advanced")
        category (str): Categoría principal del curso
        categories (List[str]): Lista de categorías a las que pertenece el curso
        students (List[str]): Lista de IDs de estudiantes inscritos
        lessons (List[Lesson]): Lista de lecciones del curso
        reviews (List[Review]): Lista de reseñas del curso
        average_rating (int): Calificación promedio del curso (calculada)
        total_reviews (int): Número total de reseñas (calculado)
        created_at (datetime): Fecha y hora de creación del curso
    """

    def __init__(
        self,
        title: str,
        description: str,
        instructor: Instructor,
        price: float = 0.0,
        thumbnail: str = "/placeholder-course.jpg",
        level: str = "beginner",
        category: str = "",
        categories: Optional[List[str]] = None,
        students: Optional[List[str]] = None,
        lessons: Optional[List[Lesson]] = None,
        reviews: Optional[List[Review]] = None,
        average_rating: Optional[int] = None,
        total_reviews: Optional[int] = None,
        _id: Optional[str] = None,
        created_at: Optional[datetime] = None,
    ):
        """
        Inicializa una nueva instancia de Course.

        Args:
            title: Título del curso
            description: Descripción detallada del curso
            instructor: Objeto Instructor con la información del instructor
            price: Precio del curso (por defecto 0.0 para cursos gratuitos)
            thumbnail: URL de la imagen del curso
            level: Nivel de dificultad ("beginner", "intermediate", "advanced")
            category: Categoría principal del curso
            categories: Lista de categorías
            students: Lista de IDs de estudiantes inscritos
            lessons: Lista de objetos Lesson
            reviews: Lista de objetos Review
            average_rating: Calificación promedio (calculada automáticamente)
            total_reviews: Total de reseñas (calculado automáticamente)
            _id: ID de MongoDB
            created_at: Fecha de creación
        """
        self.id = str(_id) if _id else None
        self.title = title
        self.description = description
        self.instructor = instructor  # Objeto Instructor embebido
        self.price = price
        self.thumbnail = thumbnail
        self.level = level  # "beginner", "intermediate", "advanced"
        self.category = category
        self.categories = categories or []
        self.students = students or []  # IDs de estudiantes inscritos
        self.lessons = lessons or []  # Lecciones del curso
        self.reviews = reviews or []  # Reseñas del curso
        self.average_rating = average_rating  # Calculado de las reviews
        self.total_reviews = total_reviews  # Calculado de las reviews
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Course":
        """
        Crear instancia de Course desde un documento de MongoDB.

        Este método deserializa un documento de MongoDB y crea objetos Python
        completos incluyendo todos los objetos embebidos (instructor, lecciones, reviews).

        Args:
            data: Diccionario con el documento de curso desde MongoDB

        Returns:
            Course: Nueva instancia con todos los datos deserializados

        Ejemplo:
            >>> course_doc = db.courses.find_one({"_id": ObjectId(...)})
            >>> course = Course.from_dict(course_doc)
        """
        # Parsear instructor (objeto embebido)
        instructor_data = data.get("instructor", {})
        instructor = Instructor.from_dict(instructor_data) if isinstance(instructor_data, dict) else Instructor()

        # Parsear lecciones (array de objetos embebidos)
        lessons_data = data.get("lessons", [])
        lessons = [Lesson.from_dict(lesson) for lesson in lessons_data] if isinstance(lessons_data, list) else []

        # Parsear reviews (array de objetos embebidos)
        reviews_data = data.get("reviews", [])
        reviews = [Review.from_dict(review) for review in reviews_data] if isinstance(reviews_data, list) else []

        return cls(
            _id=data.get("_id"),
            title=data.get("title", ""),
            description=data.get("description", ""),
            instructor=instructor,
            price=data.get("price", 0.0),
            thumbnail=data.get("image", "/placeholder-course.jpg"),
            level=data.get("level", "beginner"),
            category=data.get("category", ""),
            categories=data.get("categories", []),
            students=data.get("students", []),
            lessons=lessons,
            reviews=reviews,
            average_rating=data.get("averageRating"),
            total_reviews=data.get("totalReviews"),
            created_at=data.get("createdAt"),
        )

    def to_dict(self) -> dict:
        """
        Convertir instancia de Course a diccionario.

        Serializa el objeto Course y todos sus objetos embebidos a un
        diccionario compatible con MongoDB.

        Returns:
            dict: Diccionario con todos los datos del curso serializados

        Ejemplo:
            >>> course = Course(title="Python Básico", ...)
            >>> course_dict = course.to_dict()
            >>> # Listo para insertar en MongoDB
        """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "instructor": self.instructor.to_dict(),
            "price": self.price,
            "thumbnail": self.thumbnail,
            "level": self.level,
            "category": self.category,
            "categories": self.categories,
            "students": self.students,
            "lessons": [lesson.to_dict() for lesson in self.lessons],
            "reviews": [review.to_dict() for review in self.reviews],
            "average_rating": self.average_rating,
            "total_reviews": self.total_reviews,
            "created_at": self.created_at,
        }

    @property
    def instructor_name(self) -> str:
        """
        Obtener nombre del instructor del curso.

        Propiedad de conveniencia para acceder al nombre del instructor
        sin necesidad de acceder al objeto instructor directamente.

        Returns:
            str: Nombre completo del instructor

        Ejemplo:
            >>> course.instructor_name
            'Dr. Juan Pérez'
        """
        return self.instructor.name
