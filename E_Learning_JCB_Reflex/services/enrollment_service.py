"""
Servicio de inscripción de estudiantes a cursos.

Este módulo gestiona todas las operaciones relacionadas con las inscripciones
de estudiantes en cursos, incluyendo inscripción, desinscripción, verificación
y obtención de información de cursos inscritos.

Funcionalidades:
- Inscribir estudiantes en cursos (con validaciones)
- Desinscribir estudiantes de cursos
- Verificar si un estudiante está inscrito en un curso
- Obtener lista completa de inscripciones de un estudiante
- Contar inscripciones totales en la plataforma

Colecciones MongoDB utilizadas:
- users: Para gestionar enrolledCourses del estudiante
- courses: Para actualizar contador de studentsEnrolled
"""

from typing import List, Optional
from datetime import datetime
from bson import ObjectId
from E_Learning_JCB_Reflex.database import MongoDB


async def enroll_student(user_id: str, course_id: str) -> bool:
    """
    Inscribe un estudiante en un curso específico.

    Realiza las siguientes validaciones y operaciones:
    1. Verifica que el usuario existe y tiene rol "student"
    2. Verifica que el curso existe
    3. Comprueba que el estudiante no esté ya inscrito
    4. Crea un objeto de inscripción con progreso inicial en 0
    5. Actualiza el array enrolledCourses del usuario
    6. Incrementa el contador studentsEnrolled del curso

    Args:
        user_id: ID del usuario estudiante (formato ObjectId en string)
        course_id: ID del curso (formato ObjectId en string)

    Returns:
        bool: True si la inscripción fue exitosa, False si falló alguna validación
              o hubo un error en la base de datos

    Ejemplos:
        >>> await enroll_student("507f1f77bcf86cd799439011", "507f191e810c19729de860ea")
        True

    Notas:
        - Solo permite inscripción a usuarios con rol "student"
        - Previene inscripciones duplicadas
        - El objeto de inscripción incluye: courseId, enrolledAt, progress,
          completedLessons y status
        - Imprime mensajes de log en consola para debugging
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
    Desinscribe un estudiante de un curso, eliminando su registro de inscripción.

    Realiza las siguientes operaciones:
    1. Elimina la inscripción del array enrolledCourses del usuario
    2. Decrementa el contador studentsEnrolled del curso
    3. Elimina todo el progreso asociado a esa inscripción

    Args:
        user_id: ID del usuario estudiante (formato ObjectId en string)
        course_id: ID del curso (formato ObjectId en string)

    Returns:
        bool: True si la desinscripción fue exitosa (se encontró y eliminó),
              False si no se encontró la inscripción o hubo un error

    Ejemplos:
        >>> await unenroll_student("507f1f77bcf86cd799439011", "507f191e810c19729de860ea")
        True

    Notas:
        - Elimina permanentemente todo el progreso del estudiante en el curso
        - Utiliza operador $pull de MongoDB para eliminar del array
        - Solo decrementa el contador si se eliminó exitosamente la inscripción
        - Imprime mensajes de log en consola para debugging
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
    Verifica si un estudiante está actualmente inscrito en un curso.

    Busca en el array enrolledCourses del usuario para determinar
    si existe una inscripción para el curso especificado.

    Args:
        user_id: ID del usuario estudiante (formato ObjectId en string)
        course_id: ID del curso (formato ObjectId en string)

    Returns:
        bool: True si el estudiante está inscrito en el curso,
              False si no está inscrito, el usuario no existe,
              o no tiene inscripciones

    Ejemplos:
        >>> await is_enrolled("507f1f77bcf86cd799439011", "507f191e810c19729de860ea")
        True

    Notas:
        - Retorna False si el usuario no tiene el campo enrolledCourses
        - Compara el courseId usando string para evitar problemas de tipo
        - Útil para validar antes de inscribir o mostrar botones condicionales
        - Maneja excepciones y retorna False en caso de error
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
    Obtiene todas las inscripciones de un estudiante con información completa de cada curso.

    Para cada inscripción, realiza un lookup del curso en la colección de cursos
    para obtener información detallada como título, descripción, instructor, etc.
    Combina la información del curso con los datos de progreso de la inscripción.

    Args:
        user_id: ID del usuario estudiante (formato ObjectId en string)

    Returns:
        List[dict]: Lista de diccionarios con la siguiente estructura:
            - id: ID del curso (string)
            - title: Título del curso
            - description: Descripción del curso
            - thumbnail: URL de la imagen (o placeholder si no existe)
            - instructor_name: Nombre del instructor
            - price: Precio del curso
            - level: Nivel del curso (beginner/intermediate/advanced)
            - progress: Porcentaje de progreso (0-100)
            - enrolledAt: Fecha de inscripción (string ISO)
            - status: Estado de la inscripción (active/completed)

    Ejemplos:
        >>> enrollments = await get_student_enrollments("507f1f77bcf86cd799439011")
        >>> print(len(enrollments))
        3
        >>> print(enrollments[0]['title'])
        'Introducción a Python'

    Notas:
        - Retorna lista vacía si el usuario no existe o no tiene inscripciones
        - Solo incluye cursos que aún existen en la base de datos
        - Usa imagen placeholder si el curso no tiene imagen configurada
        - Útil para mostrar el dashboard del estudiante con progreso
        - Maneja excepciones y retorna lista vacía en caso de error
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


async def count_total_enrollments() -> int:
    """
    Cuenta el total de inscripciones activas en toda la plataforma.

    Itera sobre todos los usuarios con rol "student" y suma la cantidad
    de cursos en su array enrolledCourses para obtener el total global
    de inscripciones.

    Returns:
        int: Número total de inscripciones activas en la plataforma.
             Retorna 0 si no hay inscripciones o si hay un error.

    Ejemplos:
        >>> total = await count_total_enrollments()
        >>> print(f"Total de inscripciones: {total}")
        Total de inscripciones: 156

    Notas:
        - Solo cuenta inscripciones de usuarios con rol "student"
        - Cuenta todas las inscripciones sin importar su estado
        - Útil para estadísticas del dashboard de administrador
        - Puede ser lento si hay muchos estudiantes (considera cachear)
        - Retorna 0 en caso de error y lo imprime en consola
    """
    try:
        await MongoDB.connect()
        db = MongoDB.get_db()

        users_collection = db["users"]

        # Contar inscripciones de todos los estudiantes
        total = 0
        cursor = users_collection.find({"role": "student"})
        async for user in cursor:
            if "enrolledCourses" in user:
                total += len(user["enrolledCourses"])

        return total

    except Exception as e:
        print(f"Error al contar inscripciones: {e}")
        return 0
