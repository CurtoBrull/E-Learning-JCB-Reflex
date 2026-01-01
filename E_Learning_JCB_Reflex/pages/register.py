"""
Página de registro de nuevos usuarios en la plataforma E-Learning JCB.

Este módulo proporciona el formulario de registro para que nuevos usuarios
puedan crear una cuenta en la plataforma. Permite seleccionar el rol
(estudiante, instructor o administrador) durante el proceso de registro.

Funcionalidades:
- Formulario de registro con validación
- Campos: nombre, apellido, email, contraseña, confirmación de contraseña y rol
- Mensajes de éxito y error
- Redirección automática al login después del registro exitoso
- Link a página de login para usuarios existentes

Ruta: /register
Acceso: Pública (sin autenticación requerida)
Estado: AuthState para manejar el proceso de registro
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.components.navbar import navbar


def register_page() -> rx.Component:
    """
    Renderiza la página de registro de nuevos usuarios.

    Muestra un formulario completo de registro que incluye:
    - Campos de nombre y apellido (en una fila horizontal)
    - Campo de email con validación de formato
    - Campo de contraseña (mínimo 6 caracteres)
    - Campo de confirmación de contraseña
    - Selector de rol de usuario (student, instructor, admin)
    - Descripción de cada tipo de rol disponible
    - Botón de envío con estado de carga
    - Link a la página de login

    Returns:
        rx.Component: Componente de Reflex con el formulario de registro completo

    Notas:
        - Utiliza AuthState para manejar la lógica de validación y creación de usuario
        - Muestra callouts de éxito/error basados en AuthState.success y AuthState.error
        - El formulario está limitado a un max_width de 550px para mejor legibilidad
    """
    return rx.box(
        # Background image
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background_image="url(/images/bg/background_register.webp)",
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            opacity="0.3",
            z_index="-1",
        ),
        rx.vstack(
            navbar(),
            rx.container(
                rx.vstack(
                    # Header
                    rx.heading(
                        "Crear Cuenta",
                        size="9",
                        margin_bottom="2",
                        text_align="center",
                    ),
                    rx.text(
                        "Únete a E-Learning JCB y comienza a aprender",
                        size="5",
                        color=rx.color("gray", 12),
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
                # Formulario de registro
                rx.card(
                    rx.vstack(
                        # Campos de nombre
                        rx.hstack(
                            rx.vstack(
                                rx.text(
                                    "Nombre",
                                    size="3",
                                    weight="bold",
                                ),
                                rx.input(
                                    placeholder="Tu nombre",
                                    value=AuthState.register_first_name,
                                    on_change=AuthState.set_register_first_name,
                                    size="3",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="2",
                            ),
                            rx.vstack(
                                rx.text(
                                    "Apellido",
                                    size="3",
                                    weight="bold",
                                ),
                                rx.input(
                                    placeholder="Tu apellido",
                                    value=AuthState.register_last_name,
                                    on_change=AuthState.set_register_last_name,
                                    size="3",
                                    width="100%",
                                ),
                                width="100%",
                                spacing="2",
                            ),
                            width="100%",
                            spacing="3",
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
                                value=AuthState.register_email,
                                on_change=AuthState.set_register_email,
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
                                placeholder="Mínimo 6 caracteres",
                                type="password",
                                value=AuthState.register_password,
                                on_change=AuthState.set_register_password,
                                size="3",
                                width="100%",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Confirmar contraseña
                        rx.vstack(
                            rx.text(
                                "Confirmar Contraseña",
                                size="3",
                                weight="bold",
                            ),
                            rx.input(
                                placeholder="Repite tu contraseña",
                                type="password",
                                value=AuthState.register_confirm_password,
                                on_change=AuthState.set_register_confirm_password,
                                size="3",
                                width="100%",
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Selección de rol
                        rx.vstack(
                            rx.text(
                                "Tipo de cuenta",
                                size="3",
                                weight="bold",
                            ),
                            rx.select(
                                ["student", "instructor", "admin"],
                                placeholder="Selecciona tu rol",
                                value=AuthState.register_role,
                                on_change=AuthState.set_register_role,
                                size="3",
                                width="100%",
                            ),
                            rx.text(
                                "• Student: Para aprender cursos",
                                size="2",
                                color=rx.color("gray", 12),
                            ),
                            rx.text(
                                "• Instructor: Para crear y enseñar cursos",
                                size="2",
                                color=rx.color("gray", 12),
                            ),
                            rx.text(
                                "• Admin: Gestión completa de la plataforma",
                                size="2",
                                color=rx.color("gray", 12),
                            ),
                            width="100%",
                            spacing="2",
                        ),
                        # Botón de registro
                        rx.button(
                            rx.cond(
                                AuthState.loading,
                                rx.hstack(
                                    rx.spinner(size="2"),
                                    rx.text("Creando cuenta..."),
                                    spacing="2",
                                ),
                                rx.text("Crear Cuenta"),
                            ),
                            on_click=AuthState.handle_register,
                            disabled=AuthState.loading,
                            color_scheme="blue",
                            size="3",
                            width="100%",
                        ),
                        # Enlace para login
                        rx.hstack(
                            rx.text(
                                "¿Ya tienes una cuenta?",
                                size="2",
                                color=rx.color("gray", 11),
                            ),
                            rx.link(
                                "Inicia sesión aquí",
                                href="/login",
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
                    max_width="550px",
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
        ),
        width="100%",
        position="relative",
    )
