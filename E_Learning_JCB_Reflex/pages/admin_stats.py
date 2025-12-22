"""
Página de estadísticas avanzadas para administradores de la plataforma E-Learning JCB.

Este módulo proporciona visualizaciones y métricas detalladas sobre el uso
y rendimiento de la plataforma educativa.

Funcionalidades:
- Gráficos de crecimiento de usuarios (diario, semanal, mensual)
- Estadísticas de inscripciones por curso
- Cursos más populares y mejor valorados
- Tasa de finalización de cursos
- Actividad de instructores
- Ingresos y tendencias financieras
- Métricas de engagement de usuarios
- Exportación de reportes
- Protección de acceso solo para administradores

Ruta: /admin/stats
Acceso: Protegida (solo administradores autenticados)
Protección: admin_only HOC
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only


def admin_stats_content() -> rx.Component:
    """
    Renderiza el contenido de la página de estadísticas avanzadas.

    Muestra paneles con gráficos, métricas y análisis detallados del
    rendimiento de la plataforma.

    Returns:
        rx.Component: Contenido completo de estadísticas avanzadas

    Notas:
        - Por ahora muestra un mensaje de funcionalidad en desarrollo
        - Se implementará con gráficos usando recharts o similar
        - Incluirá filtros por fecha y exportación de datos
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            "Estadísticas Avanzadas",
                            size="9",
                        ),
                        rx.text(
                            "Análisis detallado del rendimiento de la plataforma",
                            size="5",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("download", size=20),
                            rx.text("Exportar Reporte"),
                            spacing="2",
                        ),
                        size="3",
                        variant="soft",
                        disabled=True,
                    ),
                    width="100%",
                    align_items="center",
                ),

                # Contenido principal
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("bar-chart", size=24, color=rx.color("purple", 9)),
                            rx.heading("Funcionalidad en Desarrollo", size="6"),
                            spacing="3",
                        ),
                        rx.divider(),
                        rx.vstack(
                            rx.text(
                                "El módulo de estadísticas avanzadas está actualmente en desarrollo.",
                                size="4",
                            ),
                            rx.text(
                                "Próximamente podrás visualizar:",
                                size="3",
                                weight="bold",
                                margin_top="4",
                            ),
                            rx.grid(
                                rx.card(
                                    rx.vstack(
                                        rx.icon("trending-up", size=20, color=rx.color("blue", 9)),
                                        rx.text("Crecimiento de Usuarios", size="3", weight="bold"),
                                        rx.text("Gráficos de nuevos registros diarios, semanales y mensuales", size="2", color=rx.color("gray", 10)),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("users", size=20, color=rx.color("green", 9)),
                                        rx.text("Engagement de Usuarios", size="3", weight="bold"),
                                        rx.text("Usuarios activos, tasa de retención y tiempo promedio en plataforma", size="2", color=rx.color("gray", 10)),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("book-open", size=20, color=rx.color("purple", 9)),
                                        rx.text("Rendimiento de Cursos", size="3", weight="bold"),
                                        rx.text("Cursos más populares, tasa de finalización y valoraciones", size="2", color=rx.color("gray", 10)),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("dollar-sign", size=20, color=rx.color("orange", 9)),
                                        rx.text("Análisis Financiero", size="3", weight="bold"),
                                        rx.text("Ingresos mensuales, proyecciones y tendencias de ventas", size="2", color=rx.color("gray", 10)),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("graduation-cap", size=20, color=rx.color("pink", 9)),
                                        rx.text("Actividad de Instructores", size="3", weight="bold"),
                                        rx.text("Cursos creados, estudiantes alcanzados y valoraciones promedio", size="2", color=rx.color("gray", 10)),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("clock", size=20, color=rx.color("red", 9)),
                                        rx.text("Patrones de Uso", size="3", weight="bold"),
                                        rx.text("Horarios pico, días más activos y duración promedio de sesiones", size="2", color=rx.color("gray", 10)),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                columns="2",
                                spacing="4",
                                width="100%",
                            ),
                            rx.text(
                                "Mientras tanto, las estadísticas básicas están disponibles en el dashboard principal.",
                                size="3",
                                color=rx.color("gray", 11),
                                margin_top="4",
                            ),
                            align_items="start",
                            spacing="3",
                        ),
                        rx.divider(),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("arrow-left", size=18),
                                    rx.text("Volver al Dashboard"),
                                    spacing="2",
                                ),
                                variant="soft",
                                size="2",
                            ),
                            href="/admin/dashboard",
                        ),
                        spacing="4",
                        width="100%",
                        align_items="start",
                    ),
                ),

                spacing="6",
                width="100%",
                padding_y="4",
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
    )


def admin_stats_page() -> rx.Component:
    """
    Renderiza la página de estadísticas avanzadas con protección.

    Envuelve el contenido con el HOC admin_only para garantizar
    que solo usuarios con rol "admin" puedan acceder.

    Returns:
        rx.Component: Página protegida de estadísticas avanzadas

    Notas:
        - Utiliza el HOC admin_only de components.protected
        - Si el usuario no es administrador, redirige o muestra acceso denegado
        - Esta es la función principal exportada para el routing
    """
    return admin_only(admin_stats_content())
