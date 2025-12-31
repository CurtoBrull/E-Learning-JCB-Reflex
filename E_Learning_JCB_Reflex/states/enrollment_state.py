"""
Estado de gestión de inscripciones de estudiantes.

Este módulo maneja toda la lógica de inscripción y desinscripción de estudiantes
en cursos. Proporciona funcionalidades para:
- Ver cursos disponibles para inscripción
- Inscribirse en un curso
- Desinscribirse de un curso
- Ver cursos en los que el estudiante ya está inscrito
- Calcular estadísticas de progreso

Hereda de AuthState para acceder a la información del usuario autenticado.
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services import enrollment_service
from E_Learning_JCB_Reflex.services.course_service import get_all_courses


class EnrollmentState(AuthState):
    """
    Estado para gestionar inscripciones de estudiantes en cursos.

    Extiende AuthState para tener acceso al usuario autenticado actual.
    Maneja el ciclo completo de inscripción: cargar cursos disponibles,
    inscribirse, desinscribirse, y visualizar progreso.

    Atributos de estado:
        # Listas de cursos
        available_courses (list[dict]): Todos los cursos disponibles para inscripción
        enrolled_courses (list[dict]): Cursos en los que el estudiante está inscrito

        # Estados de UI
        loading (bool): Indicador de operación en progreso
        error (str): Mensajes de error
        success (str): Mensajes de éxito

        # Diálogo de confirmación de desinscripción
        show_unenroll_dialog (bool): Mostrar/ocultar diálogo de confirmación
        course_to_unenroll_id (str): ID del curso a desinscribir
        course_to_unenroll_title (str): Título del curso a desinscribir

        # Diálogo de resultado de inscripción
        show_enrollment_result_dialog (bool): Mostrar/ocultar diálogo de resultado
        enrollment_was_successful (bool): Indica si la inscripción fue exitosa
        enrollment_course_id (str): ID del curso en el que se intentó inscribir

    Propiedades computadas:
        total_enrolled_courses (int): Número total de cursos inscritos
        completed_courses (int): Cursos con progreso 100%
        average_progress (float): Progreso promedio en todos los cursos
    """

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

    # Estado de inscripción en curso actual (para course_detail)
    is_enrolled_in_current_course: bool = False

    async def load_available_courses(self):
        """
        Cargar todos los cursos disponibles para inscripción.

        Obtiene el catálogo completo de cursos de la plataforma y los convierte
        a diccionarios para mostrarlos en la UI. Utilizado en páginas donde
        los estudiantes pueden explorar y seleccionar cursos para inscribirse.

        Actualiza el estado:
            - available_courses: Lista de diccionarios con info básica de cada curso
            - loading: True durante carga, False al terminar
            - error: Mensaje si no hay cursos o hay error
        """
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
        """
        Cargar cursos en los que el estudiante está inscrito.

        Obtiene de la base de datos todos los cursos en los que el usuario
        actual está inscrito, incluyendo información de progreso y estado
        de inscripción. Solo funciona si el usuario está autenticado.

        Actualiza el estado:
            - enrolled_courses: Lista con cursos inscritos y datos de progreso
            - loading: True durante carga, False al terminar
            - error: Mensaje si el usuario no está identificado o hay error

        Precondiciones:
            - El usuario debe estar autenticado (is_authenticated = True)
            - current_user debe contener el ID del usuario
        """
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
        """
        Inscribir al estudiante autenticado en un curso específico.

        Crea una nueva inscripción en la base de datos vinculando al estudiante
        con el curso. Inicializa el progreso en 0% y marca el estado como "active".
        También incrementa el contador de estudiantes inscritos del curso.

        Args:
            course_id: ID del curso en el que se desea inscribir

        Actualiza el estado:
            - success: Mensaje de éxito si la inscripción funciona
            - error: Mensaje si falla (usuario no autenticado, ya inscrito, etc.)
            - enrollment_was_successful: True si exitoso, False si falla
            - show_enrollment_result_dialog: True para mostrar resultado
            - enrolled_courses: Recarga la lista de cursos inscritos

        Nota:
            Si el estudiante ya está inscrito en el curso, la operación falla
            y se muestra un mensaje apropiado.
        """
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

        try:
            path = str(self.router.url.path)
            course_id = get_dynamic_id(path)
            print(f"Enrolling in course: {course_id}")

            await self.enroll_in_course(course_id)
            # Actualizar el estado de inscripción después de inscribirse
            await self.check_current_course_enrollment()
        except Exception as e:
            print(f"Error in enroll_in_current_course: {e}")
            self.error = f"Error al inscribirse: {str(e)}"

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

    async def check_current_course_enrollment(self):
        """
        Verificar si el usuario está inscrito en el curso actual.

        Lee el course_id de la URL y verifica si el usuario autenticado
        está inscrito en ese curso. Actualiza is_enrolled_in_current_course.
        """
        from E_Learning_JCB_Reflex.utils.route_helpers import get_dynamic_id

        # Solo para estudiantes autenticados
        if not self.is_authenticated or not self.is_user_student:
            self.is_enrolled_in_current_course = False
            return

        try:
            # Obtener el ID del curso desde la URL
            path = str(self.router.url.path)
            course_id = get_dynamic_id(path)

            print(f"Checking enrollment for course: {course_id}")

            # Verificar inscripción
            user_id = self.current_user.get("_id")
            if user_id and course_id:
                self.is_enrolled_in_current_course = await enrollment_service.is_enrolled(str(user_id), str(course_id))
                print(f"User {user_id} enrolled in course {course_id}: {self.is_enrolled_in_current_course}")
            else:
                self.is_enrolled_in_current_course = False

        except Exception as e:
            print(f"Error checking current course enrollment: {e}")
            self.is_enrolled_in_current_course = False

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
