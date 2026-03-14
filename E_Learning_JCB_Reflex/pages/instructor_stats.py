"""
Página de estadísticas para instructores.

Muestra métricas visuales del rendimiento del instructor:
- KPIs principales (alumnos, ingresos, cursos, valoración)
- Distribución de niveles y categorías
- Progreso de alumnos por curso
- Actividad reciente

Ruta: /instructor/stats
Acceso: Protegida (solo instructores autenticados)
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer
from E_Learning_JCB_Reflex.components.protected import instructor_only
from E_Learning_JCB_Reflex.states.auth_state import AuthState


# ---------------------------------------------------------------------------
# Helpers de UI
# ---------------------------------------------------------------------------

def kpi_card(
    icon: str,
    label: str,
    value: str,
    subtitle: str,
    color: str,
    trend: str = "",
    trend_up: bool = True,
) -> rx.Component:
    """Tarjeta de KPI con icono, valor destacado y tendencia."""
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=22, color="white"),
                    background=rx.color(color, 9),
                    padding="0.6em",
                    border_radius="10px",
                ),
                rx.spacer(),
                rx.cond(
                    trend != "",
                    rx.badge(
                        rx.hstack(
                            rx.icon(
                                "trending-up" if trend_up else "trending-down",
                                size=12,
                            ),
                            rx.text(trend, size="1"),
                            spacing="1",
                        ),
                        color_scheme="green" if trend_up else "red",
                        variant="soft",
                        size="1",
                    ),
                ),
                width="100%",
                align_items="start",
            ),
            rx.text(value, size="8", weight="bold", color=rx.color(color, 11)),
            rx.text(label, size="3", weight="medium"),
            rx.text(subtitle, size="1", color=rx.color("gray", 10)),
            spacing="1",
            align_items="start",
            width="100%",
        ),
        width="100%",
    )


def progress_row(label: str, value: int, total: int, color: str) -> rx.Component:
    """Fila con barra de progreso para distribución."""
    pct = int((value / total) * 100) if total > 0 else 0
    return rx.vstack(
        rx.hstack(
            rx.text(label, size="2", weight="medium"),
            rx.spacer(),
            rx.text(f"{value} alumnos ({pct}%)", size="2", color=rx.color("gray", 10)),
            width="100%",
        ),
        rx.progress(value=pct, color_scheme=color, size="2", width="100%"),
        spacing="1",
        width="100%",
    )


def course_stat_row(
    title: str,
    students: int,
    completion: int,
    revenue: str,
    rating: str,
) -> rx.Component:
    """Fila de estadísticas por curso."""
    return rx.table.row(
        rx.table.cell(
            rx.text(title, size="2", weight="medium"),
            max_width="200px",
        ),
        rx.table.cell(
            rx.badge(f"{students}", color_scheme="blue", variant="soft"),
        ),
        rx.table.cell(
            rx.hstack(
                rx.progress(
                    value=completion,
                    color_scheme="purple",
                    size="1",
                    width="80px",
                ),
                rx.text(f"{completion}%", size="1", color=rx.color("gray", 10)),
                spacing="2",
                align_items="center",
            ),
        ),
        rx.table.cell(
            rx.text(revenue, size="2", color=rx.color("green", 10), weight="medium"),
        ),
        rx.table.cell(
            rx.hstack(
                rx.icon("star", size=13, color=rx.color("yellow", 9)),
                rx.text(rating, size="2"),
                spacing="1",
                align_items="center",
            ),
        ),
    )


def activity_item(
    icon: str,
    color: str,
    text: str,
    time: str,
) -> rx.Component:
    """Elemento de actividad reciente."""
    return rx.hstack(
        rx.box(
            rx.icon(icon, size=15, color="white"),
            background=rx.color(color, 9),
            padding="0.4em",
            border_radius="8px",
            flex_shrink="0",
        ),
        rx.vstack(
            rx.text(text, size="2"),
            rx.text(time, size="1", color=rx.color("gray", 10)),
            spacing="0",
            align_items="start",
        ),
        spacing="3",
        align_items="start",
        width="100%",
    )


def month_bar(month: str, height: int, value: str, color: str) -> rx.Component:
    """Barra de un gráfico de barras manual."""
    return rx.vstack(
        rx.tooltip(
            rx.box(
                width="32px",
                height=f"{height}px",
                background=rx.color(color, 8),
                border_radius="6px 6px 0 0",
                _hover={"background": rx.color(color, 10)},
                transition="background 0.2s",
                cursor="pointer",
            ),
            content=f"{value}",
        ),
        rx.text(month, size="1", color=rx.color("gray", 10)),
        spacing="1",
        align_items="center",
    )


def donut_segment(label: str, pct: int, color: str) -> rx.Component:
    """Leyenda de segmento para el 'donut' visual."""
    return rx.hstack(
        rx.box(
            width="12px",
            height="12px",
            background=rx.color(color, 9),
            border_radius="3px",
            flex_shrink="0",
        ),
        rx.text(label, size="2"),
        rx.spacer(),
        rx.text(f"{pct}%", size="2", weight="bold", color=rx.color(color, 10)),
        width="100%",
        spacing="2",
        align_items="center",
    )


# ---------------------------------------------------------------------------
# Secciones
# ---------------------------------------------------------------------------

def kpis_section() -> rx.Component:
    return rx.grid(
        kpi_card("users", "Total Alumnos", "248", "En todos tus cursos", "blue", "+12% este mes"),
        kpi_card("euro", "Ingresos Totales", "€8.420", "Acumulado del año", "green", "+8% este mes"),
        kpi_card("graduation-cap", "Cursos Activos", "4", "Publicados en la plataforma", "purple", "+1 este mes"),
        kpi_card("star", "Valoración Media", "4.7", "Basado en 183 reseñas", "yellow", "+0.2 este mes"),
        columns=rx.breakpoints(initial="1", sm="2", lg="4"),
        spacing="4",
        width="100%",
    )


def revenue_chart_section() -> rx.Component:
    """Gráfico de barras de ingresos mensuales."""
    bars = [
        ("Ene", 60, "€620", "purple"),
        ("Feb", 75, "€780", "purple"),
        ("Mar", 55, "€570", "purple"),
        ("Abr", 90, "€930", "purple"),
        ("May", 70, "€720", "purple"),
        ("Jun", 110, "€1.140", "purple"),
        ("Jul", 85, "€880", "purple"),
        ("Ago", 65, "€670", "purple"),
        ("Sep", 120, "€1.250", "purple"),
        ("Oct", 100, "€1.040", "purple"),
        ("Nov", 95, "€980", "purple"),
        ("Dic", 130, "€1.350", "purple"),
    ]
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.vstack(
                    rx.heading("Ingresos por Mes", size="5"),
                    rx.text("Año 2025", size="2", color=rx.color("gray", 10)),
                    spacing="0",
                    align_items="start",
                ),
                rx.spacer(),
                rx.badge("€8.930 total", color_scheme="green", size="2"),
                width="100%",
                align_items="start",
            ),
            rx.hstack(
                *[
                    month_bar(month, height, value, color)
                    for month, height, value, color in bars
                ],
                spacing="2",
                align_items="end",
                height="160px",
                width="100%",
                padding_top="1em",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def distribution_section() -> rx.Component:
    """Distribución por nivel y categoría."""
    return rx.grid(
        # Por nivel
        rx.card(
            rx.vstack(
                rx.heading("Alumnos por Nivel", size="5"),
                rx.text(
                    "Distribución de 248 alumnos",
                    size="2",
                    color=rx.color("gray", 10),
                ),
                rx.divider(),
                progress_row("Principiante", 112, 248, "green"),
                progress_row("Intermedio", 98, 248, "orange"),
                progress_row("Avanzado", 38, 248, "red"),
                spacing="3",
                width="100%",
            ),
            width="100%",
        ),
        # Por categoría
        rx.card(
            rx.vstack(
                rx.heading("Distribución por Categoría", size="5"),
                rx.text(
                    "Porcentaje de matriculaciones",
                    size="2",
                    color=rx.color("gray", 10),
                ),
                rx.divider(),
                donut_segment("Inteligencia Artificial", 38, "purple"),
                donut_segment("Programación Web", 27, "blue"),
                donut_segment("Bases de Datos", 20, "green"),
                donut_segment("DevOps", 15, "orange"),
                rx.divider(),
                rx.center(
                    rx.vstack(
                        rx.box(
                            rx.vstack(
                                rx.text("248", size="7", weight="bold"),
                                rx.text("alumnos", size="2", color=rx.color("gray", 10)),
                                spacing="0",
                                align_items="center",
                            ),
                            background=rx.color("purple", 3),
                            border_radius="50%",
                            width="110px",
                            height="110px",
                            display="flex",
                            align_items="center",
                            justify_content="center",
                            border=f"8px solid {rx.color('purple', 8)}",
                        ),
                        align_items="center",
                    ),
                    padding_y="0.5em",
                ),
                spacing="3",
                width="100%",
            ),
            width="100%",
        ),
        columns="2",
        spacing="4",
        width="100%",
    )


def courses_table_section() -> rx.Component:
    """Tabla de rendimiento por curso."""
    return rx.card(
        rx.vstack(
            rx.heading("Rendimiento por Curso", size="5"),
            rx.text(
                "Métricas individuales de cada curso publicado",
                size="2",
                color=rx.color("gray", 10),
            ),
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("Curso"),
                        rx.table.column_header_cell("Alumnos"),
                        rx.table.column_header_cell("Completado"),
                        rx.table.column_header_cell("Ingresos"),
                        rx.table.column_header_cell("Valoración"),
                    ),
                ),
                rx.table.body(
                    course_stat_row("Introducción a la IA", 94, 72, "€3.567", "4.8"),
                    course_stat_row("Python Avanzado", 67, 58, "€2.010", "4.6"),
                    course_stat_row("MongoDB para Devs", 52, 45, "€1.560", "4.7"),
                    course_stat_row("DevOps con Docker", 35, 31, "€1.283", "4.5"),
                ),
                width="100%",
                variant="surface",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def activity_section() -> rx.Component:
    """Actividad reciente y logros."""
    return rx.grid(
        # Actividad reciente
        rx.card(
            rx.vstack(
                rx.heading("Actividad Reciente", size="5"),
                rx.divider(),
                activity_item("user-plus", "blue", "Ana López se inscribió en Introducción a la IA", "Hace 2 horas"),
                activity_item("star", "yellow", "Carlos M. dejó una reseña de 5 estrellas", "Hace 5 horas"),
                activity_item("message-square", "purple", "Nueva pregunta en Python Avanzado", "Hace 1 día"),
                activity_item("user-plus", "blue", "3 nuevos alumnos en MongoDB para Devs", "Hace 2 días"),
                activity_item("check-circle", "green", "Pedro R. completó DevOps con Docker", "Hace 3 días"),
                activity_item("star", "yellow", "Nuevo comentario en Python Avanzado", "Hace 4 días"),
                spacing="4",
                width="100%",
            ),
            width="100%",
        ),
        # Logros
        rx.card(
            rx.vstack(
                rx.heading("Logros y Hitos", size="5"),
                rx.divider(),
                rx.vstack(
                    rx.hstack(
                        rx.box(
                            rx.icon("trophy", size=20, color=rx.color("yellow", 9)),
                            background=rx.color("yellow", 3),
                            padding="0.6em",
                            border_radius="10px",
                        ),
                        rx.vstack(
                            rx.text("Instructor Destacado", size="2", weight="bold"),
                            rx.text("Top 10% de instructores de la plataforma", size="1", color=rx.color("gray", 10)),
                            spacing="0",
                            align_items="start",
                        ),
                        spacing="3",
                        align_items="center",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.icon("users", size=20, color=rx.color("blue", 9)),
                            background=rx.color("blue", 3),
                            padding="0.6em",
                            border_radius="10px",
                        ),
                        rx.vstack(
                            rx.text("200+ Alumnos", size="2", weight="bold"),
                            rx.text("Alcanzaste 200 matriculaciones totales", size="1", color=rx.color("gray", 10)),
                            spacing="0",
                            align_items="start",
                        ),
                        spacing="3",
                        align_items="center",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.icon("heart", size=20, color=rx.color("red", 9)),
                            background=rx.color("red", 3),
                            padding="0.6em",
                            border_radius="10px",
                        ),
                        rx.vstack(
                            rx.text("Valoración Excelente", size="2", weight="bold"),
                            rx.text("Mantienes una media de 4.7 o superior", size="1", color=rx.color("gray", 10)),
                            spacing="0",
                            align_items="start",
                        ),
                        spacing="3",
                        align_items="center",
                        width="100%",
                    ),
                    rx.hstack(
                        rx.box(
                            rx.icon("zap", size=20, color=rx.color("purple", 9)),
                            background=rx.color("purple", 3),
                            padding="0.6em",
                            border_radius="10px",
                        ),
                        rx.vstack(
                            rx.text("Creador Prolífico", size="2", weight="bold"),
                            rx.text("4 cursos publicados activos", size="1", color=rx.color("gray", 10)),
                            spacing="0",
                            align_items="start",
                        ),
                        spacing="3",
                        align_items="center",
                        width="100%",
                    ),
                    rx.divider(),
                    rx.vstack(
                        rx.text("Próximo hito", size="2", weight="bold", color=rx.color("gray", 11)),
                        rx.hstack(
                            rx.icon("target", size=14, color=rx.color("purple", 9)),
                            rx.text("52 alumnos más para llegar a 300", size="2", color=rx.color("gray", 10)),
                            spacing="2",
                        ),
                        rx.progress(value=79, color_scheme="purple", size="2", width="100%"),
                        spacing="2",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                ),
                spacing="4",
                width="100%",
            ),
            width="100%",
        ),
        columns=rx.breakpoints(initial="1", md="2"),
        spacing="4",
        width="100%",
    )


# ---------------------------------------------------------------------------
# Página principal
# ---------------------------------------------------------------------------

def instructor_stats_content() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading("Estadísticas", size="8"),
                        rx.text(
                            "Rendimiento general de tu actividad como instructor",
                            size="4",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="1",
                    ),
                    rx.spacer(),
                    rx.badge(
                        rx.hstack(
                            rx.icon("calendar", size=14),
                            rx.text("Año 2025"),
                            spacing="1",
                        ),
                        color_scheme="purple",
                        size="2",
                        variant="soft",
                    ),
                    width="100%",
                    align_items="center",
                ),
                rx.divider(),
                # Secciones
                kpis_section(),
                revenue_chart_section(),
                distribution_section(),
                courses_table_section(),
                activity_section(),
                spacing="6",
                width="100%",
                padding_y="6",
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        footer(),
        width="100%",
        spacing="0",
    )


def instructor_stats_page() -> rx.Component:
    return instructor_only(instructor_stats_content())
