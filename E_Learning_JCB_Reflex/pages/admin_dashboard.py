"""Dashboard para administradores."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only
from E_Learning_JCB_Reflex.states.auth_state import AuthState


def admin_dashboard_content() -> rx.Component:
    """Contenido del dashboard del administrador."""
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
                            "Panel de administración",
                            size="5",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.spacer(),
                    rx.badge(
                        "Administrador",
                        color_scheme="red",
                        size="3",
                    ),
                    width="100%",
                    align_items="center",
                ),
                # Estadísticas globales
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("users", size=24, color=rx.color("blue", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Usuarios Totales", size="3", weight="bold"),
                            rx.text(
                                "Estudiantes, instructores y admins",
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
                                rx.icon("book-open", size=24, color=rx.color("purple", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Cursos Totales", size="3", weight="bold"),
                            rx.text(
                                "Cursos publicados en la plataforma",
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
                                rx.icon("user-check", size=24, color=rx.color("green", 9)),
                                rx.spacer(),
                                rx.badge("0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Inscripciones", size="3", weight="bold"),
                            rx.text(
                                "Total de inscripciones activas",
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
                                rx.icon("trending-up", size=24, color=rx.color("orange", 9)),
                                rx.spacer(),
                                rx.badge("$0", size="2", color_scheme="gray"),
                            ),
                            rx.text("Ingresos Totales", size="3", weight="bold"),
                            rx.text(
                                "Ingresos generados por la plataforma",
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
                # Gestión
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.heading("Gestión de Usuarios", size="5"),
                            rx.divider(),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("users", size=20, color=rx.color("blue", 9)),
                                    rx.vstack(
                                        rx.text("Estudiantes", size="3", weight="bold"),
                                        rx.text("0 usuarios", size="2", color=rx.color("gray", 10)),
                                        spacing="1",
                                        align_items="start",
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                                rx.hstack(
                                    rx.icon("graduation-cap", size=20, color=rx.color("purple", 9)),
                                    rx.vstack(
                                        rx.text("Instructores", size="3", weight="bold"),
                                        rx.text("0 usuarios", size="2", color=rx.color("gray", 10)),
                                        spacing="1",
                                        align_items="start",
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                                rx.hstack(
                                    rx.icon("shield", size=20, color=rx.color("red", 9)),
                                    rx.vstack(
                                        rx.text("Administradores", size="3", weight="bold"),
                                        rx.text("0 usuarios", size="2", color=rx.color("gray", 10)),
                                        spacing="1",
                                        align_items="start",
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    "Gestionar Usuarios",
                                    size="2",
                                    variant="soft",
                                    width="100%",
                                ),
                                href="/admin/users",
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.heading("Gestión de Cursos", size="5"),
                            rx.divider(),
                            rx.vstack(
                                rx.hstack(
                                    rx.icon("book-open", size=20, color=rx.color("purple", 9)),
                                    rx.vstack(
                                        rx.text("Cursos Publicados", size="3", weight="bold"),
                                        rx.text("0 cursos", size="2", color=rx.color("gray", 10)),
                                        spacing="1",
                                        align_items="start",
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                                rx.hstack(
                                    rx.icon("clock", size=20, color=rx.color("orange", 9)),
                                    rx.vstack(
                                        rx.text("Pendientes Revisión", size="3", weight="bold"),
                                        rx.text("0 cursos", size="2", color=rx.color("gray", 10)),
                                        spacing="1",
                                        align_items="start",
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                                rx.hstack(
                                    rx.icon("tag", size=20, color=rx.color("green", 9)),
                                    rx.vstack(
                                        rx.text("Categorías", size="3", weight="bold"),
                                        rx.text("0 categorías", size="2", color=rx.color("gray", 10)),
                                        spacing="1",
                                        align_items="start",
                                    ),
                                    spacing="3",
                                    width="100%",
                                ),
                                spacing="3",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    "Gestionar Cursos",
                                    size="2",
                                    variant="soft",
                                    width="100%",
                                ),
                                href="/admin/courses",
                                width="100%",
                            ),
                            spacing="4",
                            width="100%",
                        ),
                    ),
                    columns="2",
                    spacing="4",
                    width="100%",
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
                                        rx.icon("users", size=20),
                                        rx.text("Usuarios"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/admin/users",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("book-open", size=20),
                                        rx.text("Cursos"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/admin/courses",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("tag", size=20),
                                        rx.text("Categorías"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/admin/categories",
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
                                href="/admin/stats",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("settings", size=20),
                                        rx.text("Configuración"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/admin/settings",
                                width="100%",
                            ),
                            columns="5",
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


def admin_dashboard_page() -> rx.Component:
    """Página de dashboard del administrador con protección."""
    return admin_only(admin_dashboard_content())
