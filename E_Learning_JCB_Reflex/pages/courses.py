"""Página de todos los cursos."""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_state import CourseState
from E_Learning_JCB_Reflex.states.enrollment_state import EnrollmentState
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.course_card import course_card


def courses_page() -> rx.Component:
    """Página de todos los cursos."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Todos los Cursos",
                    size="8",
                    margin_bottom="4",
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
                # Cuadrícula de cursos usando course_card
                rx.cond(
                    CourseState.courses.length() > 0,
                    rx.grid(
                        rx.foreach(
                            CourseState.courses,
                            lambda course: course_card(course)
                        ),
                        columns="3",
                        spacing="6",
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
        width="100%",
        spacing="0",
    )
