"""
Componente de tarjeta de instructor (instructor card).

Este módulo define el componente visual de tarjeta que representa un instructor
en las páginas de listado de instructores. Cada tarjeta muestra información
del instructor y es clicable para navegar a su perfil detallado.

Características visuales:
- Avatar circular del instructor con fallback
- Nombre del instructor
- Badge de área de expertise (opcional)
- Biografía limitada a 3 líneas
- Estadísticas (número de cursos creados)
- Efectos hover para interactividad (elevación y sombra)
"""

import reflex as rx


def instructor_card(instructor: dict) -> rx.Component:
    """
    Crear una tarjeta visual para mostrar información de un instructor.

    Genera un componente de tarjeta clicable que muestra la información
    esencial de un instructor. Al hacer clic, redirige a la página de perfil
    del instructor (/instructors/[instructor_id]).

    Args:
        instructor: Diccionario con la información del instructor. Campos esperados:
            - id (str): ID del instructor para la URL
            - avatar (str): URL de la imagen de perfil del instructor
            - name (str): Nombre completo del instructor
            - expertise (str, opcional): Área de especialización
            - bio (str): Biografía del instructor
            - total_courses (int): Número total de cursos creados

    Returns:
        rx.Component: Tarjeta de instructor completa y estilizada

    Ejemplo:
        >>> instructor_data = {
        ...     "id": "456",
        ...     "name": "María García",
        ...     "expertise": "Data Science",
        ...     "bio": "Experta en ciencia de datos con 10 años de experiencia",
        ...     "total_courses": 12
        ... }
        >>> card = instructor_card(instructor_data)

    Nota:
        - El avatar usa fallback="IN" si no hay imagen disponible
        - El badge de expertise solo se muestra si el campo no está vacío
        - La biografía se limita a 3 líneas con no_of_lines=3
        - Los valores por defecto se usan si faltan campos en el diccionario
    """
    return rx.link(
        rx.box(
            rx.vstack(
                # Avatar del instructor
                rx.box(
                    rx.avatar(
                        src=instructor.get("avatar", ""),
                        fallback="IN",
                        size="9",
                        radius="full",
                    ),
                    width="100%",
                    display="flex",
                    justify_content="center",
                    align_items="center",
                    padding_top="4",
                    padding_bottom="4",
                ),
                # Nombre del instructor con altura fija
                rx.box(
                    rx.heading(
                        instructor.get("name", "Instructor"),
                        size="6",
                        text_align="center",
                        no_of_lines=2,
                    ),
                    min_height="3.5rem",
                    width="100%",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                    padding_x="4px",
                ),
                # Expertise con altura fija
                rx.box(
                    rx.cond(
                        instructor.get("expertise", "") != "",
                        rx.badge(
                            instructor.get("expertise", ""),
                            color_scheme="purple",
                            size="2",
                        ),
                    ),
                    min_height="1.5rem",
                    display="flex",
                    align_items="center",
                    justify_content="center",
                ),
                # Bio con altura fija
                rx.box(
                    rx.text(
                        instructor.get("bio", "Sin biografía disponible"),
                        color=rx.color("gray", 12),
                        size="2",
                        no_of_lines=3,
                        text_align="center",
                    ),
                    min_height="4.5rem",
                    width="100%",
                    padding_x="4px",
                ),
                # Espaciador para empujar estadísticas hacia abajo
                rx.spacer(),
                # Estadísticas
                rx.hstack(
                    rx.vstack(
                        rx.text(
                            instructor.get("total_courses", 0),
                            font_weight="bold",
                            size="4",
                        ),
                        rx.text(
                            "Cursos",
                            size="1",
                            color=rx.color("gray", 12)
                        ),
                        spacing="0",
                        align_items="center",
                    ),
                    width="100%",
                    justify_content="center",
                    padding="3",
                ),
                spacing="3",
                align_items="center",
                width="100%",
                height="100%",
            ),
            border_radius="5px",
            box_shadow="5px 5px 15px rgba(0, 0, 0, 0.5)",
            overflow="hidden",
            transition_property="box-shadow, border-color, transform",
            transition_duration="200ms",
            transition_timing_function="ease-in-out",
            _hover={
                "box_shadow": "6px 6px 20px rgba(0, 0, 0, 0.5)",
                "transform": "translateY(-4px)",
                "cursor": "pointer",
            },
            padding="4",
            height="420px",
            display="flex",
            flex_direction="column",
        ),
        href=f"/instructors/{instructor.get('id', '')}",
        text_decoration="none",
        color="inherit",
        _hover={"text_decoration": "none"},
    )
