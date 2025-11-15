"""Estado de gestión de cursos."""

import reflex as rx
from E_Learning_JCB_Reflex.services.course_service import (
    get_popular_courses,
    get_all_courses,
    get_course_by_id,
)
from E_Learning_JCB_Reflex.services.user_service import get_users_by_ids


class CourseState(rx.State):
    """Estado de la aplicación para cursos."""

    courses: list[dict] = []
    loading: bool = False
    error: str = ""

    # Información básica del curso seleccionado
    course_title: str = ""
    course_description: str = ""
    course_thumbnail: str = ""
    course_price: float = 0.0
    course_level: str = ""
    course_category: str = ""

    # Información del instructor
    instructor_name: str = ""
    instructor_email: str = ""
    instructor_avatar: str = ""
    instructor_bio: str = ""

    # Estadísticas
    students_count: int = 0
    average_rating: int = 0
    total_reviews: int = 0

    # Listas
    categories: list[str] = []
    lessons: list[dict] = []
    reviews: list[dict] = []

    async def load_popular_courses(self):
        """Cargar cursos desde la base de datos."""
        self.loading = True
        self.error = ""
        try:
            some_courses = await get_popular_courses()
            # Convertir objetos Course a diccionarios para el estado de Reflex
            self.courses = [
                {
                    "id": course.id,
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
                    "id": course.id,
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

    async def load_course_by_id(self, course_id: str):
        """Cargar un curso específico por ID."""
        self.loading = True
        self.error = ""
        try:
            course = await get_course_by_id(course_id)
            if course:
                # Asignar a variables de estado planas
                self.course_title = course.title
                self.course_description = course.description
                self.course_thumbnail = course.thumbnail
                self.course_price = course.price
                self.course_level = course.level
                self.course_category = course.category

                # Información del instructor
                self.instructor_name = course.instructor.name
                self.instructor_email = course.instructor.email
                self.instructor_avatar = course.instructor.avatar_url
                self.instructor_bio = course.instructor.bio

                # Estadísticas
                self.students_count = len(course.students)
                self.average_rating = course.average_rating if course.average_rating else 0
                self.total_reviews = course.total_reviews if course.total_reviews else 0

                # Listas
                self.categories = course.categories
                self.lessons = [
                    {
                        "id": lesson.id,
                        "title": lesson.title,
                        "content": lesson.content,
                        "order": lesson.order,
                        "duration": lesson.duration,
                    }
                    for lesson in course.lessons
                ]

                # Obtener nombres de estudiantes para las reviews
                student_ids = [review.student for review in course.reviews if review.student]
                students_dict = await get_users_by_ids(student_ids) if student_ids else {}

                self.reviews = [
                    {
                        "id": review.id,
                        "student": students_dict[review.student].get_full_name() if review.student in students_dict else "Usuario Desconocido",
                        "rating": review.rating,
                        "comment": review.comment,
                        "created_at": str(review.created_at),
                    }
                    for review in course.reviews
                ]
            else:
                self.error = "Curso no encontrado"
                # Limpiar variables
                self.course_title = ""
        except Exception as e:
            self.error = f"Error loading course: {str(e)}"
            self.course_title = ""
            print(f"Error in load_course_by_id: {e}")
        finally:
            self.loading = False

    async def load_course_from_url(self):
        """Cargar curso usando el ID de la URL."""
        # Obtener el course_id desde los parámetros de la ruta
        course_id = self.router.url.params.get("course_id", "")
        if course_id:
            await self.load_course_by_id(course_id)

        print(f"Course id: {course_id}")
        print(f"Course title: {self.course_title}")
    