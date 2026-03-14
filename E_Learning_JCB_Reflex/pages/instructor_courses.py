"""
Página de gestión de cursos para instructores.

Permite al instructor ver, crear, editar y eliminar sus propios cursos.

Ruta: /instructor/courses
Acceso: Protegida (solo instructores autenticados)
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer
from E_Learning_JCB_Reflex.components.protected import instructor_only
from E_Learning_JCB_Reflex.states.instructor_course_state import InstructorCourseState


def level_badge(level: str) -> rx.Component:
    return rx.match(
        level,
        ("beginner", rx.badge("Principiante", color_scheme="green", size="1")),
        ("intermediate", rx.badge("Intermedio", color_scheme="orange", size="1")),
        ("advanced", rx.badge("Avanzado", color_scheme="red", size="1")),
        rx.badge(level, color_scheme="gray", size="1"),
    )


def course_form_dialog() -> rx.Component:
    """Modal para crear o editar un curso."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.cond(
                    InstructorCourseState.is_editing,
                    "Editar Curso",
                    "Crear Nuevo Curso",
                )
            ),
            rx.dialog.description(
                "Completa los campos para guardar el curso en la base de datos.",
                size="2",
                color=rx.color("gray", 10),
                margin_bottom="1em",
            ),
            rx.vstack(
                # Título
                rx.vstack(
                    rx.text("Título *", size="2", weight="bold"),
                    rx.input(
                        placeholder="Ej: Introducción a Python",
                        value=InstructorCourseState.form_title,
                        on_change=InstructorCourseState.set_form_title,
                        size="2",
                        width="100%",
                    ),
                    spacing="1",
                    width="100%",
                ),
                # Descripción
                rx.vstack(
                    rx.text("Descripción *", size="2", weight="bold"),
                    rx.text_area(
                        placeholder="Describe el contenido del curso...",
                        value=InstructorCourseState.form_description,
                        on_change=InstructorCourseState.set_form_description,
                        rows="3",
                        width="100%",
                    ),
                    spacing="1",
                    width="100%",
                ),
                # Precio y nivel (misma fila)
                rx.hstack(
                    rx.vstack(
                        rx.text("Precio (€) *", size="2", weight="bold"),
                        rx.input(
                            placeholder="49.99",
                            value=InstructorCourseState.form_price,
                            on_change=InstructorCourseState.set_form_price,
                            type="number",
                            size="2",
                            width="100%",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    rx.vstack(
                        rx.text("Nivel *", size="2", weight="bold"),
                        rx.select.root(
                            rx.select.trigger(width="100%"),
                            rx.select.content(
                                rx.select.item("Principiante", value="beginner"),
                                rx.select.item("Intermedio", value="intermediate"),
                                rx.select.item("Avanzado", value="advanced"),
                            ),
                            value=InstructorCourseState.form_level,
                            on_change=InstructorCourseState.set_form_level,
                            size="2",
                        ),
                        spacing="1",
                        width="100%",
                    ),
                    spacing="4",
                    width="100%",
                ),
                # Categoría
                rx.vstack(
                    rx.text("Categoría", size="2", weight="bold"),
                    rx.input(
                        placeholder="Ej: Programación, IA, Diseño Web...",
                        value=InstructorCourseState.form_category,
                        on_change=InstructorCourseState.set_form_category,
                        size="2",
                        width="100%",
                    ),
                    spacing="1",
                    width="100%",
                ),
                # Imagen
                rx.vstack(
                    rx.text("URL de imagen", size="2", weight="bold"),
                    rx.input(
                        placeholder="/images/courses/mi_curso.webp",
                        value=InstructorCourseState.form_thumbnail,
                        on_change=InstructorCourseState.set_form_thumbnail,
                        size="2",
                        width="100%",
                    ),
                    spacing="1",
                    width="100%",
                ),
                # Error
                rx.cond(
                    InstructorCourseState.error != "",
                    rx.callout(
                        InstructorCourseState.error,
                        icon="circle-alert",
                        color_scheme="red",
                        size="1",
                    ),
                ),
                spacing="4",
                width="100%",
            ),
            rx.hstack(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                        on_click=InstructorCourseState.close_form,
                    ),
                ),
                rx.button(
                    rx.cond(
                        InstructorCourseState.loading,
                        rx.spinner(size="2"),
                        rx.cond(
                            InstructorCourseState.is_editing,
                            "Guardar Cambios",
                            "Crear Curso",
                        ),
                    ),
                    color_scheme="purple",
                    on_click=InstructorCourseState.save_course,
                    disabled=InstructorCourseState.loading,
                ),
                justify="end",
                spacing="3",
                margin_top="1.5em",
                width="100%",
            ),
            max_width="520px",
        ),
        open=InstructorCourseState.show_form,
    )


def delete_confirm_dialog() -> rx.Component:
    """Diálogo de confirmación para eliminar un curso."""
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("¿Eliminar curso?"),
            rx.alert_dialog.description(
                rx.text(
                    "Vas a eliminar permanentemente: ",
                    rx.text.strong(InstructorCourseState.deleting_course_title),
                    ". Esta acción no se puede deshacer.",
                ),
                size="2",
            ),
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                        on_click=InstructorCourseState.cancel_delete,
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Eliminar",
                        color_scheme="red",
                        on_click=InstructorCourseState.execute_delete,
                    ),
                ),
                justify="end",
                spacing="3",
                margin_top="1em",
            ),
        ),
        open=InstructorCourseState.show_delete_confirm,
    )


def course_row(course: dict) -> rx.Component:
    """Fila de un curso en la tabla."""
    return rx.table.row(
        rx.table.cell(
            rx.vstack(
                rx.text(course["title"], weight="bold", size="2"),
                rx.text(
                    course["description"],
                    size="1",
                    color=rx.color("gray", 10),
                    no_of_lines=1,
                ),
                spacing="1",
                align_items="start",
            ),
            max_width="320px",
        ),
        rx.table.cell(level_badge(course["level"])),
        rx.table.cell(
            rx.text(course.get("category", "—"), size="2"),
        ),
        rx.table.cell(
            rx.text(f"€{course['price']}", size="2", weight="medium"),
        ),
        rx.table.cell(
            rx.badge(
                f"{course['students_count']} alumnos",
                color_scheme="blue",
                size="1",
            ),
        ),
        rx.table.cell(
            rx.hstack(
                rx.icon_button(
                    rx.icon("pencil", size=15),
                    variant="soft",
                    color_scheme="purple",
                    size="1",
                    on_click=InstructorCourseState.open_edit_form(course),
                    title="Editar",
                ),
                rx.icon_button(
                    rx.icon("trash-2", size=15),
                    variant="soft",
                    color_scheme="red",
                    size="1",
                    on_click=InstructorCourseState.confirm_delete(course),
                    title="Eliminar",
                ),
                spacing="2",
            ),
        ),
    )


def instructor_courses_content() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading("Mis Cursos", size="8"),
                        rx.text(
                            "Gestiona los cursos que has creado",
                            size="4",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="1",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("plus", size=18),
                            rx.text("Crear Curso"),
                            spacing="2",
                        ),
                        color_scheme="purple",
                        size="3",
                        on_click=InstructorCourseState.open_create_form,
                    ),
                    width="100%",
                    align_items="center",
                ),
                rx.divider(),
                # Mensaje de éxito
                rx.cond(
                    InstructorCourseState.success != "",
                    rx.callout(
                        InstructorCourseState.success,
                        icon="circle-check",
                        color_scheme="green",
                    ),
                ),
                # Mensaje de error global
                rx.cond(
                    InstructorCourseState.error != "",
                    rx.callout(
                        InstructorCourseState.error,
                        icon="circle-alert",
                        color_scheme="red",
                    ),
                ),
                # Estado de carga
                rx.cond(
                    InstructorCourseState.loading,
                    rx.center(rx.spinner(size="3"), padding="4em"),
                    # Tabla de cursos o estado vacío
                    rx.cond(
                        InstructorCourseState.courses.length() > 0,
                        rx.table.root(
                            rx.table.header(
                                rx.table.row(
                                    rx.table.column_header_cell("Curso"),
                                    rx.table.column_header_cell("Nivel"),
                                    rx.table.column_header_cell("Categoría"),
                                    rx.table.column_header_cell("Precio"),
                                    rx.table.column_header_cell("Alumnos"),
                                    rx.table.column_header_cell("Acciones"),
                                ),
                            ),
                            rx.table.body(
                                rx.foreach(
                                    InstructorCourseState.courses,
                                    course_row,
                                ),
                            ),
                            width="100%",
                            variant="surface",
                        ),
                        # Sin cursos
                        rx.center(
                            rx.vstack(
                                rx.icon("graduation-cap", size=48, color=rx.color("gray", 7)),
                                rx.text(
                                    "Aún no has creado ningún curso",
                                    size="4",
                                    color=rx.color("gray", 10),
                                ),
                                rx.button(
                                    rx.hstack(
                                        rx.icon("plus", size=18),
                                        rx.text("Crear mi primer curso"),
                                        spacing="2",
                                    ),
                                    color_scheme="purple",
                                    on_click=InstructorCourseState.open_create_form,
                                ),
                                spacing="4",
                                align_items="center",
                                padding="4em",
                            ),
                        ),
                    ),
                ),
                spacing="6",
                width="100%",
                padding_y="6",
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        # Modales
        course_form_dialog(),
        delete_confirm_dialog(),
        footer(),
        width="100%",
        spacing="0",
    )


def instructor_courses_page() -> rx.Component:
    return instructor_only(
        rx.box(
            instructor_courses_content(),
            on_mount=InstructorCourseState.load_my_courses,
            width="100%",
        )
    )
