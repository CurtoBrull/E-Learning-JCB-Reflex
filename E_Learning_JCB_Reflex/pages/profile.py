"""Página de perfil de usuario."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.states.profile_state import ProfileState


def profile_info_section() -> rx.Component:
    """Sección de información personal."""
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
    """Sección de cambio de contraseña."""
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
    """Sección de información de la cuenta."""
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
    """Contenido de la página de perfil."""
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
    """Página de perfil con protección de autenticación."""
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
