"""Estado de gestión de inscripciones de estudiantes."""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services import enrollment_service
from E_Learning_JCB_Reflex.services.course_service import get_all_courses


class EnrollmentState(AuthState):
    """Estado de inscripciones de estudiantes."""

    # Cursos disponibles para inscripción
    available_courses: list[dict] = []

    # Cursos en los que el estudiante está inscrito
    enrolled_courses: list[dict] = []

    # Estados de la UI
    loading: bool = False
    error: str = ""
    success: str = ""

    # Dialog de confirmación para desinscripción
    show_unenroll_dialog: bool = False
    course_to_unenroll_id: str = ""
    course_to_unenroll_title: str = ""

    # Dialog de resultado de inscripción
    show_enrollment_result_dialog: bool = False
    enrollment_was_successful: bool = False
    enrollment_course_id: str = ""

    async def load_available_courses(self):
        """Cargar todos los cursos disponibles."""
        self.loading = True
        self.error = ""
        try:
            all_courses = await get_all_courses()

            # Convertir objetos Course a diccionarios
            self.available_courses = [
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

            if not self.available_courses:
                self.error = "No hay cursos disponibles"
        except Exception as e:
            self.error = f"Error al cargar cursos: {str(e)}"
            print(f"Error in load_available_courses: {e}")
        finally:
            self.loading = False

    async def load_enrolled_courses(self):
        """Cargar cursos en los que el estudiante está inscrito."""
        if not self.is_authenticated or not self.current_user:
            return

        self.loading = True
        self.error = ""
        try:
            user_id = self.current_user.get("_id")
            if not user_id:
                self.error = "Usuario no identificado"
                self.loading = False
                return

            enrolled = await enrollment_service.get_student_enrollments(user_id)
            self.enrolled_courses = enrolled

        except Exception as e:
            self.error = f"Error al cargar cursos inscritos: {str(e)}"
            print(f"Error in load_enrolled_courses: {e}")
        finally:
            self.loading = False

    async def enroll_in_course(self, course_id: str):
        """Inscribir al estudiante en un curso."""
        if not self.is_authenticated or not self.current_user:
            self.error = "Debes iniciar sesión para inscribirte"
            self.enrollment_was_successful = False
            self.show_enrollment_result_dialog = True
            return

        self.loading = True
        self.error = ""
        self.success = ""
        self.enrollment_course_id = course_id

        try:
            user_id = self.current_user.get("_id")
            if not user_id:
                self.error = "Usuario no identificado"
                self.loading = False
                self.enrollment_was_successful = False
                self.show_enrollment_result_dialog = True
                return

            result = await enrollment_service.enroll_student(user_id, course_id)

            if result:
                self.success = "¡Inscripción exitosa! Puedes ver el curso en tu dashboard."
                self.enrollment_was_successful = True
                # Recargar cursos inscritos para actualizar la vista
                await self.load_enrolled_courses()
            else:
                self.error = "No se pudo completar la inscripción. Es posible que ya estés inscrito en este curso."
                self.enrollment_was_successful = False

        except Exception as e:
            self.error = f"Error al inscribirse: {str(e)}"
            self.enrollment_was_successful = False
            print(f"Error in enroll_in_course: {e}")
        finally:
            self.loading = False
            self.show_enrollment_result_dialog = True

    async def enroll_in_current_course(self):
        """Inscribir al estudiante en el curso actual (usando el ID de la URL)."""
        from E_Learning_JCB_Reflex.utils.route_helpers import get_dynamic_id

        course_id = get_dynamic_id(self.router.url.path)
        if course_id:
            await self.enroll_in_course(course_id)

    def open_unenroll_dialog(self, course_id: str, course_title: str, *args, **kwargs):
        """Abrir el diálogo de confirmación para desinscripción."""
        self.course_to_unenroll_id = course_id
        self.course_to_unenroll_title = course_title
        self.show_unenroll_dialog = True

    def close_unenroll_dialog(self):
        """Cerrar el diálogo de confirmación para desinscripción."""
        self.show_unenroll_dialog = False
        self.course_to_unenroll_id = ""
        self.course_to_unenroll_title = ""

    def close_enrollment_result_dialog(self):
        """Cerrar el diálogo de resultado de inscripción."""
        self.show_enrollment_result_dialog = False
        self.error = ""
        self.success = ""

    async def confirm_unenroll(self):
        """Confirmar y ejecutar la desinscripción."""
        if not self.is_authenticated or not self.current_user:
            self.error = "Debes iniciar sesión"
            self.close_unenroll_dialog()
            return

        self.loading = True
        self.error = ""
        self.success = ""

        try:
            user_id = str(self.current_user.get("_id"))
            if not user_id:
                self.error = "Usuario no identificado"
                self.loading = False
                self.close_unenroll_dialog()
                return

            result = await enrollment_service.unenroll_student(user_id, str(self.course_to_unenroll_id))

            if result:
                self.success = "Desinscripción exitosa"
                # Recargar cursos inscritos para actualizar la vista
                await self.load_enrolled_courses()
            else:
                self.error = "No se pudo completar la desinscripción"

        except Exception as e:
            self.error = f"Error al desinscribirse: {str(e)}"
            print(f"Error in confirm_unenroll: {e}")
        finally:
            self.loading = False
            self.close_unenroll_dialog()

    async def check_enrollment_status(self, course_id: str) -> bool:
        """Verificar si el estudiante está inscrito en un curso específico."""
        if not self.is_authenticated or not self.current_user:
            return False

        try:
            user_id = self.current_user.get("_id")
            if not user_id:
                return False

            return await enrollment_service.is_enrolled(user_id, course_id)
        except Exception as e:
            print(f"Error checking enrollment status: {e}")
            return False

    @rx.var
    def total_enrolled_courses(self) -> int:
        """Número total de cursos en los que está inscrito."""
        return len(self.enrolled_courses)

    @rx.var
    def completed_courses(self) -> int:
        """Número de cursos completados (progreso 100%)."""
        return sum(1 for course in self.enrolled_courses if course.get("progress", 0) >= 100)

    @rx.var
    def average_progress(self) -> float:
        """Progreso promedio en todos los cursos inscritos."""
        if not self.enrolled_courses:
            return 0.0

        total_progress = sum(course.get("progress", 0) for course in self.enrolled_courses)
        return round(total_progress / len(self.enrolled_courses), 1)
