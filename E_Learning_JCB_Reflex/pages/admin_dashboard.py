"""
Dashboard para administradores de la plataforma E-Learning JCB.

Este módulo proporciona el panel de control principal para usuarios
con rol de administrador. Muestra estadísticas globales de la plataforma
y proporciona acceso rápido a las herramientas de gestión.

Funcionalidades:
- Bienvenida personalizada con nombre del administrador
- Estadísticas globales (usuarios, cursos, inscripciones, ingresos)
- Desglose de usuarios por rol (estudiantes, instructores, admins)
- Información sobre cursos publicados y pendientes
- Acciones rápidas (usuarios, cursos, categorías, estadísticas, configuración)
- Protección de acceso solo para administradores
- Carga dinámica de estadísticas al montar la página

Ruta: /admin/dashboard
Acceso: Protegida (solo administradores autenticados)
Estado: AdminDashboardState (estadísticas de la plataforma)
Protección: admin_only HOC
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only
from E_Learning_JCB_Reflex.states.admin_dashboard_state import AdminDashboardState


def admin_dashboard_content() -> rx.Component:
    """
    Renderiza el contenido completo del dashboard del administrador.

    Muestra todas las secciones del dashboard organizadas verticalmente:
    1. Header con bienvenida y badge de rol "Administrador"
    2. Estadísticas globales en 4 tarjetas (usuarios, cursos, inscripciones, ingresos)
    3. Grid de 2 columnas con gestión de usuarios y cursos
    4. Sección "Acciones Rápidas" con enlaces a herramientas administrativas

    Returns:
        rx.Component: Contenido completo del dashboard del administrador

    Notas:
        - Utiliza on_mount con AdminDashboardState.load_statistics
        - Las estadísticas se cargan dinámicamente desde la base de datos
        - Incluye desglose por tipo de usuario (students, instructors, admins)
        - La tarjeta de ingresos muestra "N/A" (funcionalidad pendiente)
        - Max width de 1400px para mejor legibilidad
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            f"Bienvenido, {AdminDashboardState.user_name}",
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
                                rx.badge(AdminDashboardState.total_users.to_string(), size="2", color_scheme="blue"),
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
                                rx.badge(AdminDashboardState.total_courses.to_string(), size="2", color_scheme="purple"),
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
                                rx.badge(AdminDashboardState.total_enrollments.to_string(), size="2", color_scheme="green"),
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
                                rx.badge("N/A", size="2", color_scheme="gray"),
                            ),
                            rx.text("Ingresos Totales", size="3", weight="bold"),
                            rx.text(
                                "Funcionalidad pendiente de implementar",
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
                                        rx.text(f"{AdminDashboardState.total_students.to_string()} usuarios", size="2", color=rx.color("gray", 10)),
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
                                        rx.text(f"{AdminDashboardState.total_instructors.to_string()} usuarios", size="2", color=rx.color("gray", 10)),
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
                                        rx.text(f"{AdminDashboardState.total_admins.to_string()} usuarios", size="2", color=rx.color("gray", 10)),
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
                                        rx.text(f"{AdminDashboardState.total_courses.to_string()} cursos", size="2", color=rx.color("gray", 10)),
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
                                        rx.text("Funcionalidad pendiente", size="2", color=rx.color("gray", 10)),
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
                                        rx.text("Funcionalidad pendiente", size="2", color=rx.color("gray", 10)),
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
                on_mount=AdminDashboardState.load_statistics,
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
    )


def admin_dashboard_page() -> rx.Component:
    """
    Renderiza la página de dashboard del administrador con protección.

    Envuelve el contenido del dashboard con el HOC admin_only
    para garantizar que solo usuarios con rol "admin" puedan acceder.

    Returns:
        rx.Component: Dashboard protegido para administradores

    Notas:
        - Utiliza el HOC admin_only de components.protected
        - Si el usuario no es administrador, redirige o muestra acceso denegado
        - Esta es la función principal exportada para el routing
    """
    return admin_only(admin_dashboard_content())
