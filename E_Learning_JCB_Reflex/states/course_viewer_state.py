"""
Estado para visualizar y reproducir el contenido de un curso.

Este módulo gestiona la funcionalidad del visor de cursos, permitiendo a los
estudiantes inscritos ver las lecciones del curso con videos de YouTube embebidos.

Funcionalidades:
- Cargar información del curso desde la URL
- Gestionar la lección actualmente seleccionada
- Navegar entre lecciones (anterior/siguiente)
- Reproducir videos de YouTube
- Validar que el usuario esté inscrito en el curso

Hereda de AuthState para acceder a la información del usuario autenticado.
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.course_service import get_course_by_id
from E_Learning_JCB_Reflex.services.enrollment_service import is_enrolled
from E_Learning_JCB_Reflex.utils.route_helpers import get_dynamic_id


class CourseViewerState(AuthState):
    """
    Estado para el visor de cursos.

    Gestiona la visualización del contenido del curso, incluyendo la navegación
    entre lecciones y la reproducción de videos de YouTube.

    Atributos de estado:
        # Información del curso
        course_id (str): ID del curso actual
        course_title (str): Título del curso
        course_thumbnail (str): URL de la imagen del curso

        # Lecciones
        lessons (list[dict]): Lista de todas las lecciones del curso
        current_lesson_index (int): Índice de la lección actual

        # Estados de UI
        loading (bool): Indicador de carga
        error (str): Mensajes de error
        is_enrolled (bool): Si el usuario está inscrito en el curso

    Propiedades computadas:
        current_lesson (dict): Lección actualmente seleccionada
        current_video_url (str): URL del video de YouTube para embed
        has_previous_lesson (bool): Si existe una lección anterior
        has_next_lesson (bool): Si existe una lección siguiente
        progress_percentage (float): Porcentaje de progreso en el curso
    """

    # Información del curso
    current_course_id: str = ""
    course_title: str = ""
    course_thumbnail: str = ""

    # Lecciones
    lessons: list[dict] = []
    current_lesson_index: int = 0

    # Estados de UI
    loading: bool = False
    error: str = ""
    is_enrolled: bool = False
    sidebar_visible: bool = True  # Controlar visibilidad de la sidebar

    @rx.var
    def current_lesson(self) -> dict:
        """
        Obtener la lección actualmente seleccionada.

        Returns:
            dict: Diccionario con los datos de la lección actual
        """
        if 0 <= self.current_lesson_index < len(self.lessons):
            return self.lessons[self.current_lesson_index]
        return {}

    @rx.var
    def current_video_url(self) -> str:
        """
        Obtener la URL del video de YouTube para embed.

        Convierte URLs de YouTube en formato embed para poder mostrarlas en iframe.
        Soporta formatos:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID

        Returns:
            str: URL en formato embed de YouTube
        """
        lesson = self.current_lesson
        if not lesson:
            return ""

        video_url = lesson.get("video_url", "")
        if not video_url:
            return ""

        # Convertir URL de YouTube a formato embed
        if "youtube.com/watch?v=" in video_url:
            video_id = video_url.split("watch?v=")[1].split("&")[0]
            return f"https://www.youtube.com/embed/{video_id}"
        elif "youtu.be/" in video_url:
            video_id = video_url.split("youtu.be/")[1].split("?")[0]
            return f"https://www.youtube.com/embed/{video_id}"

        # Si ya está en formato embed, devolverla tal cual
        return video_url

    @rx.var
    def has_previous_lesson(self) -> bool:
        """Verificar si existe una lección anterior."""
        return self.current_lesson_index > 0

    @rx.var
    def has_next_lesson(self) -> bool:
        """Verificar si existe una lección siguiente."""
        return self.current_lesson_index < len(self.lessons) - 1

    @rx.var
    def progress_percentage(self) -> float:
        """
        Calcular el porcentaje de progreso en el curso.

        Returns:
            float: Porcentaje de lecciones vistas (0-100)
        """
        if len(self.lessons) == 0:
            return 0.0
        return ((self.current_lesson_index + 1) / len(self.lessons)) * 100

    @rx.var
    def total_lessons(self) -> int:
        """Obtener el número total de lecciones."""
        return len(self.lessons)

    async def load_course_viewer_from_url(self):
        """
        Cargar el curso desde la URL y verificar inscripción.

        Lee el course_id de la URL, carga la información del curso,
        y verifica que el usuario esté inscrito antes de mostrar el contenido.

        Si el usuario no está inscrito o hay algún error, muestra un mensaje
        apropiado y no permite acceder al contenido.
        """
        self.loading = True
        self.error = ""

        try:
            # Obtener el ID del curso desde la URL
            # Para /courses/[course_id]/view, el course_id está en el penúltimo segmento
            path = str(self.router.url.path)
            course_id = get_dynamic_id(path, index=-2)

            print(f"Loading course viewer from path: {path}, ID: {course_id}")

            self.current_course_id = course_id

            # Verificar que el usuario esté autenticado
            if not self.is_authenticated:
                print("[VIEWER] User not authenticated")
                self.error = "Debes iniciar sesión para ver este contenido"
                self.loading = False
                return

            print(f"[VIEWER] User authenticated: {self.current_user.get('_id')}")

            # Verificar que el usuario sea estudiante
            if not self.is_user_student:
                print("[VIEWER] User is not a student")
                self.error = "Solo los estudiantes pueden ver el contenido de los cursos"
                self.loading = False
                return

            print("[VIEWER] User is a student")

            # Verificar que el estudiante esté inscrito en el curso
            user_id = self.current_user.get("_id", "")
            self.is_enrolled = await is_enrolled(str(user_id), str(course_id))

            print(f"[VIEWER] Enrollment status: {self.is_enrolled}")

            if not self.is_enrolled:
                print("[VIEWER] User not enrolled")
                self.error = "No estás inscrito en este curso. Inscríbete primero para acceder al contenido."
                self.loading = False
                return

            print("[VIEWER] Loading course data...")
            # Cargar información del curso
            course = await get_course_by_id(course_id)

            if not course:
                print("[VIEWER] Course not found in database")
                self.error = "Curso no encontrado"
                self.loading = False
                return

            print(f"[VIEWER] Course loaded: {course.title}")

            # Guardar información del curso
            self.course_title = course.title
            self.course_thumbnail = course.thumbnail or "/default-course.png"

            # Cargar lecciones
            self.lessons = [lesson.to_dict() for lesson in course.lessons]

            print(f"[VIEWER] Found {len(self.lessons)} lessons")

            # Verificar que haya lecciones
            if len(self.lessons) == 0:
                print("[VIEWER] No lessons available")
                self.error = "Este curso aún no tiene lecciones disponibles"
                self.loading = False
                return

            # Ordenar lecciones por order
            self.lessons.sort(key=lambda x: x.get("order", 0))

            print(f"[VIEWER] First lesson video_url: {self.lessons[0].get('video_url', 'NO URL')}")

            # Iniciar en la primera lección
            self.current_lesson_index = 0

            print(f"[VIEWER] Successfully loaded! Course viewer ready.")
            print(f"[VIEWER] is_enrolled: {self.is_enrolled}, loading: {self.loading}, error: {self.error}")

        except Exception as e:
            print(f"[VIEWER] Exception occurred: {str(e)}")
            self.error = f"Error al cargar el curso: {str(e)}"
        finally:
            self.loading = False
            print(f"[VIEWER] Final state - is_enrolled: {self.is_enrolled}, loading: {self.loading}, error: '{self.error}'")

    def select_lesson(self, index: int):
        """
        Seleccionar una lección específica por su índice.

        Args:
            index: Índice de la lección a seleccionar (0-based)
        """
        if 0 <= index < len(self.lessons):
            self.current_lesson_index = index

    def go_to_previous_lesson(self):
        """Ir a la lección anterior si existe."""
        if self.has_previous_lesson:
            self.current_lesson_index -= 1

    def go_to_next_lesson(self):
        """Ir a la lección siguiente si existe."""
        if self.has_next_lesson:
            self.current_lesson_index += 1

    def toggle_sidebar(self):
        """Alternar visibilidad de la sidebar."""
        self.sidebar_visible = not self.sidebar_visible
