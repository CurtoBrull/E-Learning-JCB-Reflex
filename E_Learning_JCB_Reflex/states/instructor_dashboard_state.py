"""
Estado del dashboard de instructor.

Este módulo maneja el estado del dashboard del instructor, incluyendo
la carga de estadísticas y cursos del instructor autenticado.
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.user_service import get_user_by_id
from E_Learning_JCB_Reflex.services.course_service import get_all_courses


class InstructorDashboardState(AuthState):
    """
    Estado para el dashboard del instructor.

    Maneja la carga de estadísticas y cursos del instructor autenticado.

    Atributos:
        total_courses (int): Total de cursos creados por el instructor
        total_students (int): Total de estudiantes únicos en los cursos del instructor
        average_rating (float): Valoración promedio de los cursos
        total_revenue (float): Ingresos totales generados
        courses (list[dict]): Lista de cursos del instructor
        loading (bool): Indicador de carga
        error (str): Mensaje de error
    """

    total_courses: int = 0
    total_students: int = 0
    average_rating: float = 0.0
    total_revenue: float = 0.0
    courses: list[dict] = []
    loading: bool = False
    error: str = ""

    async def load_dashboard_data(self):
        """
        Cargar datos del dashboard del instructor autenticado.

        Carga estadísticas y cursos del instructor que ha iniciado sesión.
        """
        self.loading = True
        self.error = ""

        try:
            print(f"\n🔍 [InstructorDashboardState] Cargando dashboard...")
            print(f"   current_user: {self.current_user}")

            # Obtener el instructor actual
            if not self.current_user or not self.current_user.get("_id"):
                self.error = "No hay usuario autenticado"
                print(f"   ❌ No hay usuario autenticado")
                return

            user_id = self.current_user.get("_id")
            print(f"   user_id: {user_id}")

            instructor = await get_user_by_id(user_id)
            print(f"   Instructor: {instructor.get_full_name() if instructor else 'None'}")
            print(f"   courses_created: {instructor.courses_created if instructor else 'None'}")

            if not instructor or not instructor.is_instructor:
                self.error = "Usuario no es instructor"
                print(f"   ❌ Usuario no es instructor")
                return

            # Obtener todos los cursos
            all_courses = await get_all_courses()
            print(f"   Total cursos en BD: {len(all_courses)}")

            # Filtrar cursos del instructor
            instructor_courses = [
                course for course in all_courses
                if course.id in instructor.courses_created
            ]
            print(f"   Cursos del instructor: {len(instructor_courses)}")

            # Calcular estadísticas
            self.total_courses = len(instructor_courses)
            print(f"   ✅ total_courses actualizado: {self.total_courses}")

            # Calcular estudiantes únicos
            unique_students = set()
            total_ratings = []
            total_revenue = 0.0

            for course in instructor_courses:
                # Estudiantes únicos
                unique_students.update(course.students)

                # Ratings
                if course.average_rating:
                    total_ratings.append(course.average_rating)

                # Ingresos (precio * número de estudiantes)
                total_revenue += course.price * len(course.students)

            self.total_students = len(unique_students)
            self.average_rating = (
                sum(total_ratings) / len(total_ratings)
                if total_ratings
                else 0.0
            )
            self.total_revenue = total_revenue

            # Convertir cursos a diccionarios para el estado
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

        except Exception as e:
            self.error = f"Error cargando dashboard: {str(e)}"
            print(f"Error in load_dashboard_data: {e}")
        finally:
            self.loading = False

    def on_mount(self):
        """Cargar datos cuando se monta el componente."""
        return self.load_dashboard_data()
