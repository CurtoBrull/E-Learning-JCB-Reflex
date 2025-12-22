"""
Página de gestión de cursos para administradores de la plataforma E-Learning JCB.

Este módulo proporciona una interfaz completa de CRUD (Create, Read, Update, Delete)
para que los administradores gestionen todos los cursos de la plataforma.

Funcionalidades:
- Tabla con todos los cursos del sistema
- Filtros de búsqueda por título, descripción o categoría
- Filtro por nivel (all, beginner, intermediate, advanced)
- Creación de nuevos cursos mediante diálogo modal
- Edición de cursos existentes
- Eliminación de cursos con confirmación
- Estadísticas de cursos totales y filtrados
- Badges de color según el nivel del curso
- Información del instructor para cada curso
- Protección de acceso solo para administradores

Ruta: /admin/courses
Acceso: Protegida (solo administradores autenticados)
Estado: CourseManagementState (gestión de cursos)
Protección: admin_only HOC
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only
from E_Learning_JCB_Reflex.states.course_management_state import CourseManagementState


def get_level_badge(level: str) -> rx.Component:
    """
    Genera un badge con el nivel del curso en español y color apropiado.

    Args:
        level: Nivel del curso ("beginner", "intermediate" o "advanced")

    Returns:
        rx.Component: Badge con el nivel traducido y color según el tipo

    Notas:
        - beginner -> Badge verde "Principiante"
        - intermediate -> Badge naranja "Intermedio"
        - advanced -> Badge rojo "Avanzado"
        - Otros valores -> Badge gris sin traducción
    """
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
    """
    Renderiza el diálogo modal para crear o editar un curso.

    Muestra un formulario completo con todos los campos necesarios
    para crear o modificar un curso, incluyendo información del instructor.

    Returns:
        rx.Component: Dialog modal con formulario de curso

    Notas:
        - El título cambia según CourseManagementState.dialog_mode ("create" vs "edit")
        - Incluye campos: título, descripción, precio, nivel, categoría, imagen
        - Sección separada para información del instructor (nombre y email)
        - Los campos están vinculados a course_* variables del state
        - El botón ejecuta CourseManagementState.save_course
        - Se muestra cuando CourseManagementState.show_course_dialog es True
        - Max width de 600px para mejor legibilidad del formulario
    """
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
    """
    Renderiza el diálogo de confirmación para eliminar un curso.

    Muestra un alert dialog que solicita confirmación antes de eliminar
    un curso. Advierte que la acción no se puede deshacer.

    Returns:
        rx.Component: Alert dialog de confirmación de eliminación

    Notas:
        - Muestra el título del curso desde CourseManagementState.course_to_delete_title
        - Se muestra cuando CourseManagementState.show_delete_dialog es True
        - El botón "Eliminar" ejecuta CourseManagementState.confirm_delete_course
        - El botón tiene color_scheme="red" para indicar acción destructiva
    """
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
    """
    Renderiza la tabla con todos los cursos filtrados.

    Muestra una tabla con columnas: Título, Categoría, Nivel, Precio,
    Estudiantes y Acciones. Cada fila incluye botones para editar
    y eliminar el curso.

    Returns:
        rx.Component: Card con tabla de cursos

    Notas:
        - Muestra CourseManagementState.filtered_courses (ya filtrados)
        - Los botones de editar/eliminar usan lambdas para pasar todos los parámetros
        - El botón editar abre el diálogo con datos precargados del curso
        - El botón eliminar abre el diálogo de confirmación
        - El nivel se muestra usando get_level_badge para color apropiado
        - El precio se formatea con símbolo de euro
    """
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
    """
    Renderiza las tarjetas de estadísticas de cursos.

    Muestra dos tarjetas con información agregada:
    - Total de cursos en la plataforma
    - Cursos filtrados (después de aplicar búsqueda/nivel)

    Returns:
        rx.Component: Grid con 2 tarjetas de estadísticas

    Notas:
        - Las estadísticas se calculan dinámicamente desde los arrays del state
        - Útil para ver el impacto de los filtros aplicados
    """
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
    """
    Renderiza el contenido completo de la página de gestión de cursos.

    Muestra todas las secciones de la página organizadas verticalmente:
    1. Header con título y botón "Nuevo Curso"
    2. Tarjetas de estadísticas
    3. Card con filtros (búsqueda y selector de nivel)
    4. Tabla de cursos con acciones

    Returns:
        rx.Component: Contenido completo de la página de gestión

    Notas:
        - Utiliza on_mount con CourseManagementState.load_courses
        - Los filtros actualizan automáticamente la tabla
        - Incluye los diálogos modales (course_dialog y delete_confirmation_dialog)
        - Max width de 1400px para mejor legibilidad
    """
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
    """
    Renderiza la página de gestión de cursos con protección.

    Envuelve el contenido de gestión con el HOC admin_only
    para garantizar que solo administradores puedan acceder.

    Returns:
        rx.Component: Página protegida de gestión de cursos

    Notas:
        - Utiliza el HOC admin_only de components.protected
        - Si el usuario no es administrador, redirige o muestra acceso denegado
        - Esta es la función principal exportada para el routing
    """
    return admin_only(course_management_content())
