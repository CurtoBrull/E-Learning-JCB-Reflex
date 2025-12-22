"""
Página de perfil de usuario de la plataforma E-Learning JCB.

Este módulo proporciona una interfaz para que los usuarios autenticados
puedan ver y editar su información personal, cambiar su contraseña y
gestionar su cuenta.

Funcionalidades:
- Edición de información personal (nombre, apellido, email)
- Cambio de contraseña con validación
- Visualización de información de cuenta (rol, fecha de creación)
- Secciones organizadas en tarjetas (cards)
- Botón de retorno al dashboard según el rol del usuario
- Protección de autenticación

Ruta: /profile
Acceso: Protegida (requiere autenticación)
Estado: ProfileState para gestionar información del perfil
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.states.profile_state import ProfileState


def profile_info_section() -> rx.Component:
    """
    Renderiza la sección de información personal del usuario.

    Muestra un formulario con los campos editables del perfil:
    nombre, apellido y email. Incluye un botón para guardar cambios
    con estado de carga.

    Returns:
        rx.Component: Card con formulario de información personal

    Notas:
        - Los campos están vinculados a ProfileState (first_name, last_name, email)
        - El botón ejecuta ProfileState.update_profile al hacer click
        - Muestra spinner mientras ProfileState.loading es True
    """
    return rx.card(
        rx.vstack(
            rx.heading("Información Personal", size="6"),
            rx.divider(),
            rx.form(
                rx.vstack(
                    rx.vstack(
                        rx.text("Nombre", size="2", weight="bold"),
                        rx.input(
                            placeholder="Nombre",
                            value=ProfileState.first_name,
                            on_change=ProfileState.set_first_name,
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text("Apellido", size="2", weight="bold"),
                        rx.input(
                            placeholder="Apellido",
                            value=ProfileState.last_name,
                            on_change=ProfileState.set_last_name,
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text("Email", size="2", weight="bold"),
                        rx.input(
                            placeholder="Email",
                            type="email",
                            value=ProfileState.email,
                            on_change=ProfileState.set_email,
                            size="3",
                            width="100%",
                        ),
                        spacing="2",
                        width="100%",
                    ),
                    rx.button(
                        rx.cond(
                            ProfileState.loading,
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Guardando..."),
                                spacing="2",
                            ),
                            rx.text("Guardar Cambios"),
                        ),
                        on_click=ProfileState.update_profile,
                        size="3",
                        width="100%",
                        disabled=ProfileState.loading,
                    ),
                    spacing="4",
                    width="100%",
                ),
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
    )


def password_section() -> rx.Component:
    """
    Renderiza la sección de cambio de contraseña.

    Muestra una sección colapsable con un formulario para cambiar
    la contraseña. Requiere la contraseña actual y confirmación
    de la nueva contraseña.

    Returns:
        rx.Component: Card con formulario de cambio de contraseña

    Notas:
        - La sección se expande/colapsa con ProfileState.toggle_password_section
        - Requiere contraseña actual, nueva contraseña y confirmación
        - El botón ejecuta ProfileState.change_password al hacer click
        - Muestra spinner mientras ProfileState.loading es True
        - El botón tiene color_scheme="orange" para indicar acción sensible
    """
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.heading("Seguridad", size="6"),
                rx.spacer(),
                rx.button(
                    rx.cond(
                        ProfileState.show_password_section,
                        rx.hstack(
                            rx.icon("chevron-up", size=20),
                            rx.text("Ocultar"),
                            spacing="2",
                        ),
                        rx.hstack(
                            rx.icon("lock", size=20),
                            rx.text("Cambiar Contraseña"),
                            spacing="2",
                        ),
                    ),
                    on_click=ProfileState.toggle_password_section,
                    variant="soft",
                    size="2",
                ),
                width="100%",
                align_items="center",
            ),
            rx.divider(),
            rx.cond(
                ProfileState.show_password_section,
                rx.form(
                    rx.vstack(
                        rx.vstack(
                            rx.text("Contraseña Actual", size="2", weight="bold"),
                            rx.input(
                                placeholder="Contraseña actual",
                                type="password",
                                value=ProfileState.current_password,
                                on_change=ProfileState.set_current_password,
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text("Nueva Contraseña", size="2", weight="bold"),
                            rx.input(
                                placeholder="Nueva contraseña (mínimo 6 caracteres)",
                                type="password",
                                value=ProfileState.new_password,
                                on_change=ProfileState.set_new_password,
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.vstack(
                            rx.text("Confirmar Nueva Contraseña", size="2", weight="bold"),
                            rx.input(
                                placeholder="Confirmar nueva contraseña",
                                type="password",
                                value=ProfileState.confirm_password,
                                on_change=ProfileState.set_confirm_password,
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        rx.button(
                            rx.cond(
                                ProfileState.loading,
                                rx.hstack(
                                    rx.spinner(size="3"),
                                    rx.text("Cambiando..."),
                                    spacing="2",
                                ),
                                rx.text("Cambiar Contraseña"),
                            ),
                            on_click=ProfileState.change_password,
                            size="3",
                            width="100%",
                            color_scheme="orange",
                            disabled=ProfileState.loading,
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    width="100%",
                ),
            ),
            spacing="4",
            width="100%",
        ),
    )


def account_info_section() -> rx.Component:
    """
    Renderiza la sección de información de cuenta (solo lectura).

    Muestra información no editable de la cuenta del usuario:
    rol actual y fecha de creación de la cuenta.

    Returns:
        rx.Component: Card con información de cuenta

    Notas:
        - El rol se muestra con un badge de color según el tipo
        - Los colores son: student=blue, instructor=green, admin=red
        - La fecha se obtiene de ProfileState.current_user
        - Todos los campos son de solo lectura
    """
    return rx.card(
        rx.vstack(
            rx.heading("Información de la Cuenta", size="6"),
            rx.divider(),
            rx.vstack(
                rx.hstack(
                    rx.vstack(
                        rx.text("Rol", size="2", color=rx.color("gray", 11)),
                        rx.badge(
                            rx.cond(
                                ProfileState.current_user.get("role") == "student",
                                "Estudiante",
                                rx.cond(
                                    ProfileState.current_user.get("role") == "instructor",
                                    "Instructor",
                                    "Administrador",
                                ),
                            ),
                            color_scheme=rx.cond(
                                ProfileState.current_user.get("role") == "student",
                                "blue",
                                rx.cond(
                                    ProfileState.current_user.get("role") == "instructor",
                                    "green",
                                    "red",
                                ),
                            ),
                            size="2",
                        ),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.spacer(),
                    rx.vstack(
                        rx.text("Miembro desde", size="2", color=rx.color("gray", 11)),
                        rx.text(
                            ProfileState.current_user.get("createdAt", "").to_string()[:10],
                            size="2",
                            weight="medium",
                        ),
                        spacing="2",
                        align_items="end",
                    ),
                    width="100%",
                ),
                spacing="3",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
    )


def profile_page_content() -> rx.Component:
    """
    Renderiza el contenido completo de la página de perfil.

    Organiza las secciones del perfil en un layout de 2 columnas:
    - Columna izquierda: información personal y cambio de contraseña
    - Columna derecha: información de cuenta

    Returns:
        rx.Component: Contenido completo de la página de perfil

    Notas:
        - Incluye header con título y botón de retorno al dashboard
        - El botón de retorno redirige al dashboard según el rol del usuario
        - Utiliza on_mount con ProfileState.load_profile_data
        - Max width de 1200px para mejor legibilidad
        - Layout responsive con grid de 2 columnas
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading("Mi Perfil", size="9"),
                        rx.text(
                            "Gestiona tu información personal y configuración de cuenta",
                            size="4",
                            color=rx.color("gray", 11),
                        ),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("arrow-left", size=20),
                            rx.text("Volver al Dashboard"),
                            spacing="2",
                        ),
                        on_click=rx.redirect(
                            rx.cond(
                                ProfileState.current_user.get("role") == "student",
                                "/student/dashboard",
                                rx.cond(
                                    ProfileState.current_user.get("role") == "instructor",
                                    "/instructor/dashboard",
                                    "/admin/dashboard",
                                ),
                            )
                        ),
                        variant="soft",
                        size="3",
                    ),
                    width="100%",
                    align_items="center",
                ),
                # Grid de secciones
                rx.grid(
                    # Columna izquierda
                    rx.vstack(
                        profile_info_section(),
                        password_section(),
                        spacing="4",
                        width="100%",
                    ),
                    # Columna derecha
                    rx.vstack(
                        account_info_section(),
                        spacing="4",
                        width="100%",
                    ),
                    columns="2",
                    spacing="4",
                    width="100%",
                ),
                spacing="6",
                width="100%",
                padding_y="4",
                on_mount=ProfileState.load_profile_data,
            ),
            max_width="1200px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
    )


def profile_page() -> rx.Component:
    """
    Renderiza la página de perfil con protección de autenticación.

    Verifica si el usuario está autenticado antes de mostrar el contenido.
    Si no está autenticado, muestra mensaje de acceso denegado con
    botón para ir al login.

    Returns:
        rx.Component: Página de perfil o mensaje de acceso denegado

    Notas:
        - Verifica ProfileState.is_authenticated antes de mostrar contenido
        - Si no autenticado, muestra pantalla completa centrada con mensaje
        - Incluye botón que redirige a /login
    """
    return rx.cond(
        ProfileState.is_authenticated,
        profile_page_content(),
        rx.center(
            rx.vstack(
                rx.heading("Acceso Denegado", size="8"),
                rx.text("Debes iniciar sesión para ver tu perfil"),
                rx.link(
                    rx.button("Ir a Login", size="3"),
                    href="/login",
                ),
                spacing="4",
            ),
            height="100vh",
        ),
    )
