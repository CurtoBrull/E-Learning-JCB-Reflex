"""
Componente de footer (pie de página).

Este módulo define el footer responsive de la aplicación que se muestra
en todas las páginas. Incluye:
- Información de la plataforma
- Enlaces a páginas importantes
- Enlaces a redes sociales
- Información de contacto
- Copyright y versión

El footer se adapta a dispositivos móviles, tabletas y escritorio.
"""

import reflex as rx


def footer_link(text: str, url: str) -> rx.Component:
    """
    Crear un enlace estilizado para el footer.

    Args:
        text: Texto a mostrar en el enlace
        url: URL de destino del enlace

    Returns:
        rx.Component: Link con estilo consistente para el footer

    Ejemplo:
        >>> footer_link("Sobre Nosotros", "/about")
    """
    return rx.link(
        rx.text(
            text,
            size="2",
            color=rx.color("gray", 11),
            _hover={"color": rx.color("purple", 9)},
        ),
        href=url,
    )


def footer_section_title(text: str) -> rx.Component:
    """
    Crear un título para una sección del footer.

    Args:
        text: Texto del título

    Returns:
        rx.Component: Título estilizado para sección del footer
    """
    return rx.heading(
        text,
        size="4",
        weight="bold",
        margin_bottom="0.5em",
    )


def social_link(icon: str, url: str, label: str) -> rx.Component:
    """
    Crear un enlace a red social con icono.

    Args:
        icon: Nombre del icono de Reflex
        url: URL de la red social
        label: Etiqueta accesible para el enlace

    Returns:
        rx.Component: Enlace con icono de red social
    """
    return rx.link(
        rx.icon(
            icon,
            size=20,
            color=rx.color("gray", 11),
            _hover={"color": rx.color("purple", 9)},
        ),
        href=url,
        aria_label=label,
        target="_blank",
    )


def footer() -> rx.Component:
    """
    Renderiza el footer completo de la aplicación.

    Estructura del footer:
    - Sección 1: Sobre E-Learning JCB (descripción y redes sociales)
    - Sección 2: Enlaces rápidos (navegación principal)
    - Sección 3: Recursos (documentación y ayuda)
    - Sección 4: Contacto (información de contacto)
    - Barra inferior: Copyright y versión

    Returns:
        rx.Component: Footer completo y responsive

    Notas:
        - Usa grid responsive (1 columna en móvil, 4 en desktop)
        - Incluye separador visual antes del copyright
        - Todos los enlaces externos se abren en nueva pestaña
    """
    return rx.box(
        rx.center(
            rx.container(
                # Secciones principales del footer
                rx.grid(
                    # Sección 1: Sobre la plataforma
                    rx.vstack(
                        footer_section_title("E-Learning JCB"),
                        rx.text(
                            "Plataforma de aprendizaje en línea para desarrollo profesional y técnico.",
                            size="2",
                            color=rx.color("gray", 10),
                            margin_bottom="1em",
                        ),
                        rx.hstack(
                            social_link("github", "https://github.com", "GitHub"),
                            social_link("linkedin", "https://linkedin.com", "LinkedIn"),
                            social_link("twitter", "https://twitter.com", "Twitter"),
                            social_link("youtube", "https://youtube.com", "YouTube"),
                            spacing="3",
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                # Sección 2: Enlaces rápidos
                rx.vstack(
                    footer_section_title("Enlaces Rápidos"),
                    footer_link("Inicio", "/"),
                    footer_link("Cursos", "/courses"),
                    footer_link("Instructores", "/instructors"),
                    footer_link("Sobre Nosotros", "/about"),
                    align_items="start",
                    spacing="2",
                ),
                # Sección 3: Recursos
                rx.vstack(
                    footer_section_title("Recursos"),
                    footer_link("Documentación", "/docs"),
                    footer_link("Ayuda", "/help"),
                    footer_link("Preguntas Frecuentes", "/faq"),
                    footer_link("Blog", "/blog"),
                    align_items="start",
                    spacing="2",
                ),
                # Sección 4: Contacto
                rx.vstack(
                    footer_section_title("Contacto"),
                    rx.hstack(
                        rx.icon("mail", size=16, color=rx.color("gray", 10)),
                        rx.text(
                            "info@elearningjcb.com",
                            size="2",
                            color=rx.color("gray", 10),
                        ),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("phone", size=16, color=rx.color("gray", 10)),
                        rx.text(
                            "+34 123 456 789",
                            size="2",
                            color=rx.color("gray", 10),
                        ),
                        spacing="2",
                    ),
                    rx.hstack(
                        rx.icon("map-pin", size=16, color=rx.color("gray", 10)),
                        rx.text(
                            "Madrid, España",
                            size="2",
                            color=rx.color("gray", 10),
                        ),
                        spacing="2",
                    ),
                    align_items="start",
                    spacing="2",
                ),
                columns=rx.breakpoints(initial="1", sm="2", md="4"),
                spacing="6",
                width="100%",
                padding_y="3em",
            ),
            # Divider
            rx.divider(margin_y="2em"),
                # Copyright y versión
                rx.hstack(
                    rx.text(
                        f"© 2024-2026 E-Learning JCB. Todos los derechos reservados.",
                        size="2",
                        color=rx.color("gray", 10),
                    ),
                    rx.spacer(),
                    rx.hstack(
                        footer_link("Privacidad", "/privacy"),
                        footer_link("Términos", "/terms"),
                        footer_link("Cookies", "/cookies"),
                        spacing="4",
                        display=rx.breakpoints(initial="none", md="flex"),
                    ),
                    width="100%",
                    padding_bottom="2em",
                ),
                # Links adicionales en móvil
                rx.hstack(
                    footer_link("Privacidad", "/privacy"),
                    footer_link("Términos", "/terms"),
                    footer_link("Cookies", "/cookies"),
                    spacing="4",
                    display=rx.breakpoints(initial="flex", md="none"),
                    justify_content="center",
                    width="100%",
                    padding_bottom="2em",
                ),
                max_width="1400px",
            ),
            width="100%",
        ),
        width="100%",
        background=rx.color("gray", 2),
        border_top=f"1px solid {rx.color('gray', 5)}",
        margin_top="4em",
    )
