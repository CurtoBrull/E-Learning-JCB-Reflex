"""Estado de gestión de cursos."""

import reflex as rx
from E_Learning_JCB_Reflex.services.course_service import get_popular_courses
from E_Learning_JCB_Reflex.services.course_service import get_all_courses


class CourseState(rx.State):
    """Estado de la aplicación para cursos."""

    courses: list[dict] = []
    loading: bool = False
    error: str = ""

    async def load_popular_courses(self):
        """Cargar cursos desde la base de datos."""
        self.loading = True
        self.error = ""
        try:
            some_courses = await get_popular_courses()
            # Convertir objetos Course a diccionarios para el estado de Reflex
            self.courses = [
                {
                    "title": course.title,
                    "description": course.description,
                    "instructor_name": course.instructor_name,
                    "price": course.price,
                    "level": course.level,
                    "thumbnail": course.thumbnail,
                }
                for course in some_courses
            ]
            if not self.courses:
                self.error = "No courses found in database"
        except Exception as e:
            self.error = f"Error loading courses: {str(e)}"
            print(f"Error in load_courses: {e}")
        finally:
            self.loading = False
            
    async def load_courses(self):
        """Cargar todos los cursos desde la base de datos."""
        self.loading = True
        self.error = ""
        try:
            all_courses = await get_all_courses()
            # Convertir objetos Course a diccionarios para el estado de Reflex
            self.courses = [
                {
                    "title": course.title,
                    "description": course.description,
                    "instructor_name": course.instructor_name,
                    "price": course.price,
                    "level": course.level,
                    "thumbnail": course.thumbnail,
                }
                for course in all_courses
            ]
            if not self.courses:
                self.error = "No courses found in database"
        except Exception as e:
            self.error = f"Error loading courses: {str(e)}"
            print(f"Error in load_courses: {e}")
        finally:
            self.loading = False
