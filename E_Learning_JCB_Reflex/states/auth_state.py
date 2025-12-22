"""
Estado para la gestión de autenticación de usuarios.

Este módulo define AuthState, el estado principal de autenticación que maneja
todo el ciclo de vida de la sesión del usuario: login, registro, logout y
gestión del usuario actual.

Características:
- Autenticación con email y contraseña
- Registro de nuevos usuarios con validación
- Manejo de sesión de usuario
- Propiedades computadas para verificar roles
- Validaciones de formularios
- Manejo de errores y mensajes de éxito
"""

import reflex as rx
from E_Learning_JCB_Reflex.services import user_service
from E_Learning_JCB_Reflex.utils.password import verify_password


class AuthState(rx.State):
    """
    Estado de autenticación de usuarios.

    Este estado maneja toda la lógica de autenticación de la aplicación,
    incluyendo login, registro y gestión de la sesión del usuario actual.
    Es la clase base de la que heredan muchos otros estados para acceder
    a la información del usuario autenticado.

    Atributos de sesión:
        is_authenticated (bool): Indica si hay un usuario autenticado
        current_user (dict): Diccionario con los datos del usuario actual
                            Estructura: {id, firstName, lastName, email, role}

    Campos de formulario de login:
        login_email (str): Email ingresado en el formulario de login
        login_password (str): Contraseña ingresada en el formulario de login

    Campos de formulario de registro:
        register_first_name (str): Nombre del nuevo usuario
        register_last_name (str): Apellido del nuevo usuario
        register_email (str): Email del nuevo usuario
        register_password (str): Contraseña del nuevo usuario
        register_confirm_password (str): Confirmación de contraseña
        register_role (str): Rol del nuevo usuario ("student", "instructor", "admin")

    Estados de la UI:
        loading (bool): Indica si hay una operación en curso
        error (str): Mensaje de error a mostrar al usuario
        success (str): Mensaje de éxito a mostrar al usuario

    Propiedades computadas:
        user_name: Nombre completo del usuario autenticado
        user_role: Rol del usuario autenticado
        is_user_admin: True si el usuario es administrador
        is_user_instructor: True si el usuario es instructor
        is_user_student: True si el usuario es estudiante

    Métodos principales:
        handle_login(): Procesa el login del usuario
        handle_register(): Procesa el registro de un nuevo usuario
        logout(): Cierra la sesión del usuario
    """

    # ========================================================================
    # ATRIBUTOS DE SESIÓN
    # ========================================================================

    # Usuario autenticado
    is_authenticated: bool = False  # Indica si hay un usuario autenticado
    current_user: dict = {}  # Datos del usuario actual (id, firstName, lastName, email, role)

    # ========================================================================
    # CAMPOS DEL FORMULARIO DE LOGIN
    # ========================================================================

    login_email: str = ""  # Email del formulario de login
    login_password: str = ""  # Contraseña del formulario de login

    # ========================================================================
    # CAMPOS DEL FORMULARIO DE REGISTRO
    # ========================================================================

    register_first_name: str = ""  # Nombre del nuevo usuario
    register_last_name: str = ""  # Apellido del nuevo usuario
    register_email: str = ""  # Email del nuevo usuario
    register_password: str = ""  # Contraseña del nuevo usuario
    register_confirm_password: str = ""  # Confirmación de contraseña
    register_role: str = "student"  # Rol por defecto: estudiante

    # ========================================================================
    # ESTADOS DE LA UI
    # ========================================================================

    loading: bool = False  # Indica operación en curso
    error: str = ""  # Mensaje de error para mostrar
    success: str = ""  # Mensaje de éxito para mostrar

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
        """
        Procesar el inicio de sesión de un usuario.

        Este método realiza las siguientes operaciones:
        1. Valida que se hayan ingresado email y contraseña
        2. Valida el formato del email
        3. Busca el usuario en la base de datos por email
        4. Verifica la contraseña usando bcrypt
        5. Si es exitoso, establece la sesión y redirige al dashboard correspondiente

        El método maneja los estados de loading, error y success automáticamente
        para que la UI pueda mostrar retroalimentación al usuario.

        Returns:
            Generator: Yield con rx.redirect() para redirigir al dashboard apropiado

        Efectos secundarios:
            - Actualiza is_authenticated a True si el login es exitoso
            - Actualiza current_user con los datos del usuario
            - Limpia el formulario de login
            - Redirige al usuario a su dashboard correspondiente:
              * Admin -> /admin/dashboard
              * Instructor -> /instructor/dashboard
              * Student -> /student/dashboard

        Manejo de errores:
            - Email o contraseña vacíos
            - Email con formato inválido
            - Usuario no encontrado
            - Contraseña incorrecta
            - Errores de base de datos
        """
        # Validación de campos obligatorios
        if not self.login_email or not self.login_password:
            self.error = "Email y contraseña son obligatorios"
            return

        # Validación básica del formato de email
        if "@" not in self.login_email or "." not in self.login_email:
            self.error = "Por favor, introduce un email válido"
            return

        # Resetear estados de UI para nueva operación
        self.loading = True
        self.error = ""
        self.success = ""

        try:
            # Buscar usuario por email en la base de datos
            user = await user_service.get_user_by_email(self.login_email)

            # Verificar si el usuario existe
            if not user:
                self.error = "Email o contraseña incorrectos"
                self.loading = False
                return

            # Verificar password con bcrypt (compara hash almacenado)
            if not verify_password(self.login_password, user.password):
                self.error = "Email o contraseña incorrectos"
                self.loading = False
                return

            # Login exitoso: establecer sesión
            self.is_authenticated = True
            self.current_user = user.to_dict()  # Convertir a dict para serialización
            self.success = f"¡Bienvenido, {user.first_name}!"

            # Limpiar formulario de login por seguridad
            self.login_email = ""
            self.login_password = ""

            # Redirigir al dashboard correspondiente según el rol del usuario
            if user.role == "admin":
                yield rx.redirect("/admin/dashboard")
            elif user.role == "instructor":
                yield rx.redirect("/instructor/dashboard")
            else:  # student (rol por defecto)
                yield rx.redirect("/student/dashboard")

        except Exception as e:
            # Capturar cualquier error inesperado
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
            return self.current_user.get("firstName", "Usuario")
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
