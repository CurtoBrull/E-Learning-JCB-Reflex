"""
Estado de gestión de cursos.

Este módulo maneja todo el estado relacionado con cursos en la aplicación,
incluyendo la carga de listas de cursos, detalles individuales de cursos,
y la visualización de información del instructor y reseñas.

Funcionalidades principales:
- Cargar cursos populares para mostrar en homepage
- Cargar catálogo completo de cursos
- Cargar detalles de un curso específico con lecciones y reseñas
- Extraer IDs de cursos desde URLs dinámicas
"""

import reflex as rx
from E_Learning_JCB_Reflex.services.course_service import (
    get_popular_courses,
    get_all_courses,
    get_course_by_id,
)
from E_Learning_JCB_Reflex.services.user_service import get_users_by_ids
from E_Learning_JCB_Reflex.utils.route_helpers import get_dynamic_id


class CourseState(rx.State):
    """
    Estado para gestión de cursos en Reflex.

    Maneja el estado de la aplicación relacionado con cursos, incluyendo
    listados, detalles individuales, información del instructor, lecciones
    y reseñas. Proporciona métodos para cargar datos desde la base de datos
    de forma asíncrona.

    Atributos de estado:
        courses (list[dict]): Lista de cursos (para catálogo y homepage)
        loading (bool): Indicador de carga en progreso
        error (str): Mensaje de error si la operación falla

        # Información del curso seleccionado
        course_title (str): Título del curso actual
        course_description (str): Descripción completa del curso
        course_thumbnail (str): URL de la imagen del curso
        course_price (float): Precio del curso
        course_level (str): Nivel del curso (beginner, intermediate, advanced)
        course_category (str): Categoría principal del curso

        # Información del instructor
        instructor_name (str): Nombre del instructor
        instructor_email (str): Email de contacto del instructor
        instructor_avatar (str): URL del avatar del instructor
        instructor_bio (str): Biografía del instructor

        # Estadísticas del curso
        students_count (int): Número de estudiantes inscritos
        average_rating (int): Calificación promedio (1-5)
        total_reviews (int): Número total de reseñas

        # Listas anidadas
        categories (list[str]): Categorías del curso
        lessons (list[dict]): Lecciones del curso con título, contenido, orden y duración
        reviews (list[dict]): Reseñas con estudiante, calificación y comentario
    """

    courses: list[dict] = []
    loading: bool = False
    error: str = ""

    # Información básica del curso seleccionado
    current_course_id: str = ""
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
        """
        Cargar cursos populares desde la base de datos.

        Carga un número limitado de cursos (por defecto 6) para mostrar en
        la página de inicio u otras secciones destacadas. Los cursos se
        convierten de objetos Course a diccionarios planos para ser compatibles
        con el sistema de estado de Reflex.

        Actualiza el estado:
            - courses: Lista de diccionarios con información básica de cada curso
            - loading: True durante la carga, False al terminar
            - error: Mensaje de error si la operación falla

        Nota:
            Si no se encuentran cursos, establece un mensaje de error apropiado.
        """
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
        """
        Cargar el catálogo completo de cursos desde la base de datos.

        A diferencia de load_popular_courses, esta función carga TODOS los
        cursos disponibles sin límite. Se utiliza para mostrar el catálogo
        completo en la página de cursos.

        Actualiza el estado:
            - courses: Lista completa de diccionarios con información de todos los cursos
            - loading: True durante la carga, False al terminar
            - error: Mensaje de error si la operación falla

        Nota:
            Para catálogos muy grandes, considerar implementar paginación.
        """
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
        """
        Cargar todos los detalles de un curso específico por ID.

        Carga información completa de un curso incluyendo:
        - Datos básicos del curso (título, descripción, precio, nivel, etc.)
        - Información completa del instructor (nombre, email, avatar, bio)
        - Estadísticas (estudiantes inscritos, calificación promedio, total de reseñas)
        - Lista de lecciones con contenido y duración
        - Reseñas de estudiantes con sus nombres

        Args:
            course_id: ID del curso en formato string (ObjectId de MongoDB)

        Actualiza el estado:
            - Variables del curso (course_title, course_description, etc.)
            - Variables del instructor (instructor_name, instructor_email, etc.)
            - Estadísticas (students_count, average_rating, total_reviews)
            - Listas (categories, lessons, reviews)
            - error: Mensaje si el curso no existe

        Nota:
            Las reseñas requieren una consulta adicional a la base de datos
            para obtener los nombres de los estudiantes que las escribieron.
        """
        self.loading = True
        self.error = ""
        try:
            course = await get_course_by_id(course_id)
            if course:
                # Asignar a variables de estado planas
                self.current_course_id = course_id
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
        """
        Cargar curso usando el ID extraído de la URL actual.

        Extrae el course_id de la ruta usando el path completo.
        Por ejemplo: /courses/507f1f77bcf86cd799439011 -> extrae el ID.

        Este método se ejecuta típicamente en el evento on_mount de la página
        de detalles del curso.
        """
        try:
            # Obtener el path actual y extraer el ID (último segmento antes de posibles subrutas)
            path = str(self.router.url.path)
            print(f"Loading course from path: {path}")

            # Extraer el course_id del path
            course_id = get_dynamic_id(path)

            print(f"Extracted course_id: {course_id}")

            # Cargar el curso
            await self.load_course_by_id(course_id)
        except Exception as e:
            print(f"Error in load_course_from_url: {e}")
            self.error = f"Error al cargar el curso: {str(e)}"
    