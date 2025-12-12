"""Dashboard para estudiantes."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import student_only
from E_Learning_JCB_Reflex.states.auth_state import AuthState


def student_dashboard_content() -> rx.Component:
    """Contenido del dashboard del estudiante."""
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
                            "Panel de estudiante",
                            size="5",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.spacer(),
                    rx.badge(
                        "Estudiante",
                        color_scheme="blue",
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
                                rx.icon("book-open", size=24, color=rx.color("blue", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Cursos Inscritos", size="3", weight="bold"),
                            rx.text(
                                "Total de cursos en los que estás inscrito",
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
                                rx.icon("check-circle", size=24, color=rx.color("green", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Cursos Completados", size="3", weight="bold"),
                            rx.text(
                                "Cursos que has terminado exitosamente",
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
                                rx.icon("clock", size=24, color=rx.color("orange", 9)),
                                rx.spacer(),
                                rx.badge("0%", size="2", color_scheme="gray"),
                            ),
                            rx.text("Progreso General", size="3", weight="bold"),
                            rx.text(
                                "Promedio de progreso en todos tus cursos",
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
                                rx.icon("trophy", size=24, color=rx.color("yellow", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Certificados", size="3", weight="bold"),
                            rx.text(
                                "Certificados obtenidos",
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
                                    "Ver Todos",
                                    variant="soft",
                                    size="2",
                                ),
                                href="/student/enrollments",
                            ),
                            width="100%",
                        ),
                        rx.divider(),
                        rx.center(
                            rx.vstack(
                                rx.icon("book-open", size=40, color=rx.color("gray", 8)),
                                rx.text(
                                    "No tienes cursos inscritos",
                                    size="4",
                                    color=rx.color("gray", 10),
                                ),
                                rx.text(
                                    "Explora nuestro catálogo y comienza a aprender",
                                    size="3",
                                    color=rx.color("gray", 9),
                                ),
                                rx.link(
                                    rx.button(
                                        "Explorar Cursos",
                                        size="3",
                                        color_scheme="blue",
                                    ),
                                    href="/courses",
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
                                        rx.icon("search", size=20),
                                        rx.text("Explorar Cursos"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/courses",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("book-open", size=20),
                                        rx.text("Mis Inscripciones"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/student/enrollments",
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
                            columns="3",
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


def student_dashboard_page() -> rx.Component:
    """Página de dashboard del estudiante con protección."""
    return student_only(student_dashboard_content())
