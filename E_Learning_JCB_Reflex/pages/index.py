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
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.course_card import course_card


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
    return rx.vstack(
        navbar(),
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
                    color=rx.color("gray", 11),
                    margin_bottom="8",
                    text_align="center",
                ),
                rx.text(
                    "Descubre nuestros cursos online impartidos por expertos en programación, administración de sistemas y más. Aprende a tu ritmo, mejora tus habilidades y obtén certificaciones reconocidas en el sector IT.",
                    size="6",
                    color=rx.color("gray", 11),
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
    )
