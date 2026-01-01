"""
Página principal (homepage) de la plataforma E-Learning JCB.

Esta página es el punto de entrada principal de la aplicación. Muestra:
- Mensaje de bienvenida y descripción de la plataforma
- Sección de cursos populares (máximo 6 cursos destacados)
- Navegación principal (navbar)

Ruta: /
Acceso: Pública (sin autenticación requerida)
Estado: CourseState para cargar cursos populares
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_state import CourseState
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.course_card import course_card


def logout_success_dialog() -> rx.Component:
    """
    Renderiza un diálogo modal de confirmación de cierre de sesión exitoso.

    Muestra un diálogo con mensaje de éxito y botón para cerrar.

    Returns:
        rx.Component: Alert dialog de éxito de logout

    Notas:
        - Se muestra cuando AuthState.show_logout_success_message es True
        - Incluye icono de éxito (circle-check) en color verde
        - Botón "Cerrar" cierra el diálogo
    """
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.vstack(
                rx.hstack(
                    rx.icon("circle-check", size=32, color=rx.color("green", 9)),
                    rx.alert_dialog.title("Sesión Cerrada"),
                    spacing="3",
                    align_items="center",
                ),
                rx.alert_dialog.description(
                    "Has cerrado sesión exitosamente. ¡Hasta pronto!",
                    size="3",
                ),
                rx.divider(margin_y="4"),
                rx.button(
                    "Cerrar",
                    variant="solid",
                    color_scheme="blue",
                    size="3",
                    width="100%",
                    on_click=AuthState.close_logout_message,
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
        ),
        open=AuthState.show_logout_success_message,
    )


def index() -> rx.Component:
    """
    Renderizar la página principal de la plataforma.

    Carga automáticamente los cursos populares al montarse la página
    usando CourseState.load_popular_courses(). Muestra los cursos en
    un grid responsive de 3 columnas.

    Returns:
        rx.Component: Página completa con navbar, header y grid de cursos

    Eventos:
        - on_mount: Carga cursos populares al cargar la página
    """
    return rx.box(
        # Background image
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background_image="url(/images/bg/background_login.webp)",
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            opacity="0.15",
            z_index="-1",
        ),
        rx.vstack(
            navbar(),
            logout_success_dialog(),
            rx.container(
                rx.vstack(
                    # Header
                    rx.heading(
                        "¡Bienvenido a E-Learning JCB!",
                        size="9",
                        margin_bottom="2",
                        text_align="center",
                        max_width="100%",
                    ),
                    rx.text(
                        "¡Aprende y Crece con nosotros!",
                        size="8",
                        color=rx.color("gray", 12),
                        margin_bottom="8",
                        text_align="center",
                    ),
                    rx.text(
                        "Descubre nuestros cursos online impartidos por expertos en programación, administración de sistemas y más. Aprende a tu ritmo, mejora tus habilidades y obtén certificaciones reconocidas en el sector IT.",
                        size="6",
                        color=rx.color("gray", 12),
                        margin_bottom="8",
                        text_align="center",
                    ),
                # Mensaje de error
                rx.cond(
                    CourseState.error != "",
                    rx.callout(
                        CourseState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Estado de carga
                rx.cond(
                    CourseState.loading,
                    rx.spinner(size="3"),
                ),
                # Cuadrícula de cursos
                rx.cond(
                    CourseState.courses.length() > 0,
                    rx.vstack(
                        rx.heading("Cursos Populares", size="7", margin_bottom="4", text_align="center"),
                        rx.grid(

                            rx.foreach(CourseState.courses, course_card),
                            columns="3",
                            spacing="4",
                            width="100%",
                        ),
                        width="100%",
                        align_items="center",
                    ),
                ),
                # Estado vacío
                rx.cond(
                    (CourseState.courses.length() == 0) & (~CourseState.loading) & (CourseState.error == ""),
                    rx.box(
                        rx.text(
                            "No hay cursos disponibles en este momento.",
                            color=rx.color("gray", 10),
                            text_align="center",
                        ),
                        padding="8",
                    ),
                ),
                spacing="4",
                width="100%",
                padding_y="8",
                align_items="center",
                on_mount=CourseState.load_popular_courses,
            ),
            width="100%",
            max_width="100%",
            padding_x="2rem",
        ),
        width="100%",
        spacing="0",
        ),
        width="100%",
        position="relative",
    )
