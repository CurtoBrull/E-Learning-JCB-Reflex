"""
Estado para gestión de usuarios (solo administradores).

Este módulo proporciona toda la funcionalidad de administración de usuarios
del sistema. Solo accesible para usuarios con rol "admin".

Funcionalidades principales:
- Listar todos los usuarios del sistema (estudiantes, instructores, admins)
- Crear nuevos usuarios con cualquier rol
- Editar información de usuarios existentes
- Eliminar usuarios del sistema
- Buscar y filtrar usuarios por nombre, email o rol
- Cambiar contraseñas de usuarios como administrador
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.user_service import user_service


class UserManagementState(AuthState):
    """
    Estado para gestión completa de usuarios del sistema (CRUD).

    Extiende AuthState y proporciona funcionalidades de administración
    de usuarios. Solo debe ser accesible para usuarios con rol "admin".

    Atributos de estado:
        # Listas de usuarios
        users (list[dict]): Todos los usuarios del sistema
        filtered_users (list[dict]): Usuarios filtrados por búsqueda/rol

        # Filtros y búsqueda
        search_query (str): Texto de búsqueda (nombre o email)
        role_filter (str): Filtro por rol ("all", "student", "instructor", "admin")

        # Formulario de usuario
        show_user_dialog (bool): Mostrar/ocultar diálogo de edición
        edit_mode (bool): True = editar existente, False = crear nuevo
        selected_user_id (str): ID del usuario seleccionado para edición

        # Campos del formulario
        form_first_name (str): Nombre en el formulario
        form_last_name (str): Apellido en el formulario
        form_email (str): Email en el formulario
        form_password (str): Contraseña en el formulario (opcional en modo edición)
        form_role (str): Rol en el formulario ("student", "instructor", "admin")

        # Diálogo de confirmación de eliminación
        show_delete_dialog (bool): Mostrar/ocultar diálogo de confirmación
        user_to_delete_id (str): ID del usuario a eliminar
        user_to_delete_name (str): Nombre del usuario a eliminar (para mostrar)

        # UI states
        loading (bool): Indicador de operación en progreso
    """

    # Lista de usuarios
    users: list[dict] = []
    filtered_users: list[dict] = []

    # Filtros y búsqueda
    search_query: str = ""
    role_filter: str = "all"

    # Formulario de usuario
    show_user_dialog: bool = False
    edit_mode: bool = False
    selected_user_id: str = ""

    # Campos del formulario
    form_first_name: str = ""
    form_last_name: str = ""
    form_email: str = ""
    form_password: str = ""
    form_role: str = "student"

    # Diálogo de confirmación de eliminación
    show_delete_dialog: bool = False
    user_to_delete_id: str = ""
    user_to_delete_name: str = ""

    # UI states
    loading: bool = False

    def set_search_query(self, value: str):
        """Setter para search_query."""
        self.search_query = value
        self.apply_filters()

    def set_role_filter(self, value: str):
        """Setter para role_filter."""
        self.role_filter = value
        self.apply_filters()

    def set_form_first_name(self, value: str):
        """Setter para form_first_name."""
        self.form_first_name = value

    def set_form_last_name(self, value: str):
        """Setter para form_last_name."""
        self.form_last_name = value

    def set_form_email(self, value: str):
        """Setter para form_email."""
        self.form_email = value

    def set_form_password(self, value: str):
        """Setter para form_password."""
        self.form_password = value

    def set_form_role(self, value: str):
        """Setter para form_role."""
        self.form_role = value

    def apply_filters(self):
        """Aplicar filtros de búsqueda y rol."""
        filtered = self.users

        # Filtrar por rol
        if self.role_filter != "all":
            filtered = [u for u in filtered if u.get("role") == self.role_filter]

        # Filtrar por búsqueda (nombre o email)
        if self.search_query:
            query = self.search_query.lower()
            filtered = [
                u for u in filtered
                if query in u.get("firstName", "").lower()
                or query in u.get("lastName", "").lower()
                or query in u.get("email", "").lower()
            ]

        self.filtered_users = filtered

    async def load_users(self):
        """Cargar todos los usuarios del sistema."""
        if not self.is_authenticated or self.current_user.get("role") != "admin":
            return rx.toast.error("No tienes permisos para acceder a esta página")

        self.loading = True
        try:
            # Obtener todos los usuarios
            students = await user_service.get_all_students()
            instructors = await user_service.get_all_instructors()

            # Convertir a diccionarios
            all_users = []
            for student in students:
                all_users.append({
                    "_id": student.id,
                    "firstName": student.first_name,
                    "lastName": student.last_name,
                    "email": student.email,
                    "role": student.role,
                    "createdAt": str(student.created_at)[:10] if student.created_at else "",
                })

            for instructor in instructors:
                all_users.append({
                    "_id": instructor.id,
                    "firstName": instructor.first_name,
                    "lastName": instructor.last_name,
                    "email": instructor.email,
                    "role": instructor.role,
                    "createdAt": str(instructor.created_at)[:10] if instructor.created_at else "",
                })

            # Obtener admins también
            admins = await user_service.get_all_admins()
            for admin in admins:
                all_users.append({
                    "_id": admin.id,
                    "firstName": admin.first_name,
                    "lastName": admin.last_name,
                    "email": admin.email,
                    "role": admin.role,
                    "createdAt": str(admin.created_at)[:10] if admin.created_at else "",
                })

            self.users = all_users
            self.apply_filters()

        except Exception as e:
            print(f"Error loading users: {e}")
            return rx.toast.error(f"Error al cargar usuarios: {str(e)}")
        finally:
            self.loading = False

    def open_create_user_dialog(self):
        """Abrir diálogo para crear nuevo usuario."""
        self.edit_mode = False
        self.selected_user_id = ""
        self.form_first_name = ""
        self.form_last_name = ""
        self.form_email = ""
        self.form_password = ""
        self.form_role = "student"
        self.show_user_dialog = True

    def open_edit_user_dialog(self, user_id: str, first_name: str, last_name: str, email: str, role: str):
        """Abrir diálogo para editar usuario existente."""
        self.edit_mode = True
        self.selected_user_id = user_id
        self.form_first_name = first_name
        self.form_last_name = last_name
        self.form_email = email
        self.form_password = ""
        self.form_role = role
        self.show_user_dialog = True

    def close_user_dialog(self):
        """Cerrar diálogo de usuario."""
        self.show_user_dialog = False

    def open_delete_dialog(self, user_id: str, user_name: str):
        """Abrir diálogo de confirmación de eliminación."""
        self.user_to_delete_id = user_id
        self.user_to_delete_name = user_name
        self.show_delete_dialog = True

    def close_delete_dialog(self):
        """Cerrar diálogo de eliminación."""
        self.show_delete_dialog = False

    async def save_user(self):
        """Guardar usuario (crear o actualizar)."""
        if not self.is_authenticated or self.current_user.get("role") != "admin":
            return rx.toast.error("No tienes permisos")

        # Validaciones
        if not self.form_first_name or not self.form_last_name:
            return rx.toast.error("Nombre y apellido son obligatorios")

        if not self.form_email or "@" not in self.form_email:
            return rx.toast.error("Email inválido")

        if not self.edit_mode and not self.form_password:
            return rx.toast.error("La contraseña es obligatoria para nuevos usuarios")

        if self.form_password and len(self.form_password) < 6:
            return rx.toast.error("La contraseña debe tener al menos 6 caracteres")

        self.loading = True

        try:
            if self.edit_mode:
                # Actualizar usuario existente
                update_data = {
                    "firstName": self.form_first_name,
                    "lastName": self.form_last_name,
                    "email": self.form_email,
                    "role": self.form_role,
                }

                result = await user_service.update_user(self.selected_user_id, update_data)

                # Si se proporcionó una nueva contraseña, actualizarla
                if self.form_password:
                    await user_service.admin_change_password(self.selected_user_id, self.form_password)

                if result:
                    self.close_user_dialog()
                    await self.load_users()
                    return rx.toast.success("Usuario actualizado exitosamente")
                else:
                    return rx.toast.error("No se pudo actualizar el usuario")
            else:
                # Crear nuevo usuario
                result = await user_service.create_user(
                    self.form_first_name,
                    self.form_last_name,
                    self.form_email,
                    self.form_password,
                    self.form_role
                )

                if result:
                    self.close_user_dialog()
                    await self.load_users()
                    return rx.toast.success("Usuario creado exitosamente")
                else:
                    return rx.toast.error("No se pudo crear el usuario")

        except Exception as e:
            print(f"Error saving user: {e}")
            return rx.toast.error(f"Error al guardar usuario: {str(e)}")
        finally:
            self.loading = False

    async def confirm_delete_user(self):
        """Confirmar y ejecutar eliminación de usuario."""
        if not self.is_authenticated or self.current_user.get("role") != "admin":
            return rx.toast.error("No tienes permisos")

        # No permitir eliminar el propio usuario
        if self.user_to_delete_id == str(self.current_user.get("_id")):
            self.close_delete_dialog()
            return rx.toast.error("No puedes eliminar tu propia cuenta")

        self.loading = True

        try:
            result = await user_service.delete_user(self.user_to_delete_id)

            if result:
                self.close_delete_dialog()
                await self.load_users()
                return rx.toast.success("Usuario eliminado exitosamente")
            else:
                return rx.toast.error("No se pudo eliminar el usuario")

        except Exception as e:
            print(f"Error deleting user: {e}")
            return rx.toast.error(f"Error al eliminar usuario: {str(e)}")
        finally:
            self.loading = False
