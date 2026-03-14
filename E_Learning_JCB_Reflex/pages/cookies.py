"""
Página de Política de Cookies de E-Learning JCB.

Ruta: /cookies
Acceso: Pública
"""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.footer import footer

LAST_UPDATED = "14 de marzo de 2026"

COOKIE_TYPES = [
    {
        "name": "Cookies técnicas / estrictamente necesarias",
        "color": "blue",
        "icon": "settings",
        "required": True,
        "description": "Son imprescindibles para el funcionamiento de la plataforma. Sin ellas no sería posible navegar ni acceder a las funcionalidades básicas.",
        "examples": [
            ("session_id", "Mantiene la sesión activa del usuario autenticado.", "Sesión"),
            ("csrf_token", "Protege contra ataques de falsificación de solicitudes.", "Sesión"),
            ("theme_pref", "Recuerda la preferencia de tema claro/oscuro.", "30 días"),
        ],
    },
    {
        "name": "Cookies de rendimiento / analíticas",
        "color": "green",
        "icon": "bar-chart-2",
        "required": False,
        "description": "Nos permiten medir el uso de la plataforma y mejorar su rendimiento. Los datos recogidos son anónimos y agregados.",
        "examples": [
            ("_page_views", "Cuenta las páginas visitadas por sesión.", "Sesión"),
            ("_load_time", "Registra tiempos de carga para optimización.", "Sesión"),
        ],
    },
    {
        "name": "Cookies funcionales",
        "color": "purple",
        "icon": "sliders-horizontal",
        "required": False,
        "description": "Mejoran la experiencia personalizada del usuario recordando preferencias como el idioma o la última posición en un curso.",
        "examples": [
            ("last_course", "Recuerda el último curso visitado para acceso rápido.", "7 días"),
            ("search_history", "Guarda las últimas búsquedas realizadas en el catálogo.", "7 días"),
        ],
    },
    {
        "name": "Cookies de terceros",
        "color": "orange",
        "icon": "globe",
        "required": False,
        "description": "Instaladas por servicios externos integrados en la plataforma (reproductores de vídeo, mapas, etc.). Su gestión depende de cada proveedor.",
        "examples": [
            ("YouTube", "Cookies del reproductor de vídeo embebido para lecciones en formato vídeo.", "Según YouTube"),
            ("Vimeo", "Alternativa de vídeo para contenido formativo.", "Según Vimeo"),
        ],
    },
]

SECTIONS = [
    {
        "icon": "info",
        "color": "blue",
        "title": "¿Qué son las cookies?",
        "content": "Las cookies son pequeños archivos de texto que los sitios web almacenan en tu dispositivo (ordenador, tablet o móvil) cuando los visitas. Se utilizan para que la plataforma recuerde información sobre tu visita, lo que facilita tu próxima visita y hace que el sitio te resulte más útil.",
    },
    {
        "icon": "shield",
        "color": "purple",
        "title": "¿Por qué usamos cookies?",
        "content": "E-Learning JCB utiliza cookies para garantizar el correcto funcionamiento de la plataforma, recordar tus preferencias, mantener tu sesión activa mientras navegas y mejorar continuamente la experiencia de aprendizaje. Nunca usamos cookies para rastrearte fuera de nuestra plataforma ni para vender tu información a terceros.",
    },
]


def cookie_example_row(name: str, purpose: str, duration: str, color: str) -> rx.Component:
    return rx.hstack(
        rx.text(name, size="2", weight="medium", min_width="140px", color=rx.color("gray", 12)),
        rx.text(purpose, size="2", color=rx.color("gray", 11), flex="1"),
        rx.badge(duration, color_scheme=color, size="1", variant="soft", white_space="nowrap"),
        spacing="3",
        align_items="center",
        width="100%",
        padding_y="0.4em",
        border_bottom=f"1px solid {rx.color('gray', 4)}",
    )


def cookie_type_card(name: str, color: str, icon: str, required: bool, description: str, examples: list) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=18, color="white"),
                    background=rx.color(color, 9),
                    padding="0.5em",
                    border_radius="9px",
                    flex_shrink="0",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.heading(name, size="4"),
                        rx.badge(
                            "Obligatoria" if required else "Opcional",
                            color_scheme="red" if required else "gray",
                            size="1",
                            variant="soft",
                        ),
                        spacing="2",
                        align_items="center",
                        flex_wrap="wrap",
                    ),
                    rx.text(description, size="2", color=rx.color("gray", 10)),
                    spacing="1",
                    align_items="start",
                ),
                spacing="3",
                align_items="start",
                width="100%",
            ),
            rx.box(
                rx.vstack(
                    rx.text("Cookies de este tipo:", size="2", weight="medium", color=rx.color("gray", 11)),
                    *[
                        cookie_example_row(ex[0], ex[1], ex[2], color)
                        for ex in examples
                    ],
                    spacing="1",
                    width="100%",
                ),
                background=rx.color("gray", 2),
                border_radius="8px",
                padding="1em",
                width="100%",
            ),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def info_card(icon: str, color: str, title: str, content: str) -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.hstack(
                rx.box(
                    rx.icon(icon, size=18, color="white"),
                    background=rx.color(color, 9),
                    padding="0.5em",
                    border_radius="9px",
                    flex_shrink="0",
                ),
                rx.heading(title, size="4"),
                spacing="3",
                align_items="center",
            ),
            rx.text(content, size="2", color=rx.color("gray", 11), line_height="1.8"),
            spacing="4",
            width="100%",
        ),
        width="100%",
    )


def cookies_page() -> rx.Component:
    return rx.box(
        navbar(),
        rx.container(
            rx.vstack(
                rx.center(
                    rx.box(
                        rx.icon("cookie", size=40, color="white"),
                        background=rx.color("orange", 9),
                        padding="1.1em",
                        border_radius="20px",
                        box_shadow=f"0 8px 32px {rx.color('orange', 6)}",
                    ),
                    margin_bottom="0.5em",
                ),
                rx.heading(
                    "Política de Cookies",
                    size="9",
                    text_align="center",
                    background=f"linear-gradient(135deg, {rx.color('orange', 10)}, {rx.color('red', 10)})",
                    background_clip="text",
                    color="transparent",
                ),
                rx.text(
                    f"Última actualización: {LAST_UPDATED}",
                    size="2",
                    color=rx.color("gray", 10),
                    text_align="center",
                ),
                rx.text(
                    "Esta política explica qué son las cookies, cuáles utilizamos en E-Learning JCB y cómo puedes gestionarlas.",
                    size="3",
                    color=rx.color("gray", 11),
                    text_align="center",
                    max_width="620px",
                ),
                align_items="center",
                spacing="4",
                padding_y="3em",
                width="100%",
            ),
            rx.vstack(
                # Secciones informativas
                *[
                    info_card(s["icon"], s["color"], s["title"], s["content"])
                    for s in SECTIONS
                ],
                # Tipos de cookies
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.box(
                                rx.icon("list", size=18, color="white"),
                                background=rx.color("gray", 9),
                                padding="0.5em",
                                border_radius="9px",
                                flex_shrink="0",
                            ),
                            rx.heading("Tipos de cookies que utilizamos", size="4"),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.vstack(
                            *[
                                cookie_type_card(
                                    ct["name"],
                                    ct["color"],
                                    ct["icon"],
                                    ct["required"],
                                    ct["description"],
                                    ct["examples"],
                                )
                                for ct in COOKIE_TYPES
                            ],
                            spacing="4",
                            width="100%",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    width="100%",
                ),
                # Gestión de cookies
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.box(
                                rx.icon("settings-2", size=18, color="white"),
                                background=rx.color("green", 9),
                                padding="0.5em",
                                border_radius="9px",
                                flex_shrink="0",
                            ),
                            rx.heading("Cómo gestionar las cookies", size="4"),
                            spacing="3",
                            align_items="center",
                        ),
                        rx.text(
                            "Puedes controlar y/o eliminar las cookies cuando quieras. A continuación te indicamos cómo hacerlo en los principales navegadores:",
                            size="2",
                            color=rx.color("gray", 11),
                        ),
                        rx.grid(
                            *[
                                rx.hstack(
                                    rx.icon("monitor", size=16, color=rx.color("blue", 9)),
                                    rx.text(browser, size="2", weight="medium"),
                                    spacing="2",
                                    align_items="center",
                                    background=rx.color("gray", 2),
                                    padding="0.6em 1em",
                                    border_radius="8px",
                                )
                                for browser in ["Chrome", "Firefox", "Safari", "Edge", "Opera", "Samsung Internet"]
                            ],
                            columns=rx.breakpoints(initial="2", sm="3"),
                            spacing="3",
                            width="100%",
                        ),
                        rx.text(
                            "Ten en cuenta que deshabilitar las cookies técnicas puede afectar al funcionamiento de la plataforma e impedir el acceso a determinadas funcionalidades como el inicio de sesión.",
                            size="2",
                            color=rx.color("orange", 11),
                            background=rx.color("orange", 2),
                            padding="0.8em 1em",
                            border_radius="8px",
                            border_left=f"3px solid {rx.color('orange', 8)}",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                    width="100%",
                ),
                # Contacto
                rx.card(
                    rx.hstack(
                        rx.box(
                            rx.icon("mail", size=22, color="white"),
                            background=rx.color("blue", 9),
                            padding="0.65em",
                            border_radius="10px",
                            flex_shrink="0",
                        ),
                        rx.vstack(
                            rx.text("¿Tienes dudas sobre nuestra política de cookies?", size="3", weight="bold"),
                            rx.text(
                                "Escríbenos a cookies@elearningjcb.com o usa el formulario de contacto.",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="1",
                            align_items="start",
                        ),
                        rx.link(
                            rx.button("Contactar", color_scheme="blue", size="2"),
                            href="/contact",
                        ),
                        spacing="4",
                        align_items="center",
                        flex_wrap="wrap",
                        width="100%",
                    ),
                    width="100%",
                ),
                spacing="4",
                width="100%",
            ),
            max_width="860px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
            padding_bottom="4em",
        ),
        footer(),
        width="100%",
    )
