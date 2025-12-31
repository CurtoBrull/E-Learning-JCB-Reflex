"""
Página del visor de cursos para estudiantes inscritos.

Este módulo proporciona una interfaz completa para que los estudiantes
visualicen el contenido de los cursos en los que están inscritos.

Funcionalidades:
- Reproducción de videos de YouTube embebidos
- Lista de lecciones con navegación
- Indicador de progreso en el curso
- Navegación entre lecciones (anterior/siguiente)
- Información de la lección actual (título, descripción, duración)
- Diseño tipo Netflix con video player principal y sidebar de lecciones

Ruta: /courses/[course_id]/view
Acceso: Solo estudiantes inscritos en el curso
Estados: CourseViewerState (gestión del visor)
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_viewer_state import CourseViewerState
from E_Learning_JCB_Reflex.components.navbar import navbar


def lesson_item(lesson: dict, index: int) -> rx.Component:
    """
    Renderiza un item de lección en la lista lateral.

    Muestra la información de una lección en la sidebar, incluyendo
    número de orden, título y duración. Resalta la lección actual.

    Args:
        lesson: Diccionario con los datos de la lección
        index: Índice de la lección en la lista

    Returns:
        rx.Component: Box con la información de la lección
    """
    return rx.box(
        rx.hstack(
            rx.box(
                rx.text(
                    f"{index + 1}",
                    size="2",
                    weight="bold",
                    color="white",
                ),
                width="24px",
                height="24px",
                border_radius="50%",
                bg=rx.cond(
                    CourseViewerState.current_lesson_index == index,
                    rx.color("blue", 9),
                    rx.color("gray", 6),
                ),
                display="flex",
                align_items="center",
                justify_content="center",
            ),
            rx.vstack(
                rx.text(
                    lesson["title"],
                    size="2",
                    weight="medium",
                    no_of_lines=1,
                ),
                rx.text(
                    f"{lesson['duration']} min",
                    size="1",
                    color="gray",
                ),
                align_items="start",
                spacing="0",
                flex="1",
            ),
            spacing="3",
            width="100%",
        ),
        padding="3",
        border_radius="md",
        cursor="pointer",
        bg=rx.cond(
            CourseViewerState.current_lesson_index == index,
            rx.color("gray", 3),
            "transparent",
        ),
        _hover={
            "background": rx.color("gray", 2),
        },
        on_click=lambda: CourseViewerState.select_lesson(index),
        width="100%",
    )


def video_player() -> rx.Component:
    """
    Renderiza el reproductor de video de YouTube.

    Muestra el video de la lección actual usando un iframe de YouTube embebido.
    Si no hay video disponible, muestra un mensaje indicándolo.

    Returns:
        rx.Component: Reproductor de video o mensaje de no disponible
    """
    return rx.cond(
        CourseViewerState.current_video_url != "",
        rx.box(
            rx.html(
                f"""
                <iframe
                    width="100%"
                    height="100%"
                    src="{CourseViewerState.current_video_url}"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    style="border-radius: 8px;"
                ></iframe>
                """,
                width="100%",
                height="100%",
            ),
            width="100%",
            height=rx.cond(
                CourseViewerState.sidebar_visible,
                "600px",  # Con sidebar: altura estándar
                "75vh"    # Sin sidebar: 75% de la altura de la ventana
            ),
            border_radius="lg",
            overflow="hidden",
        ),
        rx.box(
            rx.vstack(
                rx.icon("video-off", size=64, color=rx.color("gray", 6)),
                rx.text(
                    "Video no disponible",
                    size="5",
                    weight="bold",
                ),
                rx.text(
                    "Esta lección aún no tiene un video asociado",
                    size="3",
                    color="gray",
                ),
                spacing="3",
                align_items="center",
            ),
            width="100%",
            height="600px",
            display="flex",
            align_items="center",
            justify_content="center",
            bg=rx.color("gray", 2),
            border_radius="lg",
        ),
    )


def lesson_info() -> rx.Component:
    """
    Renderiza la información de la lección actual.

    Muestra el título, descripción y duración de la lección que se está visualizando.

    Returns:
        rx.Component: Sección con la información de la lección
    """
    return rx.box(
        rx.vstack(
            rx.heading(
                CourseViewerState.current_lesson["title"],
                size="7",
            ),
            rx.text(
                CourseViewerState.current_lesson["content"],
                size="3",
                color="gray",
            ),
            rx.hstack(
                rx.badge(
                    f"Lección {CourseViewerState.current_lesson_index + 1} de {CourseViewerState.total_lessons}",
                    color_scheme="blue",
                ),
                rx.badge(
                    f"{CourseViewerState.current_lesson['duration']} minutos",
                    color_scheme="green",
                ),
                spacing="2",
            ),
            align_items="start",
            spacing="3",
            width="100%",
        ),
        padding="4",
        width="100%",
    )


def navigation_controls() -> rx.Component:
    """
    Renderiza los controles de navegación entre lecciones.

    Muestra botones para ir a la lección anterior y siguiente.
    Los botones se deshabilitan si no hay lección anterior/siguiente.

    Returns:
        rx.Component: Controles de navegación
    """
    return rx.hstack(
        rx.button(
            rx.hstack(
                rx.icon("chevron-left", size=18),
                rx.text("Anterior"),
                spacing="2",
            ),
            variant="soft",
            size="3",
            on_click=CourseViewerState.go_to_previous_lesson,
            disabled=~CourseViewerState.has_previous_lesson,
        ),
        rx.spacer(),
        rx.button(
            rx.hstack(
                rx.text("Siguiente"),
                rx.icon("chevron-right", size=18),
                spacing="2",
            ),
            variant="soft",
            size="3",
            on_click=CourseViewerState.go_to_next_lesson,
            disabled=~CourseViewerState.has_next_lesson,
        ),
        width="100%",
        padding="4",
    )


def progress_bar() -> rx.Component:
    """
    Renderiza la barra de progreso del curso.

    Muestra una barra visual indicando el progreso actual en el curso
    basado en las lecciones completadas.

    Returns:
        rx.Component: Barra de progreso
    """
    return rx.box(
        rx.vstack(
            rx.hstack(
                rx.text("Progreso del curso", size="2", weight="medium"),
                rx.spacer(),
                rx.text(
                    f"{CourseViewerState.progress_percentage:.0f}%",
                    size="2",
                    weight="bold",
                    color=rx.color("blue", 9),
                ),
                width="100%",
            ),
            rx.box(
                rx.box(
                    width=f"{CourseViewerState.progress_percentage}%",
                    height="100%",
                    bg=rx.color("blue", 9),
                    border_radius="full",
                    transition="width 0.3s ease",
                ),
                width="100%",
                height="8px",
                bg=rx.color("gray", 3),
                border_radius="full",
                overflow="hidden",
            ),
            spacing="2",
            width="100%",
        ),
        padding="4",
        width="100%",
    )


def lessons_sidebar() -> rx.Component:
    """
    Renderiza la sidebar con la lista de lecciones.

    Muestra todas las lecciones del curso en un panel lateral con scroll,
    permitiendo la navegación rápida entre lecciones.

    Returns:
        rx.Component: Sidebar con lista de lecciones
    """
    return rx.box(
        rx.vstack(
            rx.heading("Contenido del curso", size="5", margin_bottom="2"),
            progress_bar(),
            rx.divider(),
            rx.box(
                rx.vstack(
                    rx.foreach(
                        CourseViewerState.lessons,
                        lambda lesson, index: lesson_item(lesson, index),
                    ),
                    spacing="1",
                    width="100%",
                ),
                width="100%",
                max_height="600px",
                overflow_y="auto",
                padding_right="2",
            ),
            spacing="3",
            align_items="start",
            width="100%",
            height="100%",
        ),
        width="350px",
        padding="4",
        bg="white",
        border_radius="lg",
        border=f"1px solid {rx.color('gray', 4)}",
        height="fit-content",
        max_height="calc(100vh - 150px)",
        position="sticky",
        top="20px",
    )


def course_viewer_page() -> rx.Component:
    """
    Renderiza la página completa del visor de cursos.

    Muestra la interfaz completa del visor con:
    - Navbar superior
    - Reproductor de video principal
    - Información de la lección
    - Controles de navegación
    - Sidebar con lista de lecciones y progreso

    Returns:
        rx.Component: Página completa del visor de cursos
    """
    return rx.vstack(
        navbar(),
        rx.box(
            rx.vstack(
                # Estado de carga
                rx.cond(
                    CourseViewerState.loading,
                    rx.center(
                        rx.spinner(size="3"),
                        height="50vh",
                    ),
                ),
                # Mensaje de error
                rx.cond(
                    CourseViewerState.error != "",
                    rx.center(
                        rx.callout(
                            CourseViewerState.error,
                            icon="triangle-alert",
                            color_scheme="red",
                            size="3",
                        ),
                        height="50vh",
                    ),
                ),
                # Contenido del visor
                rx.cond(
                    (CourseViewerState.is_enrolled) & (CourseViewerState.loading == False) & (CourseViewerState.error == ""),
                    rx.vstack(
                        # Encabezado con título del curso y botón toggle
                        rx.hstack(
                            rx.heading(
                                CourseViewerState.course_title,
                                size="8",
                            ),
                            rx.spacer(),
                            rx.button(
                                rx.cond(
                                    CourseViewerState.sidebar_visible,
                                    rx.hstack(
                                        rx.icon("panel-right-close"),
                                        rx.text("Ocultar contenido"),
                                        spacing="2",
                                    ),
                                    rx.hstack(
                                        rx.icon("panel-right-open"),
                                        rx.text("Mostrar contenido"),
                                        spacing="2",
                                    ),
                                ),
                                on_click=CourseViewerState.toggle_sidebar,
                                variant="soft",
                                size="2",
                            ),
                            width="100%",
                            align_items="center",
                            margin_bottom="4",
                        ),
                        # Layout principal: Video + Sidebar (condicional)
                        rx.hstack(
                            # Columna principal con video y controles
                            rx.vstack(
                                video_player(),
                                lesson_info(),
                                navigation_controls(),
                                spacing="4",
                                flex="1",
                            ),
                            # Sidebar con lecciones (solo si está visible)
                            rx.cond(
                                CourseViewerState.sidebar_visible,
                                lessons_sidebar(),
                            ),
                            spacing="6",
                            align_items="start",
                            width="100%",
                        ),
                        spacing="4",
                        width="100%",
                        padding_y="6",
                    ),
                ),
                spacing="4",
                width="100%",
                on_mount=CourseViewerState.load_course_viewer_from_url,
            ),
            width="100%",
            padding_x=rx.cond(
                CourseViewerState.sidebar_visible,
                "2rem",  # Con sidebar: padding normal
                "0.5rem"   # Sin sidebar: padding mínimo para más espacio
            ),
            padding_y="1rem",
        ),
        width="100%",
        spacing="0",
        align_items="center",
    )
