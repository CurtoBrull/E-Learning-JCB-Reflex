"""
Página de gestión de categorías para administradores de la plataforma E-Learning JCB.

Este módulo permite a los administradores crear, editar, eliminar y visualizar
las categorías de cursos disponibles en la plataforma.

Funcionalidades:
- Listado completo de categorías existentes
- Crear nuevas categorías con nombre y descripción
- Editar categorías existentes
- Eliminar categorías (con confirmación)
- Contador de cursos por categoría
- Búsqueda y filtrado de categorías
- Protección de acceso solo para administradores

Ruta: /admin/categories
Acceso: Protegida (solo administradores autenticados)
Protección: admin_only HOC
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only


def category_management_content() -> rx.Component:
    """
    Renderiza el contenido de la página de gestión de categorías.

    Muestra una interfaz para administrar las categorías de cursos, incluyendo
    un encabezado, tabla de categorías y formulario para crear/editar.

    Returns:
        rx.Component: Contenido completo de la gestión de categorías

    Notas:
        - Por ahora muestra un mensaje de funcionalidad en desarrollo
        - Se implementará con tabla de categorías y CRUD completo
        - Incluirá contador de cursos por categoría
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            "Gestión de Categorías",
                            size="9",
                        ),
                        rx.text(
                            "Administra las categorías de cursos de la plataforma",
                            size="5",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.spacer(),
                    rx.button(
                        rx.hstack(
                            rx.icon("plus", size=20),
                            rx.text("Nueva Categoría"),
                            spacing="2",
                        ),
                        size="3",
                        disabled=True,
                    ),
                    width="100%",
                    align_items="center",
                ),

                # Contenido principal
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("info", size=24, color=rx.color("blue", 9)),
                            rx.heading("Funcionalidad en Desarrollo", size="6"),
                            spacing="3",
                        ),
                        rx.divider(),
                        rx.vstack(
                            rx.text(
                                "La gestión de categorías está actualmente en desarrollo.",
                                size="4",
                            ),
                            rx.text(
                                "Próximamente podrás:",
                                size="3",
                                weight="bold",
                                margin_top="4",
                            ),
                            rx.unordered_list(
                                rx.list_item("Crear y editar categorías de cursos"),
                                rx.list_item("Organizar cursos por categorías"),
                                rx.list_item("Ver estadísticas por categoría"),
                                rx.list_item("Asignar múltiples categorías a un curso"),
                                rx.list_item("Filtrar y buscar categorías"),
                            ),
                            rx.text(
                                "Mientras tanto, las categorías se gestionan directamente desde la página de gestión de cursos.",
                                size="3",
                                color=rx.color("gray", 11),
                                margin_top="4",
                            ),
                            align_items="start",
                            spacing="2",
                        ),
                        rx.divider(),
                        rx.hstack(
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
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("book-open", size=18),
                                        rx.text("Ir a Gestión de Cursos"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="2",
                                ),
                                href="/admin/courses",
                            ),
                            spacing="3",
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
            max_width="1200px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
    )


def category_management_page() -> rx.Component:
    """
    Renderiza la página de gestión de categorías con protección.

    Envuelve el contenido con el HOC admin_only para garantizar
    que solo usuarios con rol "admin" puedan acceder.

    Returns:
        rx.Component: Página protegida de gestión de categorías

    Notas:
        - Utiliza el HOC admin_only de components.protected
        - Si el usuario no es administrador, redirige o muestra acceso denegado
        - Esta es la función principal exportada para el routing
    """
    return admin_only(category_management_content())
