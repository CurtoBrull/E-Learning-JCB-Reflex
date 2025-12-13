"""Dashboard para estudiantes."""

import reflex as rx
from E_Learning_JCB_Reflex.components.navbar import navbar
from E_Learning_JCB_Reflex.components.protected import student_only
from E_Learning_JCB_Reflex.components.course_card import course_card
from E_Learning_JCB_Reflex.states.auth_state import AuthState
from E_Learning_JCB_Reflex.states.enrollment_state import EnrollmentState


def unenroll_confirmation_dialog() -> rx.Component:
    """Diálogo de confirmación para desinscripción."""
    return rx.alert_dialog.root(
        rx.alert_dialog.content(
            rx.alert_dialog.title("Confirmar Desinscripción"),
            rx.alert_dialog.description(
                f"¿Estás seguro de que deseas desinscribirte del curso '{EnrollmentState.course_to_unenroll_title}'? Perderás todo tu progreso.",
                size="3",
            ),
            rx.hstack(
                rx.alert_dialog.cancel(
                    rx.button(
                        "Cancelar",
                        variant="soft",
                        color_scheme="gray",
                        on_click=EnrollmentState.close_unenroll_dialog,
                    ),
                ),
                rx.alert_dialog.action(
                    rx.button(
                        "Desinscribirse",
                        color_scheme="red",
                    ),
                    on_click=EnrollmentState.confirm_unenroll,
                ),
                spacing="3",
                justify_content="end",
                width="100%",
            ),
        ),
        open=EnrollmentState.show_unenroll_dialog,
    )


def student_dashboard_content() -> rx.Component:
    """Contenido del dashboard del estudiante."""
    return rx.vstack(
        navbar(),
        unenroll_confirmation_dialog(),
        rx.container(
            rx.vstack(
                # Header
                rx.hstack(
                    rx.vstack(
                        rx.heading(
                            f"Bienvenido, {AuthState.user_name}",
                            size="9",
                        ),
                        rx.text(
                            "Panel de estudiante",
                            size="5",
                            color=rx.color("gray", 11),
                        ),
                        align_items="start",
                        spacing="2",
                    ),
                    rx.spacer(),
                    rx.badge(
                        "Estudiante",
                        color_scheme="blue",
                        size="3",
                    ),
                    width="100%",
                    align_items="center",
                ),
                # Mensajes de error y éxito
                rx.cond(
                    EnrollmentState.error != "",
                    rx.callout(
                        EnrollmentState.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                rx.cond(
                    EnrollmentState.success != "",
                    rx.callout(
                        EnrollmentState.success,
                        icon="check-circle",
                        color_scheme="green",
                        margin_bottom="4",
                    ),
                ),
                # Estadísticas
                rx.grid(
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("book-open", size=24, color=rx.color("blue", 9)),
                                rx.spacer(),
                                rx.badge(
                                    EnrollmentState.total_enrolled_courses.to_string(),
                                    size="2",
                                    color_scheme="blue",
                                ),
                            ),
                            rx.text("Cursos Inscritos", size="3", weight="bold"),
                            rx.text(
                                "Total de cursos en los que estás inscrito",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("check-circle", size=24, color=rx.color("green", 9)),
                                rx.spacer(),
                                rx.badge(
                                    EnrollmentState.completed_courses.to_string(),
                                    size="2",
                                    color_scheme="green",
                                ),
                            ),
                            rx.text("Cursos Completados", size="3", weight="bold"),
                            rx.text(
                                "Cursos que has terminado exitosamente",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("clock", size=24, color=rx.color("orange", 9)),
                                rx.spacer(),
                                rx.badge(
                                    f"{EnrollmentState.average_progress}%",
                                    size="2",
                                    color_scheme="orange",
                                ),
                            ),
                            rx.text("Progreso General", size="3", weight="bold"),
                            rx.text(
                                "Promedio de progreso en todos tus cursos",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    rx.card(
                        rx.vstack(
                            rx.hstack(
                                rx.icon("trophy", size=24, color=rx.color("yellow", 9)),
                                rx.spacer(),
                                rx.badge(
                                    EnrollmentState.completed_courses.to_string(),
                                    size="2",
                                    color_scheme="yellow",
                                ),
                            ),
                            rx.text("Certificados", size="3", weight="bold"),
                            rx.text(
                                "Certificados obtenidos",
                                size="2",
                                color=rx.color("gray", 10),
                            ),
                            spacing="3",
                            align_items="start",
                        ),
                    ),
                    columns="4",
                    spacing="4",
                    width="100%",
                ),
                # Mis Cursos Inscritos
                rx.card(
                    rx.vstack(
                        rx.hstack(
                            rx.heading("Mis Cursos", size="6"),
                            rx.spacer(),
                            rx.link(
                                rx.button(
                                    "Explorar Más Cursos",
                                    variant="soft",
                                    size="2",
                                ),
                                href="/courses",
                            ),
                            width="100%",
                        ),
                        rx.divider(),
                        # Mostrar cursos inscritos o mensaje de vacío
                        rx.cond(
                            EnrollmentState.enrolled_courses.length() > 0,
                            rx.grid(
                                rx.foreach(
                                    EnrollmentState.enrolled_courses,
                                    lambda course: rx.box(
                                        rx.vstack(
                                            # Imagen con altura fija
                                            rx.box(
                                                rx.link(
                                                    rx.image(
                                                        src=course["thumbnail"],
                                                        alt=course["title"],
                                                        width="100%",
                                                        height="100%",
                                                        object_fit="cover",
                                                        border_radius="8px 8px 0 0",
                                                    ),
                                                    href=f"/courses/{course['id']}",
                                                ),
                                                height="150px",
                                                width="100%",
                                                overflow="hidden",
                                            ),
                                            # Título con altura fija
                                            rx.box(
                                                rx.heading(
                                                    course["title"],
                                                    size="5",
                                                    no_of_lines=2,
                                                ),
                                                min_height="3.5rem",
                                                width="100%",
                                                padding_x="4",
                                                padding_top="3",
                                            ),
                                            # Info de progreso y nivel
                                            rx.hstack(
                                                rx.text(
                                                    f"Progreso: {course['progress']}%",
                                                    size="2",
                                                    color=rx.color("gray", 10),
                                                ),
                                                rx.spacer(),
                                                rx.badge(
                                                    course["level"],
                                                    color_scheme="blue",
                                                ),
                                                width="100%",
                                                padding_x="4",
                                            ),
                                            # Barra de progreso
                                            rx.box(
                                                rx.progress(
                                                    value=course["progress"],
                                                    max=100,
                                                    width="100%",
                                                ),
                                                width="100%",
                                                padding_x="4",
                                            ),
                                            # Espaciador para empujar los botones hacia abajo
                                            rx.spacer(),
                                            # Botones alineados al fondo
                                            rx.hstack(
                                                rx.link(
                                                    rx.button(
                                                        "Continuar",
                                                        size="2",
                                                        variant="soft",
                                                        color_scheme="blue",
                                                    ),
                                                    href=f"/courses/{course['id']}",
                                                ),
                                                rx.button(
                                                    "Desinscribirse",
                                                    size="2",
                                                    variant="soft",
                                                    color_scheme="red",
                                                    on_click=lambda _, c_id=course["id"], c_title=course["title"]: EnrollmentState.open_unenroll_dialog(c_id, c_title),
                                                ),
                                                width="100%",
                                                justify_content="space-between",
                                                padding="4",
                                            ),
                                            spacing="3",
                                            align_items="start",
                                            width="100%",
                                            height="100%",
                                        ),
                                        border=f"1px solid {rx.color('gray', 6)}",
                                        border_radius="8px",
                                        height="420px",
                                        display="flex",
                                        flex_direction="column",
                                    ),
                                ),
                                columns="3",
                                spacing="4",
                                width="100%",
                            ),
                            # Mensaje cuando no hay cursos inscritos
                            rx.center(
                                rx.vstack(
                                    rx.icon("book-open", size=40, color=rx.color("gray", 8)),
                                    rx.text(
                                        "No tienes cursos inscritos",
                                        size="4",
                                        color=rx.color("gray", 10),
                                    ),
                                    rx.text(
                                        "Explora nuestro catálogo y comienza a aprender",
                                        size="3",
                                        color=rx.color("gray", 9),
                                    ),
                                    rx.link(
                                        rx.button(
                                            "Explorar Cursos",
                                            size="3",
                                            color_scheme="blue",
                                        ),
                                        href="/courses",
                                    ),
                                    spacing="3",
                                    align_items="center",
                                    padding="4em",
                                ),
                            ),
                        ),
                        spacing="4",
                        width="100%",
                    ),
                ),
                # Acciones rápidas
                rx.card(
                    rx.vstack(
                        rx.heading("Acciones Rápidas", size="6"),
                        rx.divider(),
                        rx.grid(
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("search", size=20),
                                        rx.text("Explorar Cursos"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/courses",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("book-open", size=20),
                                        rx.text("Mis Inscripciones"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/student/enrollments",
                                width="100%",
                            ),
                            rx.link(
                                rx.button(
                                    rx.hstack(
                                        rx.icon("user", size=20),
                                        rx.text("Mi Perfil"),
                                        spacing="2",
                                    ),
                                    variant="soft",
                                    size="3",
                                    width="100%",
                                ),
                                href="/profile",
                                width="100%",
                            ),
                            columns="3",
                            spacing="4",
                            width="100%",
                        ),
                        spacing="4",
                        width="100%",
                    ),
                ),
                spacing="6",
                width="100%",
                padding_y="4",
                on_mount=EnrollmentState.load_enrolled_courses,
            ),
            max_width="1400px",
            padding_x=["4", "6", "8"],
            margin_x="auto",
        ),
        width="100%",
        spacing="0",
    )


def student_dashboard_page() -> rx.Component:
    """Página de dashboard del estudiante con protección."""
    return student_only(student_dashboard_content())
