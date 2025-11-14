"""Modelo de curso para la plataforma E-Learning."""

from datetime import datetime, timezone
from typing import Optional, List


class Instructor:
    """Modelo de instructor embebido en un curso."""

    def __init__(
        self,
        name: str = "Unknown",
        email: str = "",
        user_id: Optional[str] = None,
        avatar_url: str = "/default-avatar.png",
        bio: str = "",
    ):
        self.name = name
        self.email = email
        self.user_id = user_id
        self.avatar_url = avatar_url
        self.bio = bio

    @classmethod
    def from_dict(cls, data: dict) -> "Instructor":
        """Crear instancia desde diccionario."""
        return cls(
            name=data.get("name", "Unknown"),
            email=data.get("email", ""),
            user_id=data.get("userId"),
            avatar_url=data.get("avatarUrl", "/default-avatar.png"),
            bio=data.get("bio", ""),
        )

    def to_dict(self) -> dict:
        """Convertir a diccionario."""
        return {
            "name": self.name,
            "email": self.email,
            "user_id": self.user_id,
            "avatar_url": self.avatar_url,
            "bio": self.bio,
        }


class Lesson:
    """Modelo de lección embebida en un curso."""

    def __init__(
        self,
        title: str = "",
        content: str = "",
        order: int = 0,
        duration: int = 0,
        _id: Optional[str] = None,
    ):
        self.id = str(_id) if _id else None
        self.title = title
        self.content = content
        self.order = order
        self.duration = duration

    @classmethod
    def from_dict(cls, data: dict) -> "Lesson":
        """Crear instancia desde diccionario."""
        return cls(
            _id=data.get("_id"),
            title=data.get("title", ""),
            content=data.get("content", ""),
            order=data.get("order", 0),
            duration=data.get("duration", 0),
        )

    def to_dict(self) -> dict:
        """Convertir a diccionario."""
        return {
            "id": self.id,
            "title": self.title,
            "content": self.content,
            "order": self.order,
            "duration": self.duration,
        }


class Review:
    """Modelo de review embebida en un curso."""

    def __init__(
        self,
        student: str = "",
        rating: int = 5,
        comment: str = "",
        created_at: Optional[datetime] = None,
        _id: Optional[str] = None,
    ):
        self.id = str(_id) if _id else None
        self.student = student
        self.rating = rating
        self.comment = comment
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Review":
        """Crear instancia desde diccionario."""
        return cls(
            _id=data.get("_id"),
            student=data.get("student", ""),
            rating=data.get("rating", 5),
            comment=data.get("comment", ""),
            created_at=data.get("createdAt"),
        )

    def to_dict(self) -> dict:
        """Convertir a diccionario."""
        return {
            "id": self.id,
            "student": self.student,
            "rating": self.rating,
            "comment": self.comment,
            "created_at": self.created_at,
        }


class Course:
    """Modelo completo de curso para MongoDB."""

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
        self.id = str(_id) if _id else None
        self.title = title
        self.description = description
        self.instructor = instructor
        self.price = price
        self.thumbnail = thumbnail
        self.level = level
        self.category = category
        self.categories = categories or []
        self.students = students or []
        self.lessons = lessons or []
        self.reviews = reviews or []
        self.average_rating = average_rating
        self.total_reviews = total_reviews
        self.created_at = created_at or datetime.now(timezone.utc)

    @classmethod
    def from_dict(cls, data: dict) -> "Course":
        """Crear instancia de Course desde un documento de MongoDB."""
        # Parsear instructor
        instructor_data = data.get("instructor", {})
        instructor = Instructor.from_dict(instructor_data) if isinstance(instructor_data, dict) else Instructor()

        # Parsear lecciones
        lessons_data = data.get("lessons", [])
        lessons = [Lesson.from_dict(lesson) for lesson in lessons_data] if isinstance(lessons_data, list) else []

        # Parsear reviews
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
        """Convertir instancia de Course a diccionario."""
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
        """Propiedad para compatibilidad con código existente."""
        return self.instructor.name
