"""Componente de tarjeta de curso."""

import reflex as rx


def course_card(course: dict) -> rx.Component:
    """Componente de tarjeta de curso."""
    return rx.link(
        rx.box(
            rx.vstack(
                rx.box(
                    rx.image(
                        src=course.get("thumbnail", "/placeholder-course.jpg"),
                        alt=course.get("title", "Course Thumbnail"),
                        height="200px",
                        border_radius="15px 50px",
                        border="2px solid #555",
                        object_fit="contain",
                        box_shadow="0 10px 25px rgba(255, 140, 0, 0.2), 0 5px 10px rgba(0, 0, 0, 0.15)"
                    ),
                    width="100%",
                    overflow="hidden",
                    margin_bottom="3",
                    padding_top="12px",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                ),
                rx.heading(
                    course.get("title", "Untitled Course"),
                    size="6",
                    padding_x="4px",
                    text_align="center",
                    min_height="4.5rem",
                    width="100%",
                ),
                rx.text(
                    course.get("description", "No description"),
                    color="gray",
                    size="2",
                    no_of_lines=3,
                    padding_x="4px",
                    min_height="4.5rem",
                    width="100%",
                ),
                rx.hstack(
                    rx.badge(
                        course.get("level", "beginner"), color_scheme="blue", margin="4px"
                    ),
                    rx.spacer(),
                    rx.text(
                        f"${course.get('price', 0):.2f}",
                        font_weight="bold",
                        size="4",
                        color="green",
                        padding_x="4px",
                    ),
                    width="100%",
                ),
                rx.text(
                    f"Instructor: {course.get('instructor_name', 'Unknown')}",
                    color="gray",
                    size="1",
                    padding="4px",
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
            border_radius="5px",
            box_shadow="5px 5px 15px rgba(0, 0, 0, 0.5)",
            overflow="hidden",
            transition_property="box-shadow, border-color, transform",
            transition_duration="200ms",
            transition_timing_function="ease-in-out",
            _hover={
                "box_shadow": "6px 6px 20px rgba(0, 0, 0, 0.5)",
                "transform": "translateY(-4px)",
                "cursor": "pointer",
            },
        ),
        href=f"/courses/{course.get('id', '')}",
        text_decoration="none",
        color="inherit",
        _hover={"text_decoration": "none"},
    )
