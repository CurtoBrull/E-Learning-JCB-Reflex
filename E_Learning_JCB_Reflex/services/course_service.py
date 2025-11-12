"""Course service for database operations."""

from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from E_Learning_JCB_Reflex.models.course import Course
from E_Learning_JCB_Reflex.database import MongoDB


async def get_all_courses() -> List[Course]:
    """Get all courses from database."""
    try:
        # Asegurar la conexión
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de cursos
        courses_collection = db["courses"]

        # Recuperar todos los cursos (máximo 10)
        cursor = courses_collection.find().limit(10)
        courses_data = await cursor.to_list(length=10)

        # Convertir los documentos a objetos Course
        courses = [Course.from_dict(course_data) for course_data in courses_data]

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []


async def get_course_by_id(course_id: str) -> Course | None:
    """Get a single course by ID."""
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        courses_collection = db["courses"]
        course_data = await courses_collection.find_one({"_id": course_id})

        if course_data:
            return Course.from_dict(course_data)
        return None
    except Exception as e:
        print(f"Error fetching course: {e}")
        return None
