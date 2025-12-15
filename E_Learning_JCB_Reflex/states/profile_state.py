"""Estado para gestión de perfil de usuario."""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.services.user_service import user_service


class ProfileState(AuthState):
    """Estado para gestionar el perfil del usuario."""

    # Campos editables
    first_name: str = ""
    last_name: str = ""
    email: str = ""

    # Cambio de contraseña
    current_password: str = ""
    new_password: str = ""
    confirm_password: str = ""

    # UI states
    loading: bool = False
    show_password_section: bool = False

    def set_first_name(self, value: str):
        """Setter para first_name."""
        self.first_name = value

    def set_last_name(self, value: str):
        """Setter para last_name."""
        self.last_name = value

    def set_email(self, value: str):
        """Setter para email."""
        self.email = value

    def set_current_password(self, value: str):
        """Setter para current_password."""
        self.current_password = value

    def set_new_password(self, value: str):
        """Setter para new_password."""
        self.new_password = value

    def set_confirm_password(self, value: str):
        """Setter para confirm_password."""
        self.confirm_password = value

    def load_profile_data(self):
        """Cargar datos del perfil del usuario actual."""
        if self.current_user:
            self.first_name = self.current_user.get("firstName", "")
            self.last_name = self.current_user.get("lastName", "")
            self.email = self.current_user.get("email", "")

    def toggle_password_section(self):
        """Mostrar/ocultar sección de cambio de contraseña."""
        self.show_password_section = not self.show_password_section
        if not self.show_password_section:
            # Limpiar campos al cerrar
            self.current_password = ""
            self.new_password = ""
            self.confirm_password = ""

    async def update_profile(self):
        """Actualizar información del perfil."""
        if not self.is_authenticated:
            return rx.toast.error("Debes iniciar sesión")

        # Validaciones
        if not self.first_name or not self.last_name:
            return rx.toast.error("El nombre y apellido son obligatorios")

        if not self.email or "@" not in self.email:
            return rx.toast.error("Email inválido")

        self.loading = True

        try:
            user_id = str(self.current_user.get("_id"))

            # Preparar datos a actualizar
            update_data = {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email,
            }

            # Actualizar en la base de datos
            result = await user_service.update_user(user_id, update_data)

            if result:
                # Actualizar current_user en memoria
                self.current_user["firstName"] = self.first_name
                self.current_user["lastName"] = self.last_name
                self.current_user["email"] = self.email
                return rx.toast.success("Perfil actualizado exitosamente")
            else:
                return rx.toast.error("No se pudo actualizar el perfil")

        except Exception as e:
            print(f"Error in update_profile: {e}")
            return rx.toast.error(f"Error al actualizar perfil: {str(e)}")
        finally:
            self.loading = False

    async def change_password(self):
        """Cambiar la contraseña del usuario."""
        if not self.is_authenticated:
            return rx.toast.error("Debes iniciar sesión")

        # Validaciones
        if not self.current_password:
            return rx.toast.error("Ingresa tu contraseña actual")

        if not self.new_password:
            return rx.toast.error("Ingresa una nueva contraseña")

        if len(self.new_password) < 6:
            return rx.toast.error("La contraseña debe tener al menos 6 caracteres")

        if self.new_password != self.confirm_password:
            return rx.toast.error("Las contraseñas no coinciden")

        self.loading = True

        try:
            user_id = str(self.current_user.get("_id"))

            # Cambiar contraseña
            result = await user_service.change_password(
                user_id,
                self.current_password,
                self.new_password
            )

            if result:
                # Limpiar campos
                self.current_password = ""
                self.new_password = ""
                self.confirm_password = ""
                self.show_password_section = False
                return rx.toast.success("Contraseña cambiada exitosamente")
            else:
                return rx.toast.error("Contraseña actual incorrecta")

        except Exception as e:
            print(f"Error in change_password: {e}")
            return rx.toast.error(f"Error al cambiar contraseña: {str(e)}")
        finally:
            self.loading = False
