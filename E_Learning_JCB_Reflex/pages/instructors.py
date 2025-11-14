"""Página de todos los instructores."""

import reflex as rx
from E_Learning_JCB_Reflex.states.instructor_state import InstructorState
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.instructor_card import instructor_card


def instructors_page() -> rx.Component:
    """Página de todos los instructores."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                rx.heading(
                    "Nuestros Instructores",
                    size="8",
                    margin_bottom="4",
                    text_align="center",
                ),
                # Mensaje de error
                rx.cond(
                    InstructorState.error != "",
                    rx.callout(
                        InstructorState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Estado de carga
                rx.cond(
                    InstructorState.loading,
                    rx.spinner(size="3"),
                ),
                # Cuadrícula de instructores usando instructor_card
                rx.cond(
                    InstructorState.instructors.length() > 0,
                    rx.grid(
                        rx.foreach(
                            InstructorState.instructors,
                            lambda instructor: instructor_card(instructor)
                        ),
                        columns="4",
                        spacing="6",
                    ),
                ),
                spacing="4",
                width="100%",
                padding_y="8",
                align_items="center",
                on_mount=InstructorState.load_instructors,
            ),
            width="100%",
            max_width="100%",
            padding_x="2rem",
        ),
        width="100%",
        spacing="0",
    )
