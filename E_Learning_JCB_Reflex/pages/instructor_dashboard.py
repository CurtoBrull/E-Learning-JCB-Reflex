"""Dashboard para instructores."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import instructor_only
from E_Learning_JCB_Reflex.states.auth_state import AuthState


def instructor_dashboard_content() -> rx.Component:
    """Contenido del dashboard del instructor."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            f"Bienvenido, {AuthState.user_name}",
                            size="9",
                        ),
                        rx.text(
                            "Panel de instructor",
                            size="5",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.spacer(),
                    rx.badge(
                        "Instructor",
                        color_scheme="purple",
                        size="3",
                    ),
                    width="100%",
                    align_items="center",
                ),
                # Estadísticas
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("graduation-cap", size=24, color=rx.color("purple", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Cursos Creados", size="3", weight="bold"),
                            rx.text(
                                "Total de cursos que has publicado",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("users", size=24, color=rx.color("blue", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Estudiantes", size="3", weight="bold"),
                            rx.text(
                                "Estudiantes inscritos en tus cursos",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("star", size=24, color=rx.color("yellow", 9)),
                                rx.spacer(),
                                rx.badge("0.0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Valoración Media", size="3", weight="bold"),
                            rx.text(
                                "Promedio de valoraciones de tus cursos",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("dollar-sign", size=24, color=rx.color("green", 9)),
                                rx.spacer(),
                                rx.badge("$0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Ingresos", size="3", weight="bold"),
                            rx.text(
                                "Ingresos generados por tus cursos",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    columns="4",
                    spacing="4",
                    width="100%",
                ),
                # Cursos recientes
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Mis Cursos", size="6"),
                            rx.spacer(),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("plus", size=18),
                                        rx.text("Crear Curso"),
                                        spacing="2",
                                    ),
                                    size="2",
                                    color_scheme="purple",
                                ),
                                href="/instructor/courses/new",
                            ),
                            width="100%",
                        ),
                        rx.divider(),
                        rx.center(
                            rx.vstack(
                                rx.icon("graduation-cap", size=40, color=rx.color("gray", 8)),
                                rx.text(
                                    "No has creado cursos todavía",
                                    size="4",
                                    color=rx.color("gray", 10),
                                ),
                                rx.text(
                                    "Comienza a compartir tu conocimiento creando tu primer curso",
                                    size="3",
                                    color=rx.color("gray", 9),
                                ),
                                rx.link(
                                    rx.button(
                                        rx.hstack(
                                            rx.icon("plus", size=18),
                                            rx.text("Crear Mi Primer Curso"),
                                            spacing="2",
                                        ),
                                        size="3",
                                        color_scheme="purple",
                                    ),
                                    href="/instructor/courses/new",
                                ),
                                spacing="3",
                                align_items="center",
                                padding="4em",
                            ),
                        ),
                        spacing="4",
                        width="100%",
                    ),
                ),
                # Acciones rápidas
                rx.card(
                    rx.vstack(
                        rx.heading("Acciones Rápidas", size="6"),
                        rx.divider(),
                        rx.grid(
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("plus", size=20),
                                        rx.text("Crear Curso"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                    color_scheme="purple",
                                ),
                                href="/instructor/courses/new",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("graduation-cap", size=20),
                                        rx.text("Mis Cursos"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/instructor/courses",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("bar-chart", size=20),
                                        rx.text("Estadísticas"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/instructor/stats",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("user", size=20),
                                        rx.text("Mi Perfil"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/profile",
                                width="100%",
                            ),
                            columns="4",
                            spacing="4",
                            width="100%",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                ),
                spacing="6",
                width="100%",
                padding_y="4",
            ),
            max_width="1400px",
        ),
        width="100%",
        spacing="0",
    )


def instructor_dashboard_page() -> rx.Component:
    """Página de dashboard del instructor con protección."""
    return instructor_only(instructor_dashboard_content())
