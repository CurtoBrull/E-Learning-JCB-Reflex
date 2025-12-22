"""
Componente de navegación principal (navbar).

Este módulo define la barra de navegación responsive de la aplicación,
que se adapta a dispositivos móviles, tabletas y escritorio. Incluye:
- Logo y título de la aplicación
- Links de navegación a páginas principales
- Menú de usuario con opciones específicas según rol
- Botón de cambio de tema (dark/light mode)
- Versión móvil con menú hamburguesa

El navbar cambia dinámicamente según el estado de autenticación del usuario.
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState


def navbar_link(text: str, url: str) -> rx.Component:
    """
    Crear un enlace estilizado para la barra de navegación.

    Args:
        text: Texto a mostrar en el enlace
        url: URL de destino del enlace

    Returns:
        rx.Component: Link con estilo consistente para la navbar

    Ejemplo:
        >>> navbar_link("Cursos", "/courses")
        # Crea un enlace a la página de cursos con tamaño de texto 4
    """
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def user_menu() -> rx.Component:
    """
    Menú desplegable para usuarios autenticados.

    Muestra un menú con el nombre del usuario y opciones contextuales
    según su rol. Las opciones incluyen:
    - Dashboard específico del rol (admin/instructor/student)
    - Acceso al perfil de usuario
    - Botón de cerrar sesión

    El menú se construye dinámicamente usando rx.cond para mostrar
    solo las opciones relevantes al rol del usuario actual.

    Returns:
        rx.Component: Menú desplegable con avatar y opciones de usuario

    Nota:
        Utiliza AuthState.user_name, AuthState.user_role y propiedades
        computadas como is_user_admin para determinar qué mostrar.
    """
    return rx.menu.root(
        rx.menu.trigger(
            rx.hstack(
                rx.icon("user", size=20),
                rx.text(AuthState.user_name, size="4", weight="medium"),
                rx.icon("chevron-down", size=16),
                spacing="2",
                align_items="center",
                cursor="pointer",
                padding="0.5em",
                border_radius="md",
                _hover={"bg": rx.color("accent", 4)},
            )
        ),
        rx.menu.content(
            rx.cond(
                AuthState.is_user_admin,
                rx.menu.item(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=16),
                        rx.text("Panel Admin"),
                        spacing="2",
                    ),
                    on_click=lambda: rx.redirect("/admin/dashboard"),
                ),
            ),
            rx.cond(
                AuthState.is_user_instructor,
                rx.menu.item(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=16),
                        rx.text("Mi Dashboard"),
                        spacing="2",
                    ),
                    on_click=lambda: rx.redirect("/instructor/dashboard"),
                ),
            ),
            rx.cond(
                AuthState.is_user_student,
                rx.menu.item(
                    rx.hstack(
                        rx.icon("layout-dashboard", size=16),
                        rx.text("Mi Dashboard"),
                        spacing="2",
                    ),
                    on_click=lambda: rx.redirect("/student/dashboard"),
                ),
            ),
            rx.menu.separator(),
            rx.menu.item(
                rx.hstack(
                    rx.icon("user", size=16),
                    rx.text("Mi Perfil"),
                    spacing="2",
                ),
                on_click=lambda: rx.redirect("/profile"),
            ),
            rx.menu.separator(),
            rx.menu.item(
                rx.hstack(
                    rx.icon("log-out", size=16),
                    rx.text("Cerrar Sesión"),
                    spacing="2",
                ),
                on_click=AuthState.logout,
                color_scheme="red",
            ),
        ),
    )


def navbar() -> rx.Component:
    """
    Barra de navegación principal responsive de la aplicación.

    Componente principal de navegación que se adapta automáticamente al
    tamaño de pantalla del dispositivo. Proporciona dos vistas:

    1. Desktop: Barra horizontal con logo, links y menú de usuario
    2. Mobile/Tablet: Versión compacta con menú hamburguesa

    Características:
        - Logo y título clicables que redirigen a la página de inicio
        - Links a las secciones principales (Inicio, Cursos, Instructores, Contacto)
        - Menú de usuario autenticado o botón de login según estado
        - Botón de cambio de tema claro/oscuro
        - Fondo con color de acento del sistema de diseño

    Returns:
        rx.Component: Barra de navegación completa y responsive

    Nota:
        - Usa rx.desktop_only() y rx.mobile_and_tablet() para responsive design
        - El menú cambia según AuthState.is_authenticated
        - La navegación móvil incluye información del rol del usuario
    """
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                # Logo y título
                rx.hstack(
                    rx.link(
                        rx.hstack(
                            rx.image(
                                src="/E-Learning-JCB.png",
                                width="2.25em",
                                height="auto",
                                border_radius="25%",
                            ),
                            rx.heading("E-Learning JCB", size="7", weight="bold"),
                            spacing="3",
                            align_items="center",
                        ),
                        href="/",
                    ),
                ),
                # Navegación
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Cursos", "/courses"),
                    navbar_link("Instructores", "/instructors"),
                    navbar_link("Contacto", "/contact"),
                    # Mostrar login o menú de usuario según autenticación
                    rx.cond(
                        AuthState.is_authenticated,
                        user_menu(),
                        navbar_link("Login", "/login"),
                    ),
                    rx.color_mode.button(),
                    justify="end",
                    spacing="5",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                # Logo y título (móvil)
                rx.link(
                    rx.hstack(
                        rx.image(
                            src="/E-Learning-JCB.png",
                            width="2em",
                            height="auto",
                            border_radius="25%",
                        ),
                        rx.heading("E-Learning JCB", size="6", weight="bold"),
                        spacing="2",
                        align_items="center",
                    ),
                    href="/",
                ),
                # Menú móvil
                rx.hstack(
                    rx.color_mode.button(),
                    rx.menu.root(
                        rx.menu.trigger(rx.icon("menu", size=30)),
                        rx.menu.content(
                            rx.menu.item(rx.link("Inicio", href="/")),
                            rx.menu.item(rx.link("Cursos", href="/courses")),
                            rx.menu.item(rx.link("Instructores", href="/instructors")),
                            rx.menu.item(rx.link("Contacto", href="/contact")),
                            rx.cond(
                                AuthState.is_authenticated,
                                rx.fragment(
                                    rx.menu.separator(),
                                    rx.menu.item(
                                        rx.text(f"👤 {AuthState.user_name} ({AuthState.user_role})")
                                    ),
                                    rx.cond(
                                        AuthState.is_user_admin,
                                        rx.menu.item(rx.link("Panel Admin", href="/admin/dashboard")),
                                    ),
                                    rx.cond(
                                        AuthState.is_user_instructor,
                                        rx.menu.item(rx.link("Mi Dashboard", href="/instructor/dashboard")),
                                    ),
                                    rx.cond(
                                        AuthState.is_user_student,
                                        rx.menu.item(rx.link("Mi Dashboard", href="/student/dashboard")),
                                    ),
                                    rx.menu.separator(),
                                    rx.menu.item(rx.link("Mi Perfil", href="/profile")),
                                    rx.menu.separator(),
                                    rx.menu.item(
                                        rx.hstack(
                                            rx.icon("log-out", size=16),
                                            rx.text("Cerrar Sesión"),
                                            spacing="2",
                                        ),
                                        on_click=AuthState.logout,
                                    ),
                                ),
                                rx.menu.item(rx.link("Login", href="/login")),
                            ),
                        ),
                        justify="end",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
