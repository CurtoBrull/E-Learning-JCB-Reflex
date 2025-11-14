"""Estado de gestión de instructores."""

import reflex as rx
from E_Learning_JCB_Reflex.services.user_service import (
    get_all_instructors,
    get_user_by_id,
)
from E_Learning_JCB_Reflex.services.course_service import get_all_courses


class InstructorState(rx.State):
    """Estado de la aplicación para instructores."""

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
        """Cargar todos los instructores desde la base de datos."""
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
        """Cargar un instructor específico por ID."""
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
        instructor_id = self.router.page.params.get("instructor_id", "")
        if instructor_id:
            await self.load_instructor_by_id(instructor_id)
