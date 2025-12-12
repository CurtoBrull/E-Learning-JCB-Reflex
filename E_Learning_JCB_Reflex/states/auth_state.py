"""Estado para la gestión de autenticación de usuarios."""

import reflex as rx
from E_Learning_JCB_Reflex.services import user_service
from E_Learning_JCB_Reflex.utils.password import verify_password


class AuthState(rx.State):
    """Estado de autenticación de usuarios."""

    # Usuario autenticado
    is_authenticated: bool = rx.Cookie(False, name="is_authenticated", max_age=86400)  # 24 horas
    current_user: dict = rx.LocalStorage({})

    # Campos del formulario de login
    login_email: str = ""
    login_password: str = ""

    # Campos del formulario de registro
    register_first_name: str = ""
    register_last_name: str = ""
    register_email: str = ""
    register_password: str = ""
    register_confirm_password: str = ""
    register_role: str = "student"  # Por defecto, student

    # Estados de la UI
    loading: bool = False
    error: str = ""
    success: str = ""

    # Métodos para login
    def set_login_email(self, value: str):
        """Actualizar el email de login."""
        self.login_email = value

    def set_login_password(self, value: str):
        """Actualizar el password de login."""
        self.login_password = value

    # Métodos para registro
    def set_register_first_name(self, value: str):
        """Actualizar el nombre de registro."""
        self.register_first_name = value

    def set_register_last_name(self, value: str):
        """Actualizar el apellido de registro."""
        self.register_last_name = value

    def set_register_email(self, value: str):
        """Actualizar el email de registro."""
        self.register_email = value

    def set_register_password(self, value: str):
        """Actualizar el password de registro."""
        self.register_password = value

    def set_register_confirm_password(self, value: str):
        """Actualizar la confirmación de password."""
        self.register_confirm_password = value

    def set_register_role(self, value: str):
        """Actualizar el rol de registro."""
        self.register_role = value

    def reset_login_form(self):
        """Resetear el formulario de login."""
        self.login_email = ""
        self.login_password = ""
        self.error = ""
        self.success = ""

    def reset_register_form(self):
        """Resetear el formulario de registro."""
        self.register_first_name = ""
        self.register_last_name = ""
        self.register_email = ""
        self.register_password = ""
        self.register_confirm_password = ""
        self.register_role = "student"
        self.error = ""
        self.success = ""

    async def handle_login(self):
        """Procesar el login de usuario."""
        # Validación
        if not self.login_email or not self.login_password:
            self.error = "Email y contraseña son obligatorios"
            return

        if "@" not in self.login_email or "." not in self.login_email:
            self.error = "Por favor, introduce un email válido"
            return

        # Resetear estados
        self.loading = True
        self.error = ""
        self.success = ""

        try:
            # Buscar usuario por email
            user = await user_service.get_user_by_email(self.login_email)

            if not user:
                self.error = "Email o contraseña incorrectos"
                self.loading = False
                return

            # Verificar password con bcrypt
            if not verify_password(self.login_password, user.password):
                self.error = "Email o contraseña incorrectos"
                self.loading = False
                return

            # Login exitoso
            self.is_authenticated = True
            self.current_user = user.to_dict()
            self.success = f"¡Bienvenido, {user.first_name}!"

            # Limpiar formulario
            self.login_email = ""
            self.login_password = ""

            # Redirigir al dashboard correspondiente según el rol
            if user.role == "admin":
                yield rx.redirect("/admin/dashboard")
            elif user.role == "instructor":
                yield rx.redirect("/instructor/dashboard")
            else:  # student
                yield rx.redirect("/student/dashboard")

        except Exception as e:
            print(f"Error during login: {e}")
            self.error = "Error al iniciar sesión. Por favor, inténtalo de nuevo."

        finally:
            self.loading = False

    async def handle_register(self):
        """Procesar el registro de nuevo usuario."""
        # Validación
        if not self.register_first_name or not self.register_last_name:
            self.error = "Nombre y apellido son obligatorios"
            return

        if not self.register_email or not self.register_password:
            self.error = "Email y contraseña son obligatorios"
            return

        if "@" not in self.register_email or "." not in self.register_email:
            self.error = "Por favor, introduce un email válido"
            return

        if len(self.register_password) < 6:
            self.error = "La contraseña debe tener al menos 6 caracteres"
            return

        if self.register_password != self.register_confirm_password:
            self.error = "Las contraseñas no coinciden"
            return

        # Resetear estados
        self.loading = True
        self.error = ""
        self.success = ""

        try:
            # Verificar si el usuario ya existe
            existing_user = await user_service.get_user_by_email(self.register_email)

            if existing_user:
                self.error = "Este email ya está registrado"
                self.loading = False
                return

            # Crear nuevo usuario (password se hashea automáticamente en user_service)
            result = await user_service.create_user(
                first_name=self.register_first_name,
                last_name=self.register_last_name,
                email=self.register_email,
                password=self.register_password,
                role=self.register_role
            )

            if result:
                self.success = "¡Registro exitoso! Redirigiendo al login..."

                # Limpiar formulario
                self.reset_register_form()

                # Redirigir al login después de un breve delay
                yield rx.redirect("/login")
            else:
                self.error = "Error al crear la cuenta. Por favor, inténtalo de nuevo."

        except Exception as e:
            print(f"Error during registration: {e}")
            self.error = "Error al registrar usuario. Por favor, inténtalo de nuevo."

        finally:
            self.loading = False

    def logout(self):
        """Cerrar sesión del usuario."""
        self.is_authenticated = False
        self.current_user = {}
        self.success = "Sesión cerrada exitosamente"
        return rx.redirect("/")

    @rx.var
    def user_name(self) -> str:
        """Obtener el nombre del usuario actual."""
        if self.is_authenticated and isinstance(self.current_user, dict) and self.current_user:
            return self.current_user.get("first_name", "Usuario")
        return ""

    @rx.var
    def user_role(self) -> str:
        """Obtener el rol del usuario actual."""
        if self.is_authenticated and isinstance(self.current_user, dict) and self.current_user:
            return self.current_user.get("role", "student")
        return "student"

    @rx.var
    def is_user_admin(self) -> bool:
        """Verificar si el usuario actual es administrador."""
        return self.is_authenticated and self.user_role == "admin"

    @rx.var
    def is_user_instructor(self) -> bool:
        """Verificar si el usuario actual es instructor."""
        return self.is_authenticated and self.user_role == "instructor"

    @rx.var
    def is_user_student(self) -> bool:
        """Verificar si el usuario actual es estudiante."""
        return self.is_authenticated and self.user_role == "student"
