"""
Página de perfil detallado de un instructor en la plataforma E-Learning JCB.

Este módulo muestra toda la información de un instructor específico,
incluyendo sus datos personales, estadísticas y todos los cursos que
imparte en la plataforma.

Funcionalidades:
- Perfil completo del instructor con avatar grande
- Información personal (nombre, email, expertise, biografía)
- Estadísticas del instructor (cursos creados, total de estudiantes)
- Cuadrícula con todos los cursos que imparte
- Cada curso muestra: imagen, título, descripción, nivel, precio, estudiantes y rating
- Carga dinámica del instructor desde la URL

Ruta: /instructors/[instructor_id]
Acceso: Pública (sin autenticación requerida)
Estado: InstructorState para cargar información del instructor y sus cursos
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.instructor_state import InstructorState
from E_Learning_JCB_Reflex.components.navbar import navbar


def instructor_detail_page() -> rx.Component:
    """
    Renderiza la página completa de perfil de un instructor.

    Muestra toda la información del instructor organizada en secciones:
    1. Header con avatar grande y datos personales (nombre, expertise, email, biografía)
    2. Estadísticas (total de cursos creados, total de estudiantes)
    3. Cuadrícula con todos los cursos que imparte el instructor

    Returns:
        rx.Component: Componente de Reflex con el perfil completo del instructor

    Notas:
        - Utiliza on_mount con InstructorState.load_instructor_from_url para cargar desde URL
        - Muestra spinner mientras InstructorState.loading es True
        - Muestra callout de error si InstructorState.error no está vacío
        - El contenido solo se muestra si instructor_name no está vacío
        - Los cursos se muestran en cuadrícula de 3 columnas con hover effects
        - Cada curso es clickeable y redirige a /courses/{course_id}
        - Max width de 1200px para mejor legibilidad
    """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Estado de carga
                rx.cond(
                    InstructorState.loading,
                    rx.center(
                        rx.spinner(size="3"),
                        height="50vh",
                    ),
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
                # Contenido del instructor
                rx.cond(
                    (InstructorState.instructor_name != "") & (InstructorState.loading == False),
                    rx.vstack(
                        # SECCIÓN 1: HEADER CON AVATAR E INFO PRINCIPAL
                        rx.box(
                            rx.hstack(
                                # Avatar del instructor
                                rx.box(
                                    rx.avatar(
                                        src=InstructorState.instructor_avatar,
                                        fallback="IN",
                                        size="9",
                                        radius="full",
                                    ),
                                    width="200px",
                                    flex_shrink="0",
                                    display="flex",
                                    justify_content="center",
                                    align_items="center",
                                ),
                                # Info principal
                                rx.vstack(
                                    rx.heading(
                                        InstructorState.instructor_name,
                                        size="9",
                                        color=rx.color("gray", 12),
                                    ),
                                    rx.cond(
                                        InstructorState.instructor_expertise != "",
                                        rx.badge(
                                            InstructorState.instructor_expertise,
                                            color_scheme="purple",
                                            size="3",
                                        ),
                                    ),
                                    rx.text(
                                        InstructorState.instructor_email,
                                        size="3",
                                        color=rx.color("gray", 12),
                                    ),
                                    rx.cond(
                                        InstructorState.instructor_bio != "",
                                        rx.text(
                                            InstructorState.instructor_bio,
                                            size="4",
                                            margin_top="4",
                                            color=rx.color("gray", 12),
                                        ),
                                    ),
                                    align_items="start",
                                    spacing="3",
                                    flex="1",
                                ),
                                spacing="6",
                                width="100%",
                                align_items="center",
                            ),
                            width="100%",
                            padding="6",
                            border_radius="5px",
                        ),
                        # SECCIÓN 2: ESTADÍSTICAS
                        rx.hstack(
                            rx.box(
                                rx.text("Cursos", size="2"),
                                rx.text(
                                    InstructorState.total_courses,
                                    size="6",
                                    weight="bold",
                                ),
                                padding="4",
                                text_align="center",
                                flex="1",
                            ),
                            rx.box(
                                rx.text("Estudiantes", size="2"),
                                rx.text(
                                    InstructorState.total_students,
                                    size="6",
                                    weight="bold",
                                ),
                                padding="4",
                                text_align="center",
                                flex="1",
                            ),
                            spacing="4",
                            width="100%",
                            margin_top="4",
                        ),
                        # SECCIÓN 3: CURSOS DEL INSTRUCTOR
                        rx.cond(
                            InstructorState.courses.length() > 0,
                            rx.box(
                                rx.heading("Cursos impartidos", size="6", margin_bottom="3"),
                                rx.grid(
                                    rx.foreach(
                                        InstructorState.courses,
                                        lambda course: rx.link(
                                            rx.box(
                                                rx.vstack(
                                                    rx.image(
                                                        src=course["thumbnail"],
                                                        height="150px",
                                                        width="100%",
                                                        object_fit="cover",
                                                        border_radius="5px 5px 0 0",
                                                    ),
                                                    rx.vstack(
                                                        rx.heading(
                                                            course["title"],
                                                            size="4",
                                                        ),
                                                        rx.text(
                                                            course["description"],
                                                            size="2",
                                                            no_of_lines=2,
                                                        ),
                                                        rx.hstack(
                                                            rx.badge(
                                                                course["level"],
                                                                color_scheme="blue",
                                                            ),
                                                            rx.spacer(),
                                                            rx.text(
                                                                f"${course['price']:.2f}",
                                                                weight="bold",
                                                                color="green",
                                                            ),
                                                            width="100%",
                                                        ),
                                                        rx.hstack(
                                                            rx.text(
                                                                f"{course['students_count']} estudiantes",
                                                                size="1",
                                                            ),
                                                            rx.text(
                                                                f"★ {course['average_rating']}/5",
                                                                size="1",
                                                                color="orange",
                                                            ),
                                                            spacing="2",
                                                        ),
                                                        spacing="2",
                                                        padding="3",
                                                        align_items="start",
                                                        width="100%",
                                                    ),
                                                    spacing="0",
                                                    width="100%",
                                                ),
                                                border_radius="5px",
                                                box_shadow="5px 5px 10px 5px rgba(0, 0, 0, 0.3)",
                                                overflow="hidden",
                                                _hover={
                                                    "box_shadow": "5px 5px 15px rgba(0, 0, 0, 0.5)",
                                                    "transform": "translateY(-2px)",
                                                },
                                                transition="all 0.2s",
                                            ),
                                            href=f"/courses/{course['id']}",
                                            text_decoration="none",
                                            color="inherit",
                                        ),
                                    ),
                                    columns="3",
                                    spacing="4",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        spacing="4",
                        width="100%",
                        padding_y="8",
                    ),
                ),
                spacing="4",
                width="100%",
                on_mount=InstructorState.load_instructor_from_url,
            ),
            width="100%",
            max_width="1200px",
            padding_x="2rem",
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
        align_items="center",
    )
