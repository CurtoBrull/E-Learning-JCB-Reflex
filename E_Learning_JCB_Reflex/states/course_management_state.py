"""Estado para la gestión de cursos (admin)."""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.course_service import (
    get_all_courses,
    create_course,
    update_course,
    delete_course,
)


class CourseManagementState(AuthState):
    """Estado para gestionar cursos desde el panel de administrador."""

    # Lista de cursos
    courses: list[dict] = []
    filtered_courses: list[dict] = []

    # Búsqueda y filtros
    search_query: str = ""
    level_filter: str = "all"

    # Diálogo de crear/editar curso
    show_course_dialog: bool = False
    dialog_mode: str = "create"  # "create" o "edit"
    selected_course_id: str = ""
    course_title: str = ""
    course_description: str = ""
    course_price: str = ""
    course_level: str = "beginner"
    course_category: str = ""
    course_image: str = ""
    course_instructor_name: str = ""
    course_instructor_email: str = ""

    # Diálogo de eliminar
    show_delete_dialog: bool = False
    course_to_delete_id: str = ""
    course_to_delete_title: str = ""

    # Estado
    loading: bool = False

    def set_search_query(self, value: str):
        """Setter para search_query."""
        self.search_query = value

    def set_level_filter(self, value: str):
        """Setter para level_filter."""
        self.level_filter = value

    def set_course_title(self, value: str):
        """Setter para course_title."""
        self.course_title = value

    def set_course_description(self, value: str):
        """Setter para course_description."""
        self.course_description = value

    def set_course_price(self, value: str):
        """Setter para course_price."""
        self.course_price = value

    def set_course_level(self, value: str):
        """Setter para course_level."""
        self.course_level = value

    def set_course_category(self, value: str):
        """Setter para course_category."""
        self.course_category = value

    def set_course_image(self, value: str):
        """Setter para course_image."""
        self.course_image = value

    def set_course_instructor_name(self, value: str):
        """Setter para course_instructor_name."""
        self.course_instructor_name = value

    def set_course_instructor_email(self, value: str):
        """Setter para course_instructor_email."""
        self.course_instructor_email = value

    async def load_courses(self):
        """Cargar todos los cursos del sistema."""
        if not self.is_authenticated or self.current_user.get("role") != "admin":
            return rx.toast.error("No tienes permisos para acceder a esta página")

        self.loading = True
        try:
            courses = await get_all_courses()

            all_courses = []
            for course in courses:
                all_courses.append({
                    "_id": course.id,
                    "title": course.title,
                    "description": course.description,
                    "price": course.price,
                    "level": course.level,
                    "category": course.category,
                    "image": course.thumbnail,
                    "instructorName": course.instructor.name,
                    "instructorEmail": course.instructor.email,
                    "studentsEnrolled": len(course.students) if course.students else 0,
                })

            self.courses = all_courses
            self.apply_filters()
        except Exception as e:
            print(f"Error loading courses: {e}")
            return rx.toast.error(f"Error al cargar cursos: {str(e)}")
        finally:
            self.loading = False

    def apply_filters(self):
        """Aplicar filtros de búsqueda y nivel."""
        filtered = self.courses

        # Filtro de búsqueda
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                c for c in filtered
                if query in c["title"].lower()
                or query in c["description"].lower()
                or query in c["category"].lower()
            ]

        # Filtro de nivel
        if self.level_filter != "all":
            filtered = [c for c in filtered if c["level"] == self.level_filter]

        self.filtered_courses = filtered

    def on_search_change(self, value: str):
        """Manejar cambio en búsqueda."""
        self.search_query = value
        self.apply_filters()

    def on_level_filter_change(self, value: str):
        """Manejar cambio en filtro de nivel."""
        self.level_filter = value
        self.apply_filters()

    def open_create_course_dialog(self):
        """Abrir diálogo para crear curso."""
        self.dialog_mode = "create"
        self.selected_course_id = ""
        self.course_title = ""
        self.course_description = ""
        self.course_price = "0"
        self.course_level = "beginner"
        self.course_category = ""
        self.course_image = "/placeholder-course.jpg"
        self.course_instructor_name = ""
        self.course_instructor_email = ""
        self.show_course_dialog = True

    def open_edit_course_dialog(
        self,
        course_id: str,
        title: str,
        description: str,
        price: float,
        level: str,
        category: str,
        image: str,
        instructor_name: str,
        instructor_email: str,
        *args,
        **kwargs
    ):
        """Abrir diálogo para editar curso."""
        self.dialog_mode = "edit"
        self.selected_course_id = course_id
        self.course_title = title
        self.course_description = description
        self.course_price = str(price)
        self.course_level = level
        self.course_category = category
        self.course_image = image
        self.course_instructor_name = instructor_name
        self.course_instructor_email = instructor_email
        self.show_course_dialog = True

    def close_course_dialog(self):
        """Cerrar diálogo de curso."""
        self.show_course_dialog = False

    async def save_course(self):
        """Guardar curso (crear o editar)."""
        # Validaciones
        if not self.course_title or not self.course_description:
            return rx.toast.error("Título y descripción son obligatorios")

        if not self.course_instructor_name or not self.course_instructor_email:
            return rx.toast.error("Datos del instructor son obligatorios")

        try:
            price = float(self.course_price) if self.course_price else 0.0
            if price < 0:
                return rx.toast.error("El precio no puede ser negativo")
        except ValueError:
            return rx.toast.error("Precio inválido")

        self.loading = True

        try:
            course_data = {
                "title": self.course_title,
                "description": self.course_description,
                "price": price,
                "level": self.course_level,
                "category": self.course_category,
                "image": self.course_image,
                "instructor": {
                    "name": self.course_instructor_name,
                    "email": self.course_instructor_email,
                }
            }

            if self.dialog_mode == "create":
                success = await create_course(course_data)
                message = "Curso creado exitosamente" if success else "Error al crear curso"
            else:
                success = await update_course(self.selected_course_id, course_data)
                message = "Curso actualizado exitosamente" if success else "Error al actualizar curso"

            if success:
                await self.load_courses()
                self.close_course_dialog()
                return rx.toast.success(message)
            else:
                return rx.toast.error(message)

        except Exception as e:
            print(f"Error saving course: {e}")
            return rx.toast.error(f"Error al guardar curso: {str(e)}")
        finally:
            self.loading = False

    def open_delete_dialog(self, course_id: str, course_title: str, *args, **kwargs):
        """Abrir diálogo de confirmación para eliminar curso."""
        self.course_to_delete_id = course_id
        self.course_to_delete_title = course_title
        self.show_delete_dialog = True

    def close_delete_dialog(self):
        """Cerrar diálogo de eliminación."""
        self.show_delete_dialog = False

    async def confirm_delete_course(self):
        """Confirmar eliminación de curso."""
        self.loading = True

        try:
            success = await delete_course(self.course_to_delete_id)

            if success:
                await self.load_courses()
                self.close_delete_dialog()
                return rx.toast.success("Curso eliminado exitosamente")
            else:
                return rx.toast.error("Error al eliminar curso")

        except Exception as e:
            print(f"Error deleting course: {e}")
            return rx.toast.error(f"Error al eliminar curso: {str(e)}")
        finally:
            self.loading = False
