"""
Estado para el dashboard de administradores.

Este módulo maneja el estado del dashboard administrativo, mostrando
estadísticas generales de la plataforma. Solo accesible para usuarios
con rol "admin".

Funcionalidades principales:
- Mostrar estadísticas de usuarios por rol
- Mostrar estadísticas de cursos
- Mostrar total de inscripciones activas
- Cargar todas las estadísticas de forma asíncrona
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.user_service import user_service
from E_Learning_JCB_Reflex.services.course_service import get_all_courses
from E_Learning_JCB_Reflex.services.enrollment_service import count_total_enrollments


class AdminDashboardState(AuthState):
    """
    Estado para el dashboard administrativo.

    Extiende AuthState para verificar permisos de administrador.
    Carga y muestra estadísticas generales de la plataforma.

    Atributos de estado:
        # Estadísticas de usuarios
        total_users (int): Total de usuarios en la plataforma
        total_students (int): Total de estudiantes
        total_instructors (int): Total de instructores
        total_admins (int): Total de administradores

        # Estadísticas de cursos
        total_courses (int): Total de cursos disponibles
        total_enrollments (int): Total de inscripciones activas

        # Estados de UI
        loading (bool): Indicador de carga de estadísticas

    Nota:
        Solo usuarios con rol "admin" pueden acceder a este estado.
        Se verifica is_authenticated y current_user.role == "admin".
    """

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
        """
        Cargar todas las estadísticas del dashboard administrativo.

        Realiza múltiples consultas a la base de datos para obtener:
        1. Conteo de usuarios por rol (estudiantes, instructores, admins)
        2. Total de cursos disponibles en la plataforma
        3. Total de inscripciones activas de estudiantes

        Actualiza el estado:
            - total_students, total_instructors, total_admins: Conteos por rol
            - total_users: Suma de todos los usuarios
            - total_courses: Número de cursos en la plataforma
            - total_enrollments: Número de inscripciones activas
            - loading: True durante carga, False al terminar

        Precondiciones:
            - Usuario debe estar autenticado (is_authenticated = True)
            - Usuario debe tener rol "admin"

        Nota:
            Si el usuario no está autenticado o no es admin, la función
            retorna inmediatamente sin cargar estadísticas.
        """
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
