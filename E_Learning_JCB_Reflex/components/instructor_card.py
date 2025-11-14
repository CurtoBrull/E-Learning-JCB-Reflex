"""Componente de tarjeta de instructor."""

import reflex as rx


def instructor_card(instructor: dict) -> rx.Component:
    """Componente de tarjeta de instructor."""
    return rx.link(
        rx.box(
            rx.vstack(
                # Avatar del instructor
                rx.box(
                    rx.avatar(
                        src=instructor.get("avatar", ""),
                        fallback="IN",
                        size="9",
                        radius="full",
                    ),
                    width="100%",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    padding_top="4",
                    padding_bottom="4",
                ),
                # Nombre del instructor
                rx.heading(
                    instructor.get("name", "Instructor"),
                    size="6",
                    padding_x="4px",
                    text_align="center",
                    width="100%",
                ),
                # Expertise
                rx.cond(
                    instructor.get("expertise", "") != "",
                    rx.badge(
                        instructor.get("expertise", ""),
                        color_scheme="purple",
                        size="2",
                    ),
                ),
                # Bio
                rx.text(
                    instructor.get("bio", "Sin biografía disponible"),
                    color="gray",
                    size="2",
                    no_of_lines=3,
                    padding_x="4px",
                    min_height="4.5rem",
                    width="100%",
                    text_align="center",
                ),
                # Estadísticas
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            instructor.get("total_courses", 0),
                            font_weight="bold",
                            size="4",
                        ),
                        rx.text(
                            "Cursos",
                            size="1",
                            color="gray",
                        ),
                        spacing="0",
                        align_items="center",
                    ),
                    width="100%",
                    justify_content="center",
                    padding="3",
                ),
                spacing="3",
                align_items="center",
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
            padding="4",
        ),
        href=f"/instructors/{instructor.get('id', '')}",
        text_decoration="none",
        color="inherit",
        _hover={"text_decoration": "none"},
    )
