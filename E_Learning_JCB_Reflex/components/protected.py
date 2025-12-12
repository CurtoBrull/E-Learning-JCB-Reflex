"""Componentes para proteger rutas según autenticación y roles."""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState


def require_auth(component: rx.Component) -> rx.Component:
    """
    Componente que requiere autenticación.
    Redirige a /login si el usuario no está autenticado.
    """
    return rx.cond(
        AuthState.is_authenticated,
        component,
        rx.center(
            rx.vstack(
                rx.icon("lock", size=50, color=rx.color("red", 9)),
                rx.heading("Acceso Restringido", size="8"),
                rx.text(
                    "Debes iniciar sesión para acceder a esta página",
                    size="4",
                    color=rx.color("gray", 11),
                ),
                rx.link(
                    rx.button(
                        "Iniciar Sesión",
                        size="3",
                        color_scheme="blue",
                    ),
                    href="/login",
                ),
                spacing="4",
                align_items="center",
                padding="4em",
            ),
            width="100%",
            min_height="50vh",
        ),
    )


def require_role(component: rx.Component, allowed_roles: list[str]) -> rx.Component:
    """
    Componente que requiere un rol específico.

    Args:
        component: Componente a mostrar si el usuario tiene el rol requerido
        allowed_roles: Lista de roles permitidos (ej: ["admin", "instructor"])
    """
    # Verificar si el usuario tiene uno de los roles permitidos
    has_permission = rx.cond(
        AuthState.is_authenticated,
        # Si está autenticado, verificar el rol
        rx.cond(
            AuthState.user_role.is_in(allowed_roles),  # Verificar si el rol está en la lista
            True,
            False,
        ),
        False,
    )

    return rx.cond(
        AuthState.is_authenticated,
        rx.cond(
            # Verificar cada rol permitido
            sum([AuthState.user_role == role for role in allowed_roles]) > 0,
            component,
            # No tiene permiso
            rx.center(
                rx.vstack(
                    rx.icon("shield-x", size=50, color=rx.color("red", 9)),
                    rx.heading("Acceso Denegado", size="8"),
                    rx.text(
                        f"No tienes permisos para acceder a esta página",
                        size="4",
                        color=rx.color("gray", 11),
                    ),
                    rx.text(
                        f"Tu rol actual: {AuthState.user_role}",
                        size="3",
                        color=rx.color("gray", 10),
                    ),
                    rx.link(
                        rx.button(
                            "Volver al Inicio",
                            size="3",
                            color_scheme="gray",
                        ),
                        href="/",
                    ),
                    spacing="4",
                    align_items="center",
                    padding="4em",
                ),
                width="100%",
                min_height="50vh",
            ),
        ),
        # No está autenticado
        rx.center(
            rx.vstack(
                rx.icon("lock", size=50, color=rx.color("red", 9)),
                rx.heading("Acceso Restringido", size="8"),
                rx.text(
                    "Debes iniciar sesión para acceder a esta página",
                    size="4",
                    color=rx.color("gray", 11),
                ),
                rx.link(
                    rx.button(
                        "Iniciar Sesión",
                        size="3",
                        color_scheme="blue",
                    ),
                    href="/login",
                ),
                spacing="4",
                align_items="center",
                padding="4em",
            ),
            width="100%",
            min_height="50vh",
        ),
    )


def admin_only(component: rx.Component) -> rx.Component:
    """Componente que solo pueden ver los administradores."""
    return require_role(component, ["admin"])


def instructor_only(component: rx.Component) -> rx.Component:
    """Componente que solo pueden ver los instructores."""
    return require_role(component, ["instructor"])


def student_only(component: rx.Component) -> rx.Component:
    """Componente que solo pueden ver los estudiantes."""
    return require_role(component, ["student"])


def instructor_or_admin(component: rx.Component) -> rx.Component:
    """Componente que pueden ver instructores y administradores."""
    return require_role(component, ["instructor", "admin"])
