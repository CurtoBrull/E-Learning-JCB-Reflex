"""Página de contacto de la plataforma E-Learning JCB."""

import reflex as rx
from E_Learning_JCB_Reflex.states.contact_state import ContactState
from E_Learning_JCB_Reflex.components.navbar import navbar


def contact_page() -> rx.Component:
    """Página de contacto con formulario."""
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.heading(
                    "Contáctanos",
                    size="9",
                    margin_bottom="2",
                    text_align="center",
                ),
                rx.text(
                    "¿Tienes alguna pregunta o sugerencia? Estamos aquí para ayudarte",
                    size="5",
                    color=rx.color("gray", 11),
                    margin_bottom="8",
                    text_align="center",
                ),
                # Mensaje de éxito
                rx.cond(
                    ContactState.success,
                    rx.callout(
                        "¡Mensaje enviado con éxito! Nos pondremos en contacto contigo pronto.",
                        icon="check_check",
                        color_scheme="green",
                        margin_bottom="4",
                    ),
                ),
                # Mensaje de error
                rx.cond(
                    ContactState.error != "",
                    rx.callout(
                        ContactState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Formulario de contacto
                rx.card(
                    rx.vstack(
                        # Campo de nombre
                        rx.vstack(
                            rx.text(
                                "Nombre",
                                size="3",
                                weight="bold",
                            ),
                            rx.input(
                                placeholder="Tu nombre completo",
                                value=ContactState.name,
                                on_change=ContactState.set_name,
                                size="3",
                                width="100%",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Campo de email
                        rx.vstack(
                            rx.text(
                                "Email",
                                size="3",
                                weight="bold",
                            ),
                            rx.input(
                                placeholder="tu.email@ejemplo.com",
                                type="email",
                                value=ContactState.email,
                                on_change=ContactState.set_email,
                                size="3",
                                width="100%",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Campo de mensaje
                        rx.vstack(
                            rx.text(
                                "Mensaje",
                                size="3",
                                weight="bold",
                            ),
                            rx.text_area(
                                placeholder="Escribe tu mensaje aquí...",
                                value=ContactState.message,
                                on_change=ContactState.set_message,
                                size="3",
                                width="100%",
                                min_height="200px",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Botones
                        rx.hstack(
                            rx.button(
                                "Limpiar",
                                on_click=ContactState.reset_form,
                                variant="soft",
                                color_scheme="gray",
                                size="3",
                            ),
                            rx.button(
                                rx.cond(
                                    ContactState.loading,
                                    rx.hstack(
                                        rx.spinner(size="2"),
                                        rx.text("Enviando..."),
                                        spacing="2",
                                    ),
                                    rx.text("Enviar Mensaje"),
                                ),
                                on_click=ContactState.submit_contact,
                                disabled=ContactState.loading,
                                color_scheme="blue",
                                size="3",
                            ),
                            justify="end",
                            width="100%",
                            spacing="3",
                        ),
                        spacing="5",
                        width="100%",
                    ),
                    size="4",
                    width="100%",
                    max_width="600px",
                ),
                # Información adicional
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "Otras formas de contacto",
                            size="6",
                            margin_bottom="4",
                        ),
                        rx.vstack(
                            rx.hstack(
                                rx.icon("mail", size=20),
                                rx.text(
                                    "Email: contacto@elearningjcb.com",
                                    size="3",
                                ),
                                spacing="3",
                            ),
                            rx.hstack(
                                rx.icon("phone", size=20),
                                rx.text(
                                    "Teléfono: +34 123 456 789",
                                    size="3",
                                ),
                                spacing="3",
                            ),
                            rx.hstack(
                                rx.icon("map_pin", size=20),
                                rx.text(
                                    "Dirección: Calle Elearning Nº 1, Almería, España",
                                    size="3",
                                ),
                                spacing="3",
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                        spacing="4",
                        padding="6",
                    ),
                    width="100%",
                    max_width="600px",
                    margin_top="8",
                ),
                spacing="6",
                width="100%",
                padding_y="8",
                align_items="center",
            ),
            width="100%",
            max_width="100%",
            padding_x="2rem",
        ),
        width="100%",
        spacing="0",
    )
