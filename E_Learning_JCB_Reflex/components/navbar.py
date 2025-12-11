"""Componente de navegación principal."""

import reflex as rx


def navbar_link(text: str, url: str) -> rx.Component:
    """Enlace de la barra de navegación."""
    return rx.link(rx.text(text, size="4", weight="medium"), href=url)


def navbar() -> rx.Component:
    """Barra de navegación principal."""
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/E-Learning-JCB.png",
                        width="2.25em",
                        height="auto",
                        border_radius="25%",
                    ),
                    rx.heading("E-Learning JCB", size="7", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Inicio", "/"),
                    navbar_link("Cursos", "/courses"),
                    navbar_link("Instructores", "/instructors"),
                    navbar_link("Contacto", "/contact"),
                    navbar_link("Login", "/login"),
                    rx.color_mode.button(),
                    justify="end",
                    spacing="5",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.image(
                        src="/E-Learning-JCB.png", width="2em", height="auto", border_radius="25%"
                    ),
                    rx.heading("E-Learning JCB", size="6", weight="bold"),
                    align_items="center",
                ),
                rx.hstack(
                    rx.color_mode.button(),
                    rx.menu.root(
                        rx.menu.trigger(rx.icon("menu", size=30)),
                        rx.menu.content(
                            rx.menu.item(rx.link("Inicio", href="/")),
                            rx.menu.item(rx.link("Cursos", href="/courses")),
                            rx.menu.item(rx.link("Instructores", href="/instructors")),
                            rx.menu.item(rx.link("Contacto", href="/contact")),
                            rx.menu.item(rx.link("Login", href="/login")),
                        ),
                        justify="end",
                    ),
                    spacing="3",
                    align_items="center",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg=rx.color("accent", 3),
        padding="1em",
        # position="fixed",
        # top="0px",
        # z_index="5",
        width="100%",
    )
