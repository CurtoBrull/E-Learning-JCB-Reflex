"""
Página de catálogo de instructores de la plataforma E-Learning JCB.

Este módulo muestra el directorio completo de todos los instructores
registrados en la plataforma. Los instructores se presentan en una
cuadrícula utilizando el componente instructor_card.

Funcionalidades:
- Directorio completo de instructores de la plataforma
- Visualización en cuadrícula responsive (4 columnas)
- Estado de carga mientras se obtienen los datos
- Manejo de errores con mensajes visuales
- Carga automática de instructores al montar la página

Ruta: /instructors
Acceso: Pública (sin autenticación requerida)
Estado: InstructorState para cargar y mostrar todos los instructores
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.instructor_state import InstructorState
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.instructor_card import instructor_card


def instructors_page() -> rx.Component:
    """
    Renderiza la página con el catálogo completo de instructores.

    Muestra todos los instructores registrados en la plataforma
    organizados en una cuadrícula de 4 columnas. Cada instructor
    se renderiza usando el componente instructor_card que muestra
    información básica y permite navegar a su perfil detallado.

    Returns:
        rx.Component: Componente de Reflex con el directorio de instructores

    Notas:
        - Utiliza on_mount para cargar automáticamente los instructores al abrir la página
        - Muestra un spinner mientras InstructorState.loading es True
        - Muestra callout de error si InstructorState.error no está vacío
        - La cuadrícula solo se muestra si hay instructores disponibles
    """
    return rx.box(
        # Background image
        rx.box(
            position="fixed",
            top="0",
            left="0",
            width="100%",
            height="100%",
            background_image="url(/images/bg/background_login.webp)",
            background_size="cover",
            background_position="center",
            background_repeat="no-repeat",
            opacity="0.15",
            z_index="-1",
        ),
        rx.vstack(
            navbar(),
            rx.container(
                rx.vstack(
                    rx.heading(
                        "Nuestros Instructores",
                        size="8",
                        margin_bottom="4",
                        text_align="center",
                    ),
                # Mensaje de error
                rx.cond(
                    InstructorState.error != "",
                    rx.callout(
                        InstructorState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Estado de carga
                rx.cond(
                    InstructorState.loading,
                    rx.spinner(size="3"),
                ),
                # Cuadrícula de instructores usando instructor_card
                rx.cond(
                    InstructorState.instructors.length() > 0,
                    rx.grid(
                        rx.foreach(
                            InstructorState.instructors,
                            lambda instructor: instructor_card(instructor)
                        ),
                        columns="4",
                        spacing="6",
                    ),
                ),
                spacing="4",
                width="100%",
                padding_y="8",
                align_items="center",
                on_mount=InstructorState.load_instructors,
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
