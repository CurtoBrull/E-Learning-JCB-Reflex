"""Página de gestión de cursos para administradores."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only
from E_Learning_JCB_Reflex.states.course_management_state import CourseManagementState


def get_level_badge(level: str) -> rx.Component:
    """Obtener badge de nivel con color."""
    level_colors = {
        "beginner": "green",
        "intermediate": "orange",
        "advanced": "red",
    }
    level_labels = {
        "beginner": "Principiante",
        "intermediate": "Intermedio",
        "advanced": "Avanzado",
    }
    return rx.badge(
        level_labels.get(level, level),
        color_scheme=level_colors.get(level, "gray"),
        size="1",
    )


def course_dialog() -> rx.Component:
    """Diálogo para crear/editar curso."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.cond(
                    CourseManagementState.dialog_mode == "create",
                    "Crear Nuevo Curso",
                    "Editar Curso",
                )
            ),
            rx.dialog.description(
                "Completa la información del curso",
                size="2",
                mb="4",
            ),
            rx.flex(
                rx.vstack(
                    rx.text("Título", size="2", weight="bold"),
                    rx.input(
                        value=CourseManagementState.course_title,
                        on_change=CourseManagementState.set_course_title,
                        placeholder="Nombre del curso",
                    ),
                    rx.text("Descripción", size="2", weight="bold"),
                    rx.text_area(
                        value=CourseManagementState.course_description,
                        on_change=CourseManagementState.set_course_description,
                        placeholder="Descripción del curso",
                        rows="4",
                    ),
                    rx.hstack(
                        rx.vstack(
                            rx.text("Precio (€)", size="2", weight="bold"),
                            rx.input(
                                value=CourseManagementState.course_price,
                                on_change=CourseManagementState.set_course_price,
                                placeholder="0.00",
                                type="number",
                            ),
                            width="50%",
                            align_items="start",
                        ),
                        rx.vstack(
                            rx.text("Nivel", size="2", weight="bold"),
                            rx.select(
                                ["beginner", "intermediate", "advanced"],
                                value=CourseManagementState.course_level,
                                on_change=CourseManagementState.set_course_level,
                            ),
                            width="50%",
                            align_items="start",
                        ),
                        width="100%",
                    ),
                    rx.text("Categoría", size="2", weight="bold"),
                    rx.input(
                        value=CourseManagementState.course_category,
                        on_change=CourseManagementState.set_course_category,
                        placeholder="Programación, Diseño, Marketing...",
                    ),
                    rx.text("URL de Imagen", size="2", weight="bold"),
                    rx.input(
                        value=CourseManagementState.course_image,
                        on_change=CourseManagementState.set_course_image,
                        placeholder="/placeholder-course.jpg",
                    ),
                    rx.divider(),
                    rx.text("Información del Instructor", size="3", weight="bold"),
                    rx.text("Nombre del Instructor", size="2", weight="bold"),
                    rx.input(
                        value=CourseManagementState.course_instructor_name,
                        on_change=CourseManagementState.set_course_instructor_name,
                        placeholder="Nombre completo",
                    ),
                    rx.text("Email del Instructor", size="2", weight="bold"),
                    rx.input(
                        value=CourseManagementState.course_instructor_email,
                        on_change=CourseManagementState.set_course_instructor_email,
                        placeholder="email@ejemplo.com",
                        type="email",
                    ),
                    spacing="3",
                    width="100%",
                ),
                direction="column",
                spacing="3",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.dialog.close(
                    rx.button(
                        rx.cond(
                            CourseManagementState.dialog_mode == "create",
                            "Crear Curso",
                            "Guardar Cambios",
                        ),
                        on_click=CourseManagementState.save_course,
                    ),
                ),
                spacing="3",
                mt="4",
                justify="end",
            ),
            style={"max_width": 600},
        ),
        open=CourseManagementState.show_course_dialog,
        on_open_change=CourseManagementState.close_course_dialog,
    )


def delete_confirmation_dialog() -> rx.Component:
    """Diálogo de confirmación para eliminar curso."""
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirmar Eliminación"),
            rx.alert_dialog.description(
                f"¿Estás seguro que deseas eliminar el curso '{CourseManagementState.course_to_delete_title}'? Esta acción no se puede deshacer."
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button("Cancelar", variant="soft", color_scheme="gray"),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Eliminar",
                        color_scheme="red",
                        on_click=CourseManagementState.confirm_delete_course,
                    ),
                ),
                spacing="3",
                mt="4",
                justify="end",
            ),
        ),
        open=CourseManagementState.show_delete_dialog,
    )


def courses_table() -> rx.Component:
    """Tabla de cursos."""
    return rx.card(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Título"),
                    rx.table.column_header_cell("Categoría"),
                    rx.table.column_header_cell("Nivel"),
                    rx.table.column_header_cell("Precio"),
                    rx.table.column_header_cell("Estudiantes"),
                    rx.table.column_header_cell("Acciones"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    CourseManagementState.filtered_courses,
                    lambda course: rx.table.row(
                        rx.table.cell(course["title"], font_weight="medium"),
                        rx.table.cell(course["category"]),
                        rx.table.cell(get_level_badge(course["level"])),
                        rx.table.cell(f"€{course['price']}"),
                        rx.table.cell(course["studentsEnrolled"]),
                        rx.table.cell(
                            rx.hstack(
                                rx.button(
                                    rx.icon("pencil", size=16),
                                    size="2",
                                    variant="soft",
                                    color_scheme="blue",
                                    on_click=lambda _, course_id=course["_id"], title=course["title"], description=course["description"], price=course["price"], level=course["level"], category=course["category"], image=course["image"], instructor_name=course["instructorName"], instructor_email=course["instructorEmail"]: CourseManagementState.open_edit_course_dialog(
                                        course_id, title, description, price, level, category, image, instructor_name, instructor_email
                                    ),
                                ),
                                rx.button(
                                    rx.icon("trash-2", size=16),
                                    size="2",
                                    variant="soft",
                                    color_scheme="red",
                                    on_click=lambda _, course_id=course["_id"], title=course["title"]: CourseManagementState.open_delete_dialog(
                                        course_id, title
                                    ),
                                ),
                                spacing="2",
                            )
                        ),
                    ),
                ),
            ),
        ),
    )


def statistics_cards() -> rx.Component:
    """Tarjetas de estadísticas."""
    return rx.grid(
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon("book-open", size=20, color=rx.color("purple", 9)),
                    rx.spacer(),
                    rx.badge(CourseManagementState.courses.length().to_string(), size="2", color_scheme="purple"),
                ),
                rx.text("Total Cursos", size="3", weight="bold"),
                spacing="2",
                align_items="start",
            ),
        ),
        rx.card(
            rx.vstack(
                rx.hstack(
                    rx.icon("filter", size=20, color=rx.color("blue", 9)),
                    rx.spacer(),
                    rx.badge(CourseManagementState.filtered_courses.length().to_string(), size="2", color_scheme="blue"),
                ),
                rx.text("Cursos Filtrados", size="3", weight="bold"),
                spacing="2",
                align_items="start",
            ),
        ),
        columns="2",
        spacing="4",
        width="100%",
    )


def course_management_content() -> rx.Component:
    """Contenido de la página de gestión de cursos."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.heading("Gestión de Cursos", size="8"),
                    rx.spacer(),
                    rx.button(
                        rx.icon("plus", size=20),
                        "Nuevo Curso",
                        on_click=CourseManagementState.open_create_course_dialog,
                    ),
                    width="100%",
                    align_items="center",
                ),
                # Estadísticas
                statistics_cards(),
                # Filtros
                rx.card(
                    rx.hstack(
                        rx.input(
                            value=CourseManagementState.search_query,
                            on_change=CourseManagementState.on_search_change,
                            placeholder="Buscar por título, descripción o categoría...",
                            width="100%",
                        ),
                        rx.select(
                            ["all", "beginner", "intermediate", "advanced"],
                            value=CourseManagementState.level_filter,
                            on_change=CourseManagementState.on_level_filter_change,
                            placeholder="Filtrar por nivel",
                        ),
                        width="100%",
                        spacing="3",
                    ),
                ),
                # Tabla
                courses_table(),
                spacing="6",
                width="100%",
                padding_y="4",
                on_mount=CourseManagementState.load_courses,
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        # Diálogos
        course_dialog(),
        delete_confirmation_dialog(),
        width="100%",
        spacing="0",
    )


def course_management_page() -> rx.Component:
    """Página de gestión de cursos con protección."""
    return admin_only(course_management_content())
