"""
Componentes para proteger rutas según autenticación y roles.

Este módulo proporciona componentes de alto orden (HOC) para controlar el acceso
a páginas y secciones de la aplicación basándose en el estado de autenticación
y el rol del usuario.

Componentes principales:
- require_auth: Requiere que el usuario esté autenticado
- require_role: Requiere que el usuario tenga un rol específico
- admin_only: Solo accesible para administradores
- instructor_only: Solo accesible para instructores
- student_only: Solo accesible para estudiantes
- instructor_or_admin: Accesible para instructores y administradores

Uso típico:
    >>> from E_Learning_JCB_Reflex.components.protected import admin_only
    >>>
    >>> def admin_panel():
    ...     return admin_only(
    ...         rx.box("Panel de administración")
    ...     )
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState


def require_auth(component: rx.Component) -> rx.Component:
    """
    Protege un componente requiriendo autenticación.

    Envuelve un componente para que solo sea visible si el usuario está autenticado.
    Si el usuario no está autenticado, muestra un mensaje de "Acceso Restringido"
    con un botón para ir a la página de login.

    Args:
        component: Componente de Reflex a proteger

    Returns:
        rx.Component: Componente protegido que verifica autenticación

    Ejemplo:
        >>> def my_profile_page():
        ...     return require_auth(
        ...         rx.box("Mi perfil privado")
        ...     )

    Nota:
        Este componente solo verifica autenticación, no roles específicos.
        Para protección basada en roles, usar require_role().
    """
    return rx.cond(
        AuthState.is_authenticated,  # Verificar si está autenticado
        component,  # Mostrar componente si está autenticado
        # Mostrar mensaje de acceso restringido si NO está autenticado
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
    # Crear la condición de rol basada en los roles permitidos
    if len(allowed_roles) == 1:
        role_condition = AuthState.user_role == allowed_roles[0]
    else:
        # Para múltiples roles, usar OR
        role_condition = (AuthState.user_role == allowed_roles[0])
        for role in allowed_roles[1:]:
            role_condition = role_condition | (AuthState.user_role == role)

    return rx.cond(
        AuthState.is_authenticated,
        rx.cond(
            role_condition,
            component,
            # No tiene permiso
            rx.center(
                rx.vstack(
                    rx.icon("shield-x", size=50, color=rx.color("red", 9)),
                    rx.heading("Acceso Denegado", size="8"),
                    rx.text(
                        "No tienes permisos para acceder a esta página",
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
