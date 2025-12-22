"""
Servicio de cursos para operaciones de base de datos.

Este módulo proporciona funciones para gestionar cursos en la base de datos MongoDB.
Incluye operaciones CRUD completas, búsqueda y listado de cursos.

Funciones principales:
- get_popular_courses: Obtener cursos populares (limitado)
- get_all_courses: Obtener todos los cursos
- get_course_by_id: Obtener curso por ID
- create_course: Crear nuevo curso
- update_course: Actualizar curso existente
- delete_course: Eliminar curso
"""

from typing import List
from bson import ObjectId
from E_Learning_JCB_Reflex.models.course import Course
from E_Learning_JCB_Reflex.database import MongoDB


async def get_popular_courses(limit: int = 6) -> List[Course]:
    """
    Obtener cursos populares de la plataforma.

    Recupera un número limitado de cursos de la base de datos, típicamente
    para mostrar en la página de inicio o en secciones destacadas.

    Args:
        limit: Número máximo de cursos a retornar. Por defecto 6.

    Returns:
        List[Course]: Lista de objetos Course. Retorna lista vacía si hay error.

    Ejemplo:
        >>> popular = await get_popular_courses(3)
        >>> for course in popular:
        ...     print(course.title)

    Nota:
        Actualmente retorna los primeros cursos encontrados. En el futuro
        se puede ordenar por popularidad (número de estudiantes, calificación, etc.)
    """
    try:
        # Asegurar la conexión a MongoDB
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de cursos
        courses_collection = db["courses"]

        # Recuperar cursos con límite especificado
        cursor = courses_collection.find().limit(limit)
        courses_data = await cursor.to_list(length=limit)

        # Convertir los documentos de MongoDB a objetos Course
        courses = [Course.from_dict(course_data) for course_data in courses_data]

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []

async def get_all_courses() -> List[Course]:
    """
    Obtener todos los cursos de la base de datos.

    Recupera el catálogo completo de cursos disponibles en la plataforma
    sin aplicar ningún filtro o límite.

    Returns:
        List[Course]: Lista completa de objetos Course. Retorna lista vacía si hay error.

    Ejemplo:
        >>> all_courses = await get_all_courses()
        >>> print(f"Total de cursos: {len(all_courses)}")

    Nota:
        Esta función puede retornar una gran cantidad de datos. Considerar
        usar paginación para catálogos muy grandes.
    """
    try:
        # Asegurar la conexión a MongoDB
        await MongoDB.connect()
        db = MongoDB.get_db()

        # Obtener la colección de cursos
        courses_collection = db["courses"]

        # Recuperar todos los cursos sin límite
        cursor = courses_collection.find()
        courses_data = await cursor.to_list(length=None)

        # Convertir los documentos de MongoDB a objetos Course
        courses = [Course.from_dict(course_data) for course_data in courses_data]

        return courses
    except Exception as e:
        print(f"Error fetching courses: {e}")
        return []


async def get_course_by_id(course_id: str) -> Course | None:
    """
    Obtener un curso específico por su ID.

    Busca y retorna un curso individual usando su ObjectId de MongoDB.

    Args:
        course_id: ID del curso (string del ObjectId de MongoDB)

    Returns:
        Course | None: Objeto Course si se encuentra, None si no existe o hay error

    Ejemplo:
        >>> course = await get_course_by_id("507f1f77bcf86cd799439011")
        >>> if course:
        ...     print(f"Curso: {course.title}")
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        courses_collection = db["courses"]
        course_data = await courses_collection.find_one({"_id": ObjectId(course_id)})

        if course_data:
            return Course.from_dict(course_data)
        return None
    except Exception as e:
        print(f"Error fetching course: {e}")
        return None


async def create_course(course_data: dict) -> bool:
    """
    Crear un nuevo curso en la base de datos.

    Inserta un nuevo curso con campos por defecto automáticos como
    fecha de creación y contador de estudiantes inicializado en 0.

    Args:
        course_data: Diccionario con los datos del curso en formato MongoDB (camelCase)

    Returns:
        bool: True si se creó exitosamente, False si hubo error

    Ejemplo:
        >>> course_data = {
        ...     "title": "Python Básico",
        ...     "description": "Aprende Python desde cero",
        ...     "instructor": {...},
        ...     "price": 49.99
        ... }
        >>> success = await create_course(course_data)

    Nota:
        Los campos createdAt y studentsEnrolled se agregan automáticamente.
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        courses_collection = db["courses"]

        # Agregar campos por defecto automáticamente
        from datetime import datetime, timezone
        course_data["createdAt"] = datetime.now(timezone.utc)
        course_data["studentsEnrolled"] = 0

        result = await courses_collection.insert_one(course_data)
        return result.inserted_id is not None
    except Exception as e:
        print(f"Error creating course: {e}")
        return False


async def update_course(course_id: str, update_data: dict) -> bool:
    """
    Actualizar los datos de un curso existente.

    Actualiza campos específicos de un curso usando la operación $set de MongoDB.

    Args:
        course_id: ID del curso a actualizar
        update_data: Diccionario con los campos a actualizar (en formato camelCase)

    Returns:
        bool: True si se encontró el curso (aunque no se haya modificado),
              False si el curso no existe o hay error

    Ejemplo:
        >>> update_data = {"price": 39.99, "level": "intermediate"}
        >>> success = await update_course("507f1f77bcf86cd799439011", update_data)
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        courses_collection = db["courses"]

        result = await courses_collection.update_one(
            {"_id": ObjectId(course_id)},
            {"$set": update_data}
        )

        return result.matched_count > 0
    except Exception as e:
        print(f"Error updating course: {e}")
        return False


async def delete_course(course_id: str) -> bool:
    """
    Eliminar un curso del sistema permanentemente.

    Elimina completamente un curso de la base de datos. Esta operación
    es irreversible.

    Args:
        course_id: ID del curso a eliminar

    Returns:
        bool: True si se eliminó el curso, False si no existe o hay error

    Ejemplo:
        >>> success = await delete_course("507f1f77bcf86cd799439011")
        >>> if success:
        ...     print("Curso eliminado exitosamente")

    Advertencia:
        - Esta operación es IRREVERSIBLE
        - NO elimina automáticamente las inscripciones de estudiantes
        - Considerar manejar la limpieza de datos relacionados antes de eliminar
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        courses_collection = db["courses"]

        result = await courses_collection.delete_one({"_id": ObjectId(course_id)})

        return result.deleted_count > 0
    except Exception as e:
        print(f"Error deleting course: {e}")
        return False
