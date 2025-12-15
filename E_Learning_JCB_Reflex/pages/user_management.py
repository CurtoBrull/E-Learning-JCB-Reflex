"""Página de gestión de usuarios (solo administradores)."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only
from E_Learning_JCB_Reflex.states.user_management_state import UserManagementState


def user_dialog() -> rx.Component:
    """Diálogo para crear/editar usuario."""
    return rx.dialog.root(
        rx.dialog.content(
            rx.dialog.title(
                rx.cond(
                    UserManagementState.edit_mode,
                    "Editar Usuario",
                    "Crear Nuevo Usuario",
                )
            ),
            rx.dialog.description(
                rx.cond(
                    UserManagementState.edit_mode,
                    "Modifica los datos del usuario",
                    "Completa los datos del nuevo usuario",
                ),
                size="2",
                margin_bottom="4",
            ),
            rx.vstack(
                rx.vstack(
                    rx.text("Nombre", size="2", weight="bold"),
                    rx.input(
                        placeholder="Nombre",
                        value=UserManagementState.form_first_name,
                        on_change=UserManagementState.set_form_first_name,
                        size="3",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text("Apellido", size="2", weight="bold"),
                    rx.input(
                        placeholder="Apellido",
                        value=UserManagementState.form_last_name,
                        on_change=UserManagementState.set_form_last_name,
                        size="3",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text("Email", size="2", weight="bold"),
                    rx.input(
                        placeholder="Email",
                        type="email",
                        value=UserManagementState.form_email,
                        on_change=UserManagementState.set_form_email,
                        size="3",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text(
                        rx.cond(
                            UserManagementState.edit_mode,
                            "Nueva Contraseña (dejar vacío para no cambiar)",
                            "Contraseña",
                        ),
                        size="2",
                        weight="bold",
                    ),
                    rx.input(
                        placeholder="Contraseña (mínimo 6 caracteres)",
                        type="password",
                        value=UserManagementState.form_password,
                        on_change=UserManagementState.set_form_password,
                        size="3",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.text("Rol", size="2", weight="bold"),
                    rx.select(
                        ["student", "instructor", "admin"],
                        value=UserManagementState.form_role,
                        on_change=UserManagementState.set_form_role,
                        size="3",
                    ),
                    spacing="2",
                    width="100%",
                ),
                spacing="4",
                width="100%",
            ),
            rx.flex(
                rx.dialog.close(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.button(
                    rx.cond(
                        UserManagementState.loading,
                        rx.hstack(
                            rx.spinner(size="3"),
                            rx.text("Guardando..."),
                            spacing="2",
                        ),
                        rx.cond(
                            UserManagementState.edit_mode,
                            "Actualizar",
                            "Crear",
                        ),
                    ),
                    on_click=UserManagementState.save_user,
                    disabled=UserManagementState.loading,
                ),
                spacing="3",
                margin_top="4",
                justify="end",
            ),
        ),
        open=UserManagementState.show_user_dialog,
        on_open_change=UserManagementState.close_user_dialog,
    )


def delete_confirmation_dialog() -> rx.Component:
    """Diálogo de confirmación para eliminar usuario."""
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirmar Eliminación"),
            rx.alert_dialog.description(
                f"¿Estás seguro de que deseas eliminar al usuario {UserManagementState.user_to_delete_name}? Esta acción no se puede deshacer.",
                size="3",
            ),
            rx.flex(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        rx.cond(
                            UserManagementState.loading,
                            rx.hstack(
                                rx.spinner(size="3"),
                                rx.text("Eliminando..."),
                                spacing="2",
                            ),
                            "Eliminar",
                        ),
                        color_scheme="red",
                        disabled=UserManagementState.loading,
                    ),
                    on_click=UserManagementState.confirm_delete_user,
                ),
                spacing="3",
                justify="end",
            ),
        ),
        open=UserManagementState.show_delete_dialog,
        on_open_change=UserManagementState.close_delete_dialog,
    )


def get_role_badge(role: str) -> rx.Component:
    """Obtener badge de rol con color apropiado."""
    return rx.match(
        role,
        ("student", rx.badge("Estudiante", color_scheme="blue", size="2")),
        ("instructor", rx.badge("Instructor", color_scheme="green", size="2")),
        ("admin", rx.badge("Admin", color_scheme="red", size="2")),
        rx.badge(role, size="2"),
    )


def users_table() -> rx.Component:
    """Tabla de usuarios."""
    return rx.card(
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("Nombre"),
                    rx.table.column_header_cell("Email"),
                    rx.table.column_header_cell("Rol"),
                    rx.table.column_header_cell("Fecha Creación"),
                    rx.table.column_header_cell("Acciones"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    UserManagementState.filtered_users,
                    lambda user: rx.table.row(
                        rx.table.cell(
                            f"{user['firstName']} {user['lastName']}",
                            font_weight="medium",
                        ),
                        rx.table.cell(user["email"]),
                        rx.table.cell(get_role_badge(user["role"])),
                        rx.table.cell(user["createdAt"]),
                        rx.table.cell(
                            rx.hstack(
                                rx.button(
                                    rx.icon("pencil", size=16),
                                    size="2",
                                    variant="soft",
                                    color_scheme="blue",
                                    on_click=lambda user_id=user["_id"], first_name=user["firstName"], last_name=user["lastName"], email=user["email"], role=user["role"]: UserManagementState.open_edit_user_dialog(
                                        user_id, first_name, last_name, email, role
                                    ),
                                ),
                                rx.button(
                                    rx.icon("trash-2", size=16),
                                    size="2",
                                    variant="soft",
                                    color_scheme="red",
                                    on_click=lambda user_id=user["_id"], user_name=f"{user['firstName']} {user['lastName']}": UserManagementState.open_delete_dialog(
                                        user_id, user_name
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


def user_management_content() -> rx.Component:
    """Contenido de la página de gestión de usuarios."""
    return rx.vstack(
        navbar(),
        user_dialog(),
        delete_confirmation_dialog(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading("Gestión de Usuarios", size="9"),
                        rx.text(
                            "Administra los usuarios del sistema",
                            size="4",
                            color=rx.color("gray", 11),
                        ),
                        spacing="2",
                        align_items="start",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("user-plus", size=20),
                            rx.text("Crear Usuario"),
                            spacing="2",
                        ),
                        on_click=UserManagementState.open_create_user_dialog,
                        size="3",
                    ),
                    width="100%",
                    align_items="center",
                ),
                # Filtros
                rx.card(
                    rx.hstack(
                        rx.input(
                            placeholder="Buscar por nombre o email...",
                            value=UserManagementState.search_query,
                            on_change=UserManagementState.set_search_query,
                            size="3",
                            width="100%",
                            max_width="400px",
                        ),
                        rx.select(
                            ["all", "student", "instructor", "admin"],
                            placeholder="Filtrar por rol",
                            value=UserManagementState.role_filter,
                            on_change=UserManagementState.set_role_filter,
                            size="3",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                ),
                # Estadísticas
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("users", size=24, color=rx.color("blue", 9)),
                                rx.spacer(),
                                rx.badge(
                                    UserManagementState.users.length().to_string(),
                                    size="2",
                                    color_scheme="blue",
                                ),
                            ),
                            rx.text("Total Usuarios", size="3", weight="bold"),
                            rx.text(
                                "Usuarios registrados en el sistema",
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
                                rx.badge(
                                    UserManagementState.filtered_users.length().to_string(),
                                    size="2",
                                    color_scheme="green",
                                ),
                            ),
                            rx.text("Filtrados", size="3", weight="bold"),
                            rx.text(
                                "Usuarios mostrados en la tabla",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    columns="2",
                    spacing="4",
                    width="100%",
                ),
                # Tabla
                users_table(),
                spacing="6",
                width="100%",
                padding_y="4",
                on_mount=UserManagementState.load_users,
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
    )


def user_management_page() -> rx.Component:
    """Página de gestión de usuarios con protección de admin."""
    return admin_only(user_management_content())
