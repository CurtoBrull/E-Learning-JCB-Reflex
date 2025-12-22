"""
Página de inicio de sesión (login).

Proporciona el formulario de autenticación para que los usuarios accedan
a la plataforma con sus credenciales (email y contraseña).

Funcionalidades:
- Formulario de login con validación
- Mensajes de error y éxito
- Redirección automática al dashboard según rol del usuario
- Link a página de registro para nuevos usuarios

Ruta: /login
Acceso: Pública
Estado: AuthState para manejar autenticación
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.components.navbar import navbar


def login_page() -> rx.Component:
    """
    Renderizar la página de inicio de sesión.

    Muestra un formulario con campos de email y contraseña. Al enviar,
    AuthState.handle_login() valida las credenciales y redirige al
    dashboard correspondiente según el rol del usuario.

    Returns:
        rx.Component: Página con formulario de login

    Eventos:
        - on_submit: AuthState.handle_login
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.heading(
                    "Iniciar Sesión",
                    size="9",
                    margin_bottom="2",
                    text_align="center",
                ),
                rx.text(
                    "Accede a tu cuenta de E-Learning JCB",
                    size="5",
                    color=rx.color("gray", 11),
                    margin_bottom="8",
                    text_align="center",
                ),
                # Mensaje de éxito
                rx.cond(
                    AuthState.success != "",
                    rx.callout(
                        AuthState.success,
                        icon="check_check",
                        color_scheme="green",
                        margin_bottom="4",
                    ),
                ),
                # Mensaje de error
                rx.cond(
                    AuthState.error != "",
                    rx.callout(
                        AuthState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Formulario de login
                rx.card(
                    rx.vstack(
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
                                value=AuthState.login_email,
                                on_change=AuthState.set_login_email,
                                size="3",
                                width="100%",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Campo de contraseña
                        rx.vstack(
                            rx.text(
                                "Contraseña",
                                size="3",
                                weight="bold",
                            ),
                            rx.input(
                                placeholder="Tu contraseña",
                                type="password",
                                value=AuthState.login_password,
                                on_change=AuthState.set_login_password,
                                size="3",
                                width="100%",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Botón de login
                        rx.button(
                            rx.cond(
                                AuthState.loading,
                                rx.hstack(
                                    rx.spinner(size="2"),
                                    rx.text("Iniciando sesión..."),
                                    spacing="2",
                                ),
                                rx.text("Iniciar Sesión"),
                            ),
                            on_click=AuthState.handle_login,
                            disabled=AuthState.loading,
                            color_scheme="blue",
                            size="3",
                            width="100%",
                        ),
                        # Enlace para registrarse
                        rx.hstack(
                            rx.text(
                                "¿No tienes una cuenta?",
                                size="2",
                                color=rx.color("gray", 11),
                            ),
                            rx.link(
                                "Regístrate aquí",
                                href="/register",
                                size="2",
                                color=rx.color("blue", 11),
                            ),
                            spacing="2",
                            justify="center",
                            width="100%",
                        ),
                        spacing="5",
                        width="100%",
                    ),
                    size="4",
                    width="100%",
                    max_width="450px",
                ),
                # Información adicional
                rx.box(
                    rx.vstack(
                        rx.heading(
                            "¿Olvidaste tu contraseña?",
                            size="5",
                            margin_bottom="2",
                        ),
                        rx.text(
                            "Contacta con soporte en contacto@elearningjcb.com",
                            size="3",
                            color=rx.color("gray", 11),
                        ),
                        spacing="2",
                        padding="6",
                        text_align="center",
                    ),
                    width="100%",
                    max_width="450px",
                    margin_top="6",
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
