"""Página de detalles de un curso específico."""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_state import CourseState
from E_Learning_JCB_Reflex.components.navbar import navbar


def course_detail_page() -> rx.Component:
    """Página de detalles de un curso."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Estado de carga
                rx.cond(
                    CourseState.loading,
                    rx.center(
                        rx.spinner(size="3"),
                        height="50vh",
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
                # Contenido del curso
                rx.cond(
                    (CourseState.course_title != "") & (CourseState.loading == False),
                    rx.vstack(
                        # SECCIÓN 1: HEADER CON IMAGEN Y INFO PRINCIPAL
                        rx.box(
                            rx.hstack(
                                # Imagen del curso
                                rx.box(
                                    rx.image(
                                        src=CourseState.course_thumbnail,
                                        width="100%",
                                        height="300px",
                                        object_fit="cover",
                                        border_radius="5px",
                                    ),
                                    width="400px",
                                    flex_shrink="0",
                                ),
                                # Info principal
                                rx.vstack(
                                    rx.heading(
                                        CourseState.course_title,
                                        size="9",
                                    ),
                                    rx.text(
                                        CourseState.course_description,
                                        size="4",
                                        color="gray",
                                    ),
                                    rx.hstack(
                                        rx.badge(
                                            CourseState.course_level,
                                            color_scheme="blue",
                                            size="3",
                                        ),
                                        rx.text(
                                            f"${CourseState.course_price:.2f}",
                                            size="7",
                                            weight="bold",
                                            color="green",
                                        ),
                                        spacing="4",
                                    ),
                                    align_items="start",
                                    spacing="3",
                                    flex="1",
                                ),
                                spacing="6",
                                width="100%",
                                align_items="start",
                            ),
                            width="100%",
                            padding="6",
                            border_radius="lg",
                            bg="white",
                        ),
                        # SECCIÓN 2: INFORMACIÓN DEL INSTRUCTOR
                        rx.box(
                            rx.heading("Instructor", size="6", margin_bottom="3"),
                            rx.hstack(
                                rx.avatar(
                                    src=CourseState.instructor_avatar,
                                    fallback="IN",
                                    size="5",
                                ),
                                rx.vstack(
                                    rx.text(
                                        CourseState.instructor_name,
                                        weight="bold",
                                        size="4",
                                    ),
                                    rx.text(
                                        CourseState.instructor_email,
                                        size="2",
                                        color="gray",
                                    ),
                                    rx.cond(
                                        CourseState.instructor_bio != "",
                                        rx.text(
                                            CourseState.instructor_bio,
                                            size="2",
                                            color="gray",
                                        ),
                                    ),
                                    align_items="start",
                                    spacing="1",
                                ),
                            ),
                            width="100%",
                            padding="4",
                            margin_top="6",
                        ),
                        # SECCIÓN 3: ESTADÍSTICAS
                        rx.hstack(
                            rx.box(
                                rx.text("Estudiantes", size="2", color="gray"),
                                rx.text(
                                    CourseState.students_count,
                                    size="6",
                                    weight="bold",
                                ),
                                padding="4",
                                text_align="center",
                                flex="1",
                            ),
                            rx.cond(
                                CourseState.average_rating > 0,
                                rx.box(
                                    rx.text("Rating", size="2", color="gray"),
                                    rx.text(
                                        CourseState.average_rating,
                                        size="6",
                                        weight="bold",
                                    ),
                                    padding="4",
                                    text_align="center",
                                    flex="1",
                                ),
                            ),
                            rx.cond(
                                CourseState.total_reviews > 0,
                                rx.box(
                                    rx.text("Reviews", size="2", color="gray"),
                                    rx.text(
                                        CourseState.total_reviews,
                                        size="6",
                                        weight="bold",
                                    ),
                                    padding="4",
                                    text_align="center",
                                    flex="1",
                                ),
                            ),
                            spacing="4",
                            width="100%",
                            margin_top="4",
                        ),
                        # SECCIÓN 4: CATEGORÍAS
                        rx.cond(
                            CourseState.categories.length() > 0,
                            rx.box(
                                rx.heading("Categorías", size="6", margin_bottom="3"),
                                rx.hstack(
                                    rx.foreach(
                                        CourseState.categories,
                                        lambda cat: rx.badge(cat, color_scheme="purple"),
                                    ),
                                    spacing="2",
                                    wrap="wrap",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        # SECCIÓN 5: LECCIONES
                        rx.cond(
                            CourseState.lessons.length() > 0,
                            rx.box(
                                rx.heading("Contenido del curso", size="6", margin_bottom="3"),
                                rx.vstack(
                                    rx.foreach(
                                        CourseState.lessons,
                                        lambda lesson: rx.box(
                                            rx.hstack(
                                                rx.heading(lesson["title"], size="4"),
                                                rx.spacer(),
                                                rx.badge(
                                                    f"{lesson['duration']} min",
                                                    color_scheme="blue",
                                                ),
                                            ),
                                            rx.text(
                                                lesson["content"],
                                                size="2",
                                                color="gray",
                                                no_of_lines=2,
                                                margin_top="2",
                                            ),
                                            padding="3",
                                            width="100%",
                                            _hover={
                                                "background": rx.color("gray", 2),
                                            },
                                        ),
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        # SECCIÓN 6: REVIEWS
                        rx.cond(
                            CourseState.reviews.length() > 0,
                            rx.box(
                                rx.heading("Opiniones de estudiantes", size="6", margin_bottom="3"),
                                rx.vstack(
                                    rx.foreach(
                                        CourseState.reviews,
                                        lambda review: rx.box(
                                            rx.hstack(
                                                rx.text(review["student"], weight="bold", size="3"),
                                                rx.spacer(),
                                                rx.hstack(
                                                    rx.text("Rating:", size="2", color="gray"),
                                                    rx.text(review["rating"], size="2", weight="bold"),
                                                    rx.text("/5", size="2", color="gray"),
                                                    spacing="1",
                                                ),
                                            ),
                                            rx.text(
                                                review["comment"],
                                                size="2",
                                                color="gray",
                                                margin_top="2",
                                            ),
                                            padding="3",
                                            width="100%",
                                        ),
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        # BOTÓN DE INSCRIPCIÓN
                        rx.button(
                            "Inscribirse al curso",
                            size="4",
                            width="100%",
                            margin_top="6",
                            color_scheme="green",
                        ),
                        spacing="4",
                        width="100%",
                        padding_y="8",
                    ),
                ),
                spacing="4",
                width="100%",
                on_mount=CourseState.load_course_from_url,
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
