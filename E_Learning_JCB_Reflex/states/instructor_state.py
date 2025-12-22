"""
Estado de gestión de instructores.

Este módulo maneja el estado relacionado con la visualización de instructores
en la plataforma, incluyendo listados de todos los instructores y perfiles
individuales con sus cursos y estadísticas.

Funcionalidades principales:
- Cargar lista de todos los instructores
- Cargar perfil detallado de un instructor específico
- Mostrar cursos creados por el instructor
- Calcular estadísticas (total de cursos, estudiantes únicos)
"""

import reflex as rx
from E_Learning_JCB_Reflex.services.user_service import (
    get_all_instructors,
    get_user_by_id,
)
from E_Learning_JCB_Reflex.services.course_service import get_all_courses
from E_Learning_JCB_Reflex.utils.route_helpers import get_dynamic_id


class InstructorState(rx.State):
    """
    Estado para gestión de instructores en la UI.

    Maneja la visualización de información de instructores, incluyendo
    listados completos y perfiles individuales con sus cursos y estadísticas.

    Atributos de estado:
        # Lista de instructores
        instructors (list[dict]): Todos los instructores de la plataforma
        loading (bool): Indicador de carga en progreso
        error (str): Mensaje de error si la operación falla

        # Información del instructor seleccionado
        current_instructor_id (str): ID del instructor actual
        instructor_name (str): Nombre completo del instructor
        instructor_email (str): Email del instructor
        instructor_avatar (str): URL del avatar del instructor
        instructor_bio (str): Biografía del instructor
        instructor_expertise (str): Área de especialización

        # Estadísticas del instructor
        total_courses (int): Número total de cursos creados
        total_students (int): Número total de estudiantes únicos en sus cursos

        # Cursos del instructor
        courses (list[dict]): Lista de cursos creados por el instructor
    """

    instructors: list[dict] = []
    loading: bool = False
    error: str = ""

    # Información básica del instructor seleccionado
    current_instructor_id: str = ""
    instructor_name: str = ""
    instructor_email: str = ""
    instructor_avatar: str = ""
    instructor_bio: str = ""
    instructor_expertise: str = ""

    # Estadísticas
    total_courses: int = 0
    total_students: int = 0

    # Cursos del instructor
    courses: list[dict] = []

    async def load_instructors(self):
        """
        Cargar todos los instructores desde la base de datos.

        Obtiene la lista completa de usuarios con rol "instructor" y extrae
        su información de perfil (avatar, bio, expertise) y estadísticas
        (número de cursos creados).

        Actualiza el estado:
            - instructors: Lista de diccionarios con info de cada instructor
            - loading: True durante carga, False al terminar
            - error: Mensaje si no hay instructores o hay error

        Nota:
            La información de instructor_profile se almacena en el campo
            instructor_profile del modelo User y contiene avatarUrl, bio y expertise.
        """
        self.loading = True
        self.error = ""
        try:
            all_instructors = await get_all_instructors()
            # Convertir objetos User a diccionarios para el estado de Reflex
            self.instructors = [
                {
                    "id": instructor.id,
                    "name": instructor.get_full_name(),
                    "email": instructor.email,
                    "avatar": instructor.instructor_profile.get("avatarUrl", ""),
                    "bio": instructor.instructor_profile.get("bio", ""),
                    "expertise": instructor.instructor_profile.get("expertise", ""),
                    "total_courses": len(instructor.courses_created) if instructor.courses_created else 0,
                }
                for instructor in all_instructors
            ]
            if not self.instructors:
                self.error = "No instructors found in database"
        except Exception as e:
            self.error = f"Error loading instructors: {str(e)}"
            print(f"Error in load_instructors: {e}")
        finally:
            self.loading = False

    async def load_instructor_by_id(self, instructor_id: str):
        """
        Cargar perfil completo de un instructor específico por ID.

        Carga información detallada del instructor incluyendo:
        - Datos personales y de perfil (nombre, email, avatar, bio, expertise)
        - Lista de cursos creados por el instructor
        - Estadísticas (total de cursos, total de estudiantes únicos)

        Args:
            instructor_id: ID del instructor (ObjectId como string)

        Actualiza el estado:
            - Variables del instructor (instructor_name, instructor_email, etc.)
            - total_courses: Número de cursos creados
            - total_students: Número de estudiantes únicos en todos sus cursos
            - courses: Lista de cursos con estadísticas individuales
            - error: Mensaje si el instructor no existe o no tiene rol instructor

        Nota:
            Los estudiantes únicos se calculan usando un set para evitar
            contar duplicados (un estudiante puede estar en varios cursos).
        """
        self.loading = True
        self.error = ""
        try:
            instructor = await get_user_by_id(instructor_id)
            if instructor and instructor.is_instructor:
                # Asignar a variables de estado planas
                self.current_instructor_id = instructor.id
                self.instructor_name = instructor.get_full_name()
                self.instructor_email = instructor.email
                self.instructor_avatar = instructor.instructor_profile.get("avatarUrl", "")
                self.instructor_bio = instructor.instructor_profile.get("bio", "")
                self.instructor_expertise = instructor.instructor_profile.get("expertise", "")

                # Obtener los cursos del instructor
                all_courses = await get_all_courses()
                instructor_courses = [
                    course for course in all_courses
                    if course.id in instructor.courses_created
                ]

                # Estadísticas
                self.total_courses = len(instructor_courses)

                # Calcular total de estudiantes únicos
                unique_students = set()
                for course in instructor_courses:
                    unique_students.update(course.students)
                self.total_students = len(unique_students)

                # Convertir cursos a diccionarios
                self.courses = [
                    {
                        "id": course.id,
                        "title": course.title,
                        "description": course.description,
                        "thumbnail": course.thumbnail,
                        "price": course.price,
                        "level": course.level,
                        "students_count": len(course.students),
                        "average_rating": course.average_rating if course.average_rating else 0,
                    }
                    for course in instructor_courses
                ]
            else:
                self.error = "Instructor no encontrado"
                # Limpiar variables
                self.instructor_name = ""
        except Exception as e:
            self.error = f"Error loading instructor: {str(e)}"
            self.instructor_name = ""
            print(f"Error in load_instructor_by_id: {e}")
        finally:
            self.loading = False

    async def load_instructor_from_url(self):
        """Cargar instructor usando el ID de la URL."""
        # Obtener el instructor_id desde los parámetros de la ruta
        instructor_id = get_dynamic_id(self.router.url.path)
        if instructor_id:
            await self.load_instructor_by_id(instructor_id)
