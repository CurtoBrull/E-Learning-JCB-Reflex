"""
Estado para gestión de cursos del instructor.

Permite al instructor crear, editar y eliminar sus propios cursos.
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.course_service import (
    get_all_courses,
    create_course,
    update_course,
    delete_course,
)
from E_Learning_JCB_Reflex.database.mongodb import MongoDB


class InstructorCourseState(AuthState):
    """Estado para que el instructor gestione sus cursos."""

    # Lista de cursos del instructor
    courses: list[dict] = []
    loading: bool = False
    error: str = ""
    success: str = ""

    # Control del modal de crear/editar
    show_form: bool = False
    editing_course_id: str = ""
    auto_open_form: bool = False  # Flag para abrir el formulario al montar la página

    # Campos del formulario
    form_title: str = ""
    form_description: str = ""
    form_price: str = "0"
    form_level: str = "beginner"
    form_category: str = ""
    form_thumbnail: str = ""

    # Control del modal de confirmación de borrado
    show_delete_confirm: bool = False
    deleting_course_id: str = ""
    deleting_course_title: str = ""

    @rx.var
    def is_editing(self) -> bool:
        return self.editing_course_id != ""

    # -------------------------------------------------------------------------
    # Carga de datos
    # -------------------------------------------------------------------------

    async def load_my_courses(self):
        """Cargar los cursos creados por el instructor autenticado."""
        # Si viene de go_to_create, abrir el formulario al montar la página
        # auto_open_form se mantiene True hasta que el formulario esté visible
        # para sobrevivir el doble on_mount de Reflex en desarrollo
        if self.auto_open_form and not self.show_form:
            self.open_create_form()
            self.auto_open_form = False
        elif self.auto_open_form and self.show_form:
            self.auto_open_form = False

        self.loading = True
        self.error = ""
        try:
            user_id = self.current_user.get("_id", "")
            if not user_id:
                self.error = "No hay usuario autenticado"
                return

            all_courses = await get_all_courses()
            self.courses = [
                {
                    "id": c.id,
                    "title": c.title,
                    "description": c.description,
                    "price": c.price,
                    "level": c.level,
                    "category": c.category,
                    "thumbnail": c.thumbnail,
                    "students_count": len(c.students),
                }
                for c in all_courses
                if c.instructor.user_id and str(c.instructor.user_id) == str(user_id)
            ]
        except Exception as e:
            self.error = f"Error al cargar cursos: {str(e)}"
            print(f"[InstructorCourseState] load_my_courses error: {e}")
        finally:
            self.loading = False

    # -------------------------------------------------------------------------
    # Formulario: abrir / cerrar / campos
    # -------------------------------------------------------------------------

    def open_create_form(self):
        """Abrir formulario para crear un curso nuevo."""
        self.editing_course_id = ""
        self.form_title = ""
        self.form_description = ""
        self.form_price = "0"
        self.form_level = "beginner"
        self.form_category = ""
        self.form_thumbnail = ""
        self.error = ""
        self.success = ""
        self.show_form = True

    def go_to_create(self):
        """Ir a la página de cursos y abrir el formulario de creación."""
        self.auto_open_form = True
        return rx.redirect("/instructor/courses")

    def open_edit_form(self, course: dict):
        """Abrir formulario pre-relleno para editar un curso."""
        self.editing_course_id = course["id"]
        self.form_title = course["title"]
        self.form_description = course["description"]
        self.form_price = str(course["price"])
        self.form_level = course["level"]
        self.form_category = course.get("category", "")
        self.form_thumbnail = course.get("thumbnail", "")
        self.error = ""
        self.success = ""
        self.show_form = True

    def close_form(self):
        self.show_form = False
        self.editing_course_id = ""
        self.error = ""
        self.success = ""

    def set_form_title(self, v: str):
        self.form_title = v

    def set_form_description(self, v: str):
        self.form_description = v

    def set_form_price(self, v: str):
        self.form_price = v

    def set_form_level(self, v: str):
        self.form_level = v

    def set_form_category(self, v: str):
        self.form_category = v

    def set_form_thumbnail(self, v: str):
        self.form_thumbnail = v

    # -------------------------------------------------------------------------
    # CRUD
    # -------------------------------------------------------------------------

    async def save_course(self):
        """Crear o actualizar un curso."""
        # Validaciones básicas
        if not self.form_title.strip():
            self.error = "El título es obligatorio"
            return
        if not self.form_description.strip():
            self.error = "La descripción es obligatoria"
            return

        self.loading = True
        self.error = ""
        self.success = ""
        try:
            user_id = self.current_user.get("_id", "")
            user_name = f"{self.current_user.get('firstName', '')} {self.current_user.get('lastName', '')}".strip()
            user_email = self.current_user.get("email", "")

            try:
                price = float(self.form_price)
            except ValueError:
                price = 0.0

            if self.editing_course_id:
                # Actualizar
                update_data = {
                    "title": self.form_title.strip(),
                    "description": self.form_description.strip(),
                    "price": price,
                    "level": self.form_level,
                    "category": self.form_category.strip(),
                    "image": self.form_thumbnail.strip() or "/images/courses/default.webp",
                }
                ok = await update_course(self.editing_course_id, update_data)
                if ok:
                    self.success = "Curso actualizado correctamente"
                else:
                    self.error = "No se pudo actualizar el curso"
            else:
                # Crear nuevo
                from bson import ObjectId
                course_data = {
                    "title": self.form_title.strip(),
                    "description": self.form_description.strip(),
                    "price": price,
                    "level": self.form_level,
                    "category": self.form_category.strip(),
                    "categories": [self.form_category.strip()] if self.form_category.strip() else [],
                    "image": self.form_thumbnail.strip() or "/images/courses/default.webp",
                    "instructor": {
                        "userId": ObjectId(user_id),
                        "name": user_name,
                        "email": user_email,
                        "avatarUrl": "",
                        "bio": "",
                    },
                    "students": [],
                    "lessons": [],
                    "studentsEnrolled": 0,
                }
                ok = await create_course(course_data)
                if ok:
                    # Actualizar coursesCreated del instructor en la BD
                    await self._add_course_to_instructor(user_id)
                    self.success = "Curso creado correctamente"
                else:
                    self.error = "No se pudo crear el curso"

            if self.success:
                self.show_form = False
                await self.load_my_courses()

        except Exception as e:
            self.error = f"Error: {str(e)}"
            print(f"[InstructorCourseState] save_course error: {e}")
        finally:
            self.loading = False

    async def _add_course_to_instructor(self, user_id: str):
        """Añadir el último curso creado al array coursesCreated del instructor."""
        try:
            from bson import ObjectId
            await MongoDB.connect()
            db = MongoDB.get_db()
            # Obtener el último curso insertado por este instructor
            courses_col = db["courses"]
            users_col = db["users"]
            last_course = await courses_col.find_one(
                {"instructor.userId": ObjectId(user_id)},
                sort=[("createdAt", -1)]
            )
            if last_course:
                await users_col.update_one(
                    {"_id": ObjectId(user_id)},
                    {"$addToSet": {"coursesCreated": last_course["_id"]}}
                )
        except Exception as e:
            print(f"[InstructorCourseState] _add_course_to_instructor error: {e}")

    # -------------------------------------------------------------------------
    # Borrado
    # -------------------------------------------------------------------------

    def confirm_delete(self, course: dict):
        """Mostrar diálogo de confirmación antes de borrar."""
        self.deleting_course_id = course["id"]
        self.deleting_course_title = course["title"]
        self.show_delete_confirm = True

    def cancel_delete(self):
        self.show_delete_confirm = False
        self.deleting_course_id = ""
        self.deleting_course_title = ""

    async def execute_delete(self):
        """Borrar el curso tras confirmación."""
        self.loading = True
        self.error = ""
        self.success = ""
        try:
            ok = await delete_course(self.deleting_course_id)
            if ok:
                # Eliminar también de coursesCreated del instructor
                await self._remove_course_from_instructor(
                    self.current_user.get("_id", ""),
                    self.deleting_course_id,
                )
                self.success = f'Curso "{self.deleting_course_title}" eliminado'
                self.show_delete_confirm = False
                self.deleting_course_id = ""
                self.deleting_course_title = ""
                await self.load_my_courses()
            else:
                self.error = "No se pudo eliminar el curso"
        except Exception as e:
            self.error = f"Error: {str(e)}"
            print(f"[InstructorCourseState] execute_delete error: {e}")
        finally:
            self.loading = False

    async def _remove_course_from_instructor(self, user_id: str, course_id: str):
        """Eliminar curso del array coursesCreated del instructor."""
        try:
            from bson import ObjectId
            await MongoDB.connect()
            db = MongoDB.get_db()
            await db["users"].update_one(
                {"_id": ObjectId(user_id)},
                {"$pull": {"coursesCreated": ObjectId(course_id)}}
            )
        except Exception as e:
            print(f"[InstructorCourseState] _remove_course_from_instructor error: {e}")
