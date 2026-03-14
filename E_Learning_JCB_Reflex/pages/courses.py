"""
Página de catálogo de cursos de la plataforma E-Learning JCB.

Este módulo muestra el catálogo completo de todos los cursos disponibles
en la plataforma. Los cursos se presentan en una cuadrícula utilizando
el componente course_card para mantener consistencia visual.

Funcionalidades:
- Catálogo completo de cursos disponibles
- Visualización en cuadrícula responsive (3 columnas)
- Estado de carga mientras se obtienen los datos
- Manejo de errores con mensajes visuales
- Carga automática de cursos al montar la página

Ruta: /courses
Acceso: Pública (sin autenticación requerida)
Estado: CourseState para cargar y mostrar todos los cursos
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_state import CourseState
from E_Learning_JCB_Reflex.states.enrollment_state import EnrollmentState
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer
from E_Learning_JCB_Reflex.components.course_card import course_card


def courses_page() -> rx.Component:
    """
    Renderiza la página con el catálogo completo de cursos.

    Muestra todos los cursos disponibles en la plataforma organizados
    en una cuadrícula de 3 columnas. Cada curso se renderiza usando
    el componente course_card que muestra información básica y permite
    navegar a los detalles del curso.

    Returns:
        rx.Component: Componente de Reflex con el catálogo de cursos

    Notas:
        - Utiliza on_mount para cargar automáticamente los cursos al abrir la página
        - Muestra un spinner mientras CourseState.loading es True
        - Muestra callout de error si CourseState.error no está vacío
        - La cuadrícula solo se muestra si hay cursos disponibles (CourseState.courses.length() > 0)
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
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Todos los Cursos",
                        size="8",
                        margin_bottom="4",
                        text_align="center",
                    ),
                    # Buscador
                    rx.box(
                        rx.input(
                            rx.input.slot(
                                rx.icon("search", size=18, color=rx.color("gray", 10)),
                            ),
                            placeholder="Buscar por título, instructor, nivel...",
                            value=CourseState.search_query,
                            on_change=CourseState.set_search_query,
                            size="3",
                            width="100%",
                        ),
                        width="100%",
                        max_width="600px",
                        margin_bottom="4",
                    ),
                    # Contador de resultados
                    rx.cond(
                        CourseState.search_query != "",
                        rx.text(
                            f"{CourseState.filtered_courses.length()} resultado(s) para: ",
                            rx.text.strong(CourseState.search_query),
                            size="2",
                            color=rx.color("gray", 10),
                            margin_bottom="2",
                        ),
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
                # Cuadrícula de cursos usando course_card
                rx.cond(
                    CourseState.filtered_courses.length() > 0,
                    rx.grid(
                        rx.foreach(
                            CourseState.filtered_courses,
                            lambda course: course_card(course)
                        ),
                        columns="3",
                        spacing="6",
                    ),
                    rx.cond(
                        CourseState.search_query != "",
                        rx.center(
                            rx.vstack(
                                rx.icon("search-x", size=40, color=rx.color("gray", 8)),
                                rx.text(
                                    "No se encontraron cursos con ese criterio",
                                    size="4",
                                    color=rx.color("gray", 10),
                                ),
                                rx.button(
                                    "Limpiar búsqueda",
                                    on_click=CourseState.set_search_query(""),
                                    variant="soft",
                                    size="2",
                                ),
                                spacing="3",
                                align_items="center",
                                padding="4em",
                            ),
                        ),
                    ),
                ),
                spacing="4",
                width="100%",
                padding_y="8",
                align_items="center",
                on_mount=CourseState.load_courses, # Cargar todos los cursos al montar la página
            ),
            width="100%",
            max_width="100%",
            padding_x="2rem",
        ),
        footer(),
        width="100%",
        spacing="0",
        ),
        width="100%",
        position="relative",
    )
