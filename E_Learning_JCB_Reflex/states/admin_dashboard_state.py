"""Estado para el dashboard de administradores."""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.user_service import user_service
from E_Learning_JCB_Reflex.services.course_service import get_all_courses
from E_Learning_JCB_Reflex.services.enrollment_service import count_total_enrollments


class AdminDashboardState(AuthState):
    """Estado para el dashboard de administradores."""

    # Estadísticas de usuarios
    total_users: int = 0
    total_students: int = 0
    total_instructors: int = 0
    total_admins: int = 0

    # Estadísticas de cursos
    total_courses: int = 0
    total_enrollments: int = 0

    # Loading state
    loading: bool = False

    async def load_statistics(self):
        """Cargar todas las estadísticas del dashboard."""
        if not self.is_authenticated or self.current_user.get("role") != "admin":
            return

        self.loading = True

        try:
            # Cargar usuarios por rol
            students = await user_service.get_all_students()
            instructors = await user_service.get_all_instructors()
            admins = await user_service.get_all_admins()

            self.total_students = len(students)
            self.total_instructors = len(instructors)
            self.total_admins = len(admins)
            self.total_users = self.total_students + self.total_instructors + self.total_admins

            # Cargar cursos
            courses = await get_all_courses()
            self.total_courses = len(courses)

            # Cargar inscripciones
            self.total_enrollments = await count_total_enrollments()

        except Exception as e:
            print(f"Error loading admin statistics: {e}")
        finally:
            self.loading = False
