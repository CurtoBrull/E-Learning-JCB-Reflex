"""
Página de configuración del sistema para administradores de la plataforma E-Learning JCB.

Este módulo permite a los administradores configurar diversos aspectos de la
plataforma, incluyendo parámetros generales, seguridad, correo electrónico,
pagos y más.

Funcionalidades:
- Configuración general de la plataforma (nombre, logo, descripción)
- Configuración de correo electrónico (SMTP, plantillas)
- Configuración de pagos y suscripciones
- Parámetros de seguridad (políticas de contraseñas, sesiones)
- Configuración de notificaciones
- Gestión de backups automáticos
- Configuración de SEO (meta tags, sitemap)
- Logs del sistema y auditoría
- Protección de acceso solo para administradores

Ruta: /admin/settings
Acceso: Protegida (solo administradores autenticados)
Protección: admin_only HOC
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import admin_only


def admin_settings_content() -> rx.Component:
    """
    Renderiza el contenido de la página de configuración del sistema.

    Muestra paneles organizados por categorías de configuración, permitiendo
    a los administradores personalizar diversos aspectos de la plataforma.

    Returns:
        rx.Component: Contenido completo de configuración del sistema

    Notas:
        - Por ahora muestra un mensaje de funcionalidad en desarrollo
        - Se implementará con formularios por sección
        - Incluirá validación y confirmación de cambios críticos
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            "Configuración del Sistema",
                            size="9",
                        ),
                        rx.text(
                            "Administra los parámetros globales de la plataforma",
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

                # Contenido principal
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.icon("settings", size=24, color=rx.color("red", 9)),
                            rx.heading("Funcionalidad en Desarrollo", size="6"),
                            spacing="3",
                        ),
                        rx.divider(),
                        rx.vstack(
                            rx.text(
                                "El panel de configuración del sistema está actualmente en desarrollo.",
                                size="4",
                            ),
                            rx.text(
                                "Próximamente podrás configurar:",
                                size="3",
                                weight="bold",
                                margin_top="4",
                            ),
                            rx.grid(
                                rx.card(
                                    rx.vstack(
                                        rx.icon("globe", size=20, color=rx.color("blue", 9)),
                                        rx.text("Configuración General", size="3", weight="bold"),
                                        rx.unordered_list(
                                            rx.list_item("Nombre de la plataforma"),
                                            rx.list_item("Logo y favicon"),
                                            rx.list_item("Descripción y meta tags"),
                                            rx.list_item("Idioma predeterminado"),
                                            margin_left="4",
                                        ),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("shield", size=20, color=rx.color("red", 9)),
                                        rx.text("Seguridad", size="3", weight="bold"),
                                        rx.unordered_list(
                                            rx.list_item("Políticas de contraseñas"),
                                            rx.list_item("Duración de sesiones"),
                                            rx.list_item("Autenticación de dos factores"),
                                            rx.list_item("Bloqueo de IPs"),
                                            margin_left="4",
                                        ),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("mail", size=20, color=rx.color("green", 9)),
                                        rx.text("Correo Electrónico", size="3", weight="bold"),
                                        rx.unordered_list(
                                            rx.list_item("Configuración SMTP"),
                                            rx.list_item("Plantillas de correo"),
                                            rx.list_item("Notificaciones automáticas"),
                                            rx.list_item("Remitente predeterminado"),
                                            margin_left="4",
                                        ),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("credit-card", size=20, color=rx.color("orange", 9)),
                                        rx.text("Pagos y Suscripciones", size="3", weight="bold"),
                                        rx.unordered_list(
                                            rx.list_item("Pasarelas de pago"),
                                            rx.list_item("Moneda predeterminada"),
                                            rx.list_item("Planes de suscripción"),
                                            rx.list_item("Comisiones de instructores"),
                                            margin_left="4",
                                        ),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("bell", size=20, color=rx.color("purple", 9)),
                                        rx.text("Notificaciones", size="3", weight="bold"),
                                        rx.unordered_list(
                                            rx.list_item("Notificaciones push"),
                                            rx.list_item("Alertas por email"),
                                            rx.list_item("Recordatorios automáticos"),
                                            rx.list_item("Preferencias de usuarios"),
                                            margin_left="4",
                                        ),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                rx.card(
                                    rx.vstack(
                                        rx.icon("database", size=20, color=rx.color("pink", 9)),
                                        rx.text("Backups y Mantenimiento", size="3", weight="bold"),
                                        rx.unordered_list(
                                            rx.list_item("Backups automáticos"),
                                            rx.list_item("Restauración de datos"),
                                            rx.list_item("Limpieza de logs"),
                                            rx.list_item("Modo mantenimiento"),
                                            margin_left="4",
                                        ),
                                        spacing="2",
                                        align_items="start",
                                    ),
                                ),
                                columns="2",
                                spacing="4",
                                width="100%",
                            ),
                            rx.callout(
                                rx.hstack(
                                    rx.icon("alert-triangle", size=20),
                                    rx.text(
                                        "Advertencia: Los cambios en la configuración del sistema pueden afectar el funcionamiento de la plataforma. Se recomienda hacer backups antes de modificar parámetros críticos.",
                                        size="2",
                                    ),
                                    spacing="2",
                                ),
                                color_scheme="yellow",
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


def admin_settings_page() -> rx.Component:
    """
    Renderiza la página de configuración del sistema con protección.

    Envuelve el contenido con el HOC admin_only para garantizar
    que solo usuarios con rol "admin" puedan acceder.

    Returns:
        rx.Component: Página protegida de configuración del sistema

    Notas:
        - Utiliza el HOC admin_only de components.protected
        - Si el usuario no es administrador, redirige o muestra acceso denegado
        - Esta es la función principal exportada para el routing
        - Los cambios críticos requieren confirmación adicional
    """
    return admin_only(admin_settings_content())
