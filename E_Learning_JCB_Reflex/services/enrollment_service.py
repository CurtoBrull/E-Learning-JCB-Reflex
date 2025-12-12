"""Servicio de inscripción de estudiantes a cursos."""

from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from E_Learning_JCB_Reflex.database import MongoDB


async def enroll_student(user_id: str, course_id: str) -> bool:
    """
    Inscribir un estudiante en un curso.

    Args:
        user_id: ID del usuario estudiante
        course_id: ID del curso

    Returns:
        bool: True si la inscripción fue exitosa, False en caso contrario
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        courses_collection = db["courses"]

        # Verificar que el usuario existe y es estudiante
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if not user or user.get("role") != "student":
            print(f"Usuario no encontrado o no es estudiante: {user_id}")
            return False

        # Verificar que el curso existe
        course = await courses_collection.find_one({"_id": ObjectId(course_id)})
        if not course:
            print(f"Curso no encontrado: {course_id}")
            return False

        # Verificar si ya está inscrito
        if "enrolledCourses" not in user:
            user["enrolledCourses"] = []

        for enrollment in user["enrolledCourses"]:
            if str(enrollment.get("courseId")) == course_id:
                print(f"Usuario ya inscrito en el curso: {course_id}")
                return False

        # Crear la inscripción
        enrollment = {
            "courseId": ObjectId(course_id),
            "enrolledAt": datetime.utcnow(),
            "progress": 0,
            "completedLessons": [],
            "status": "active"
        }

        # Actualizar el usuario
        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$push": {"enrolledCourses": enrollment}}
        )

        # Incrementar el contador de estudiantes en el curso
        await courses_collection.update_one(
            {"_id": ObjectId(course_id)},
            {"$inc": {"studentsEnrolled": 1}}
        )

        print(f"Inscripción exitosa: usuario {user_id} en curso {course_id}")
        return result.modified_count > 0

    except Exception as e:
        print(f"Error al inscribir estudiante: {e}")
        return False


async def unenroll_student(user_id: str, course_id: str) -> bool:
    """
    Desinscribir un estudiante de un curso.

    Args:
        user_id: ID del usuario estudiante
        course_id: ID del curso

    Returns:
        bool: True si la desinscripción fue exitosa, False en caso contrario
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        courses_collection = db["courses"]

        # Eliminar la inscripción del usuario
        result = await users_collection.update_one(
            {"_id": ObjectId(user_id)},
            {"$pull": {"enrolledCourses": {"courseId": ObjectId(course_id)}}}
        )

        if result.modified_count > 0:
            # Decrementar el contador de estudiantes en el curso
            await courses_collection.update_one(
                {"_id": ObjectId(course_id)},
                {"$inc": {"studentsEnrolled": -1}}
            )
            print(f"Desinscripción exitosa: usuario {user_id} de curso {course_id}")
            return True

        print(f"No se encontró la inscripción: usuario {user_id} curso {course_id}")
        return False

    except Exception as e:
        print(f"Error al desinscribir estudiante: {e}")
        return False


async def is_enrolled(user_id: str, course_id: str) -> bool:
    """
    Verificar si un estudiante está inscrito en un curso.

    Args:
        user_id: ID del usuario estudiante
        course_id: ID del curso

    Returns:
        bool: True si está inscrito, False en caso contrario
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if not user or "enrolledCourses" not in user:
            return False

        for enrollment in user["enrolledCourses"]:
            if str(enrollment.get("courseId")) == course_id:
                return True

        return False

    except Exception as e:
        print(f"Error al verificar inscripción: {e}")
        return False


async def get_student_enrollments(user_id: str) -> List[dict]:
    """
    Obtener todas las inscripciones de un estudiante con la información completa de los cursos.

    Args:
        user_id: ID del usuario estudiante

    Returns:
        List[dict]: Lista de cursos inscritos con información completa
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]
        courses_collection = db["courses"]

        # Obtener el usuario
        user = await users_collection.find_one({"_id": ObjectId(user_id)})
        if not user or "enrolledCourses" not in user:
            return []

        # Obtener información completa de cada curso
        enrolled_courses = []
        for enrollment in user["enrolledCourses"]:
            course_id = enrollment.get("courseId")
            if course_id:
                course = await courses_collection.find_one({"_id": course_id})
                if course:
                    course_data = {
                        "id": str(course["_id"]),
                        "title": course.get("title", ""),
                        "description": course.get("description", ""),
                        "thumbnail": course.get("image", "/placeholder-course.jpg"),
                        "instructor_name": course.get("instructor", {}).get("name", "Unknown"),
                        "price": course.get("price", 0),
                        "level": course.get("level", "beginner"),
                        "progress": enrollment.get("progress", 0),
                        "enrolledAt": str(enrollment.get("enrolledAt", "")),
                        "status": enrollment.get("status", "active"),
                    }
                    enrolled_courses.append(course_data)

        return enrolled_courses

    except Exception as e:
        print(f"Error al obtener inscripciones: {e}")
        return []
