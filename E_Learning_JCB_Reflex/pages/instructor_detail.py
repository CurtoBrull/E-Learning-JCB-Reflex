"""Página de detalles de un instructor específico."""

import reflex as rx
from E_Learning_JCB_Reflex.states.instructor_state import InstructorState
from E_Learning_JCB_Reflex.components.navbar import navbar


def instructor_detail_page() -> rx.Component:
    """Página de detalles de un instructor."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Estado de carga
                rx.cond(
                    InstructorState.loading,
                    rx.center(
                        rx.spinner(size="3"),
                        height="50vh",
                    ),
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
                # Contenido del instructor
                rx.cond(
                    (InstructorState.instructor_name != "") & (InstructorState.loading == False),
                    rx.vstack(
                        # SECCIÓN 1: HEADER CON AVATAR E INFO PRINCIPAL
                        rx.box(
                            rx.hstack(
                                # Avatar del instructor
                                rx.box(
                                    rx.avatar(
                                        src=InstructorState.instructor_avatar,
                                        fallback="IN",
                                        size="9",
                                        radius="full",
                                    ),
                                    width="200px",
                                    flex_shrink="0",
                                    display="flex",
                                    justify_content="center",
                                    align_items="center",
                                ),
                                # Info principal
                                rx.vstack(
                                    rx.heading(
                                        InstructorState.instructor_name,
                                        size="9",
                                    ),
                                    rx.cond(
                                        InstructorState.instructor_expertise != "",
                                        rx.badge(
                                            InstructorState.instructor_expertise,
                                            color_scheme="purple",
                                            size="3",
                                        ),
                                    ),
                                    rx.text(
                                        InstructorState.instructor_email,
                                        size="3",
                                        color="gray",
                                    ),
                                    rx.cond(
                                        InstructorState.instructor_bio != "",
                                        rx.text(
                                            InstructorState.instructor_bio,
                                            size="4",
                                            margin_top="4",
                                        ),
                                    ),
                                    align_items="start",
                                    spacing="3",
                                    flex="1",
                                ),
                                spacing="6",
                                width="100%",
                                align_items="center",
                            ),
                            width="100%",
                            padding="6",
                            border_radius="5px",
                            bg="white",
                        ),
                        # SECCIÓN 2: ESTADÍSTICAS
                        rx.hstack(
                            rx.box(
                                rx.text("Cursos", size="2", color="gray"),
                                rx.text(
                                    InstructorState.total_courses,
                                    size="6",
                                    weight="bold",
                                ),
                                padding="4",
                                text_align="center",
                                flex="1",
                            ),
                            rx.box(
                                rx.text("Estudiantes", size="2", color="gray"),
                                rx.text(
                                    InstructorState.total_students,
                                    size="6",
                                    weight="bold",
                                ),
                                padding="4",
                                text_align="center",
                                flex="1",
                            ),
                            spacing="4",
                            width="100%",
                            margin_top="4",
                        ),
                        # SECCIÓN 3: CURSOS DEL INSTRUCTOR
                        rx.cond(
                            InstructorState.courses.length() > 0,
                            rx.box(
                                rx.heading("Cursos impartidos", size="6", margin_bottom="3"),
                                rx.grid(
                                    rx.foreach(
                                        InstructorState.courses,
                                        lambda course: rx.link(
                                            rx.box(
                                                rx.vstack(
                                                    rx.image(
                                                        src=course["thumbnail"],
                                                        height="150px",
                                                        width="100%",
                                                        object_fit="cover",
                                                        border_radius="5px 5px 0 0",
                                                    ),
                                                    rx.vstack(
                                                        rx.heading(
                                                            course["title"],
                                                            size="4",
                                                        ),
                                                        rx.text(
                                                            course["description"],
                                                            size="2",
                                                            color="gray",
                                                            no_of_lines=2,
                                                        ),
                                                        rx.hstack(
                                                            rx.badge(
                                                                course["level"],
                                                                color_scheme="blue",
                                                            ),
                                                            rx.spacer(),
                                                            rx.text(
                                                                f"${course['price']:.2f}",
                                                                weight="bold",
                                                                color="green",
                                                            ),
                                                            width="100%",
                                                        ),
                                                        rx.hstack(
                                                            rx.text(
                                                                f"{course['students_count']} estudiantes",
                                                                size="1",
                                                                color="gray",
                                                            ),
                                                            rx.text(
                                                                f"★ {course['average_rating']}/5",
                                                                size="1",
                                                                color="orange",
                                                            ),
                                                            spacing="2",
                                                        ),
                                                        spacing="2",
                                                        padding="3",
                                                        align_items="start",
                                                        width="100%",
                                                    ),
                                                    spacing="0",
                                                    width="100%",
                                                ),
                                                border_radius="5px",
                                                box_shadow="3px 3px 10px rgba(0, 0, 0, 0.3)",
                                                overflow="hidden",
                                                _hover={
                                                    "box_shadow": "5px 5px 15px rgba(0, 0, 0, 0.5)",
                                                    "transform": "translateY(-2px)",
                                                },
                                                transition="all 0.2s",
                                            ),
                                            href=f"/courses/{course['id']}",
                                            text_decoration="none",
                                            color="inherit",
                                        ),
                                    ),
                                    columns="3",
                                    spacing="4",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        spacing="4",
                        width="100%",
                        padding_y="8",
                    ),
                ),
                spacing="4",
                width="100%",
                on_mount=InstructorState.load_instructor_from_url,
            ),
            width="100%",
            max_width="1200px",
            padding_x="2rem",
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
        align_items="center",
    )
