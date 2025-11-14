"""Course service for database operations."""

from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from E_Learning_JCB_Reflex.models.course import Course
from E_Learning_JCB_Reflex.database import MongoDB

async def get_popular_courses(limit: int = 6) -> List[Course]:
    """Mostra algunos cursos de la base de datos."""
    try:
        # Asegurar la conexión
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de cursos
        courses_collection = db["courses"]

        # Recuperar cursos con límite especificado
        cursor = courses_collection.find().limit(limit)
        courses_data = await cursor.to_list(length=limit)

        # Convertir los documentos a objetos Course
        courses = [Course.from_dict(course_data) for course_data in courses_data]

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []

async def get_all_courses() -> List[Course]:
    """Obtener todos los cursos de la base de datos."""
    try:
        # Asegurar la conexión
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de cursos
        courses_collection = db["courses"]

        # Recuperar todos los cursos sin límite
        cursor = courses_collection.find()
        courses_data = await cursor.to_list(length=None)

        # Convertir los documentos a objetos Course
        courses = [Course.from_dict(course_data) for course_data in courses_data]

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []


async def get_course_by_id(course_id: str) -> Course | None:
    """Obtener un curso por ID."""
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
