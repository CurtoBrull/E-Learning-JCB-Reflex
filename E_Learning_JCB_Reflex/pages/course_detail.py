"""
Página de detalles de un curso específico en la plataforma E-Learning JCB.

Este módulo muestra toda la información detallada de un curso individual,
incluyendo descripción, instructor, lecciones, reviews y permite la inscripción
de estudiantes autenticados.

Funcionalidades:
- Vista completa del curso con toda su información
- Sección de instructor con avatar, nombre, email y biografía
- Estadísticas del curso (estudiantes, rating, reviews)
- Lista de categorías del curso
- Contenido del curso (lecciones con duración)
- Opiniones y valoraciones de estudiantes
- Botón de inscripción (solo para estudiantes autenticados)
- Diálogo de resultado de inscripción con opciones de navegación
- Carga dinámica del curso desde la URL

Ruta: /courses/[course_id]
Acceso: Pública (inscripción solo para usuarios autenticados con rol student)
Estados: CourseState (información del curso), EnrollmentState (inscripciones), AuthState (autenticación)
"""

import reflex as rx
from E_Learning_JCB_Reflex.states.course_state import CourseState
from E_Learning_JCB_Reflex.states.enrollment_state import EnrollmentState
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.utils.route_helpers import get_dynamic_id


def enrollment_result_dialog() -> rx.Component:
    """
    Renderiza un diálogo modal con el resultado de la inscripción.

    Muestra un diálogo diferente según el resultado de la inscripción:
    - Éxito: Muestra mensaje de éxito con 4 opciones de navegación
      (ver lecciones del curso, ir al dashboard, ver detalles del curso, explorar más cursos)
    - Error: Muestra mensaje de error con opciones para reintentar
      o ver otros cursos

    Returns:
        rx.Component: Alert dialog que se muestra/oculta según EnrollmentState.show_enrollment_result_dialog

    Notas:
        - El contenido cambia según EnrollmentState.enrollment_was_successful
        - Incluye iconos descriptivos (check-circle para éxito, triangle-alert para error)
        - Los botones tienen esquemas de color apropiados al resultado
    """
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.cond(
                EnrollmentState.enrollment_was_successful,
                rx.vstack(
                    rx.hstack(
                        rx.icon("circle-check", size=32, color=rx.color("green", 9)),
                        rx.alert_dialog.title("¡Inscripción Exitosa!"),
                        spacing="3",
                        align_items="center",
                    ),
                    rx.alert_dialog.description(
                        EnrollmentState.success,
                        size="3",
                    ),
                    rx.divider(margin_y="4"),
                    rx.text(
                        "¿Qué deseas hacer ahora?",
                        size="3",
                        weight="bold",
                        margin_bottom="3",
                    ),
                    rx.vstack(
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("circle-play", size=18),
                                    rx.text("Ir al Curso"),
                                    spacing="2",
                                ),
                                variant="solid",
                                color_scheme="green",
                                size="3",
                                width="100%",
                            ),
                            href=f"/courses/{EnrollmentState.enrollment_course_id}/view",
                            width="100%",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("graduation-cap", size=18),
                                    rx.text("Ir a Mi Dashboard"),
                                    spacing="2",
                                ),
                                variant="soft",
                                color_scheme="blue",
                                size="3",
                                width="100%",
                            ),
                            href="/student/dashboard",
                            width="100%",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("book-open", size=18),
                                    rx.text("Ver Detalles del Curso"),
                                    spacing="2",
                                ),
                                variant="soft",
                                color_scheme="gray",
                                size="3",
                                width="100%",
                                on_click=EnrollmentState.close_enrollment_result_dialog,
                            ),
                            width="100%",
                        ),
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("search", size=18),
                                    rx.text("Explorar Más Cursos"),
                                    spacing="2",
                                ),
                                variant="soft",
                                color_scheme="gray",
                                size="3",
                                width="100%",
                            ),
                            href="/courses",
                            width="100%",
                        ),
                        spacing="3",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.icon("triangle-alert", size=32, color=rx.color("red", 9)),
                        rx.alert_dialog.title("Error en la Inscripción"),
                        spacing="3",
                        align_items="center",
                    ),
                    rx.alert_dialog.description(
                        EnrollmentState.error,
                        size="3",
                    ),
                    rx.divider(margin_y="4"),
                    rx.vstack(
                        rx.button(
                            "Intentar de Nuevo",
                            variant="solid",
                            color_scheme="blue",
                            size="3",
                            width="100%",
                            on_click=EnrollmentState.close_enrollment_result_dialog,
                        ),
                        rx.link(
                            rx.button(
                                "Ver Otros Cursos",
                                variant="soft",
                                color_scheme="gray",
                                size="3",
                                width="100%",
                            ),
                            href="/courses",
                            width="100%",
                        ),
                        spacing="3",
                        width="100%",
                    ),
                    spacing="3",
                    align_items="start",
                    width="100%",
                ),
            ),
        ),
        open=EnrollmentState.show_enrollment_result_dialog,
    )


def course_detail_page() -> rx.Component:
    """
    Renderiza la página completa de detalles de un curso.

    Muestra toda la información del curso organizada en secciones:
    1. Header con imagen del curso y información principal (título, descripción, nivel, precio)
    2. Información del instructor con avatar y biografía
    3. Estadísticas (estudiantes, rating, reviews)
    4. Categorías del curso
    5. Contenido del curso (lista de lecciones)
    6. Opiniones de estudiantes (reviews)
    7. Botón de inscripción (condicional según autenticación y rol)

    Returns:
        rx.Component: Componente de Reflex con toda la información del curso

    Notas:
        - Utiliza on_mount con CourseState.load_course_from_url para cargar el curso desde la URL
        - Muestra spinner mientras CourseState.loading es True
        - El botón de inscripción solo aparece para estudiantes autenticados
        - Para usuarios no autenticados, muestra botón que redirige a login
        - Para instructores/admins, muestra botón deshabilitado con mensaje informativo
        - Incluye el diálogo de resultado de inscripción
        - Max width de 1200px para mejor legibilidad
    """
    return rx.vstack(
        navbar(),
        enrollment_result_dialog(),
        rx.container(
            rx.vstack(
                # Estado de carga
                rx.cond(
                    CourseState.loading,
                    rx.center(
                        rx.spinner(size="3"),
                        height="50vh",
                    ),
                ),
                # Mensaje de error del curso
                rx.cond(
                    CourseState.error != "",
                    rx.callout(
                        CourseState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Contenido del curso
                rx.cond(
                    (CourseState.course_title != "") & (CourseState.loading == False),
                    rx.vstack(
                        # SECCIÓN 1: HEADER CON IMAGEN Y INFO PRINCIPAL
                        rx.box(
                            rx.hstack(
                                # Imagen del curso
                                rx.box(
                                    rx.image(
                                        src=CourseState.course_thumbnail,
                                        width="100%",
                                        height="300px",
                                        object_fit="cover",
                                        border_radius="5px",
                                    ),
                                    width="400px",
                                    flex_shrink="0",
                                ),
                                # Info principal
                                rx.vstack(
                                    rx.heading(
                                        CourseState.course_title,
                                        size="9",
                                    ),
                                    rx.text(
                                        CourseState.course_description,
                                        size="4",
                                    ),
                                    rx.hstack(
                                        rx.badge(
                                            CourseState.course_level,
                                            color_scheme="purple",
                                            size="3",
                                        ),
                                        rx.text(
                                            f"${CourseState.course_price:.2f}",
                                            size="7",
                                            weight="bold",
                                            color="green",
                                        ),
                                        spacing="4",
                                    ),
                                    align_items="start",
                                    spacing="3",
                                    flex="1",
                                ),
                                spacing="6",
                                width="100%",
                                align_items="start",
                            ),
                            width="100%",
                            padding="6",
                            border_radius="lg",
                        ),
                        # SECCIÓN 2: INFORMACIÓN DEL INSTRUCTOR
                        rx.box(
                            rx.heading("Instructor", size="6", margin_bottom="3"),
                            rx.hstack(
                                rx.avatar(
                                    src=CourseState.instructor_avatar,
                                    fallback="IN",
                                    size="5",
                                ),
                                rx.vstack(
                                    rx.text(
                                        CourseState.instructor_name,
                                        weight="bold",
                                        size="4",
                                    ),
                                    rx.text(
                                        CourseState.instructor_email,
                                        size="2",
                                    ),
                                    rx.cond(
                                        CourseState.instructor_bio != "",
                                        rx.text(
                                            CourseState.instructor_bio,
                                            size="2",
                                            color="black",
                                        ),
                                    ),
                                    align_items="start",
                                    spacing="1",
                                ),
                            ),
                            width="100%",
                            padding="4",
                            margin_top="6",
                        ),
                        # SECCIÓN 3: ESTADÍSTICAS
                        rx.hstack(
                            rx.box(
                                rx.text("Estudiantes", size="2"),
                                rx.text(
                                    CourseState.students_count,
                                    size="6",
                                    weight="bold",
                                ),
                                padding="4",
                                text_align="center",
                                flex="1",
                            ),
                            rx.cond(
                                CourseState.average_rating > 0,
                                rx.box(
                                    rx.text("Rating", size="2"),
                                    rx.text(
                                        CourseState.average_rating,
                                        size="6",
                                        weight="bold",
                                    ),
                                    padding="4",
                                    text_align="center",
                                    flex="1",
                                ),
                            ),
                            rx.cond(
                                CourseState.total_reviews > 0,
                                rx.box(
                                    rx.text("Reviews", size="2"),
                                    rx.text(
                                        CourseState.total_reviews,
                                        size="6",
                                        weight="bold",
                                    ),
                                    padding="4",
                                    text_align="center",
                                    flex="1",
                                ),
                            ),
                            spacing="4",
                            width="100%",
                            margin_top="4",
                        ),
                        # SECCIÓN 4: CATEGORÍAS
                        rx.cond(
                            CourseState.categories.length() > 0,
                            rx.box(
                                rx.heading("Categorías", size="6", margin_bottom="3"),
                                rx.hstack(
                                    rx.foreach(
                                        CourseState.categories,
                                        lambda cat: rx.badge(cat, color_scheme="purple"),
                                    ),
                                    spacing="2",
                                    wrap="wrap",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        # SECCIÓN 5: LECCIONES
                        rx.cond(
                            CourseState.lessons.length() > 0,
                            rx.box(
                                rx.heading("Contenido del curso", size="6", margin_bottom="3"),
                                rx.vstack(
                                    rx.foreach(
                                        CourseState.lessons,
                                        lambda lesson: rx.box(
                                            rx.hstack(
                                                rx.heading(lesson["title"], size="4"),
                                                rx.spacer(),
                                                rx.badge(
                                                    f"{lesson['duration']} min",
                                                    color_scheme="blue",
                                                ),
                                            ),
                                            rx.text(
                                                lesson["content"],
                                                size="2",
                                                no_of_lines=2,
                                                margin_top="2",
                                            ),
                                            padding="3",
                                            width="100%",
                                            _hover={
                                                "background": rx.color("gray", 2),
                                            },
                                        ),
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        # SECCIÓN 6: REVIEWS
                        rx.cond(
                            CourseState.reviews.length() > 0,
                            rx.box(
                                rx.heading("Opiniones de estudiantes", size="6", margin_bottom="3"),
                                rx.vstack(
                                    rx.foreach(
                                        CourseState.reviews,
                                        lambda review: rx.box(
                                            rx.hstack(
                                                rx.text(review["student"], weight="bold", size="3"),
                                                rx.spacer(),
                                                rx.hstack(
                                                    rx.text("Rating:", size="2"),
                                                    rx.text(review["rating"], size="2", weight="bold"),
                                                    rx.text("/5", size="2"),
                                                    spacing="1",
                                                ),
                                            ),
                                            rx.text(
                                                review["comment"],
                                                size="2",
                                                margin_top="2",
                                            ),
                                            padding="3",
                                            width="100%",
                                        ),
                                    ),
                                    spacing="2",
                                    width="100%",
                                ),
                                width="100%",
                                padding="4",
                                margin_top="4",
                            ),
                        ),
                        # BOTÓN DE INSCRIPCIÓN / VER CURSO
                        rx.cond(
                            AuthState.is_user_student,
                            # Si es estudiante, mostrar botón según inscripción
                            rx.cond(
                                EnrollmentState.is_enrolled_in_current_course,
                                # Si está inscrito, mostrar botón "Ver curso"
                                rx.link(
                                    rx.button(
                                        rx.hstack(
                                            rx.icon("circle-play", size=20),
                                            rx.text("Ver Curso"),
                                            spacing="2",
                                        ),
                                        size="4",
                                        width="100%",
                                        margin_top="6",
                                        color_scheme="blue",
                                    ),
                                    href=f"/courses/{CourseState.current_course_id}/view",
                                    width="100%",
                                ),
                                # Si no está inscrito, mostrar botón de inscripción
                                rx.button(
                                    rx.cond(
                                        EnrollmentState.loading,
                                        rx.hstack(
                                            rx.spinner(size="3"),
                                            rx.text("Inscribiendo..."),
                                            spacing="2",
                                        ),
                                        "Inscribirse al curso",
                                    ),
                                    size="4",
                                    width="100%",
                                    margin_top="6",
                                    color_scheme="green",
                                    on_click=EnrollmentState.enroll_in_current_course,
                                    disabled=EnrollmentState.loading,
                                ),
                            ),
                            # Si no es estudiante
                            rx.cond(
                                AuthState.is_authenticated,
                                rx.button(
                                    "Solo estudiantes pueden inscribirse",
                                    size="4",
                                    width="100%",
                                    margin_top="6",
                                    color_scheme="gray",
                                    disabled=True,
                                ),
                                rx.link(
                                    rx.button(
                                        "Inicia sesión para inscribirte",
                                        size="4",
                                        width="100%",
                                        margin_top="6",
                                        color_scheme="blue",
                                    ),
                                    href="/login",
                                ),
                            ),
                        ),
                        spacing="4",
                        width="100%",
                        padding_y="8",
                    ),
                ),
                spacing="4",
                width="100%",
                on_mount=[CourseState.load_course_from_url, EnrollmentState.check_current_course_enrollment],
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
