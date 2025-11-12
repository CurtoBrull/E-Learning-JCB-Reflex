"""E-Learning JCB Platform - Main application file."""

from pydoc import text
import reflex as rx
from rxconfig import config
from E_Learning_JCB_Reflex.services.course_service import get_all_courses
from E_Learning_JCB_Reflex.models.course import Course


class State(rx.State):
    """Estado de la aplicación."""

    courses: list[dict] = []
    loading: bool = False
    error: str = ""

    async def load_courses(self):
        """Cargar cursos desde la base de datos."""
        self.loading = True
        self.error = ""
        try:
            courses_list = await get_all_courses()
            # Convertir objetos Course a diccionarios para el estado de Reflex
            self.courses = [
                {
                    "title": course.title,
                    "description": course.description,
                    "instructor_name": course.instructor_name,
                    "price": course.price,
                    "level": course.level,
                    "thumbnail": course.thumbnail,
                }
                for course in courses_list
            ]
            if not self.courses:
                self.error = "No courses found in database"
        except Exception as e:
            self.error = f"Error loading courses: {str(e)}"
            print(f"Error in load_courses: {e}")
        finally:
            self.loading = False


def course_card(course: dict) -> rx.Component:
    """Componente de tarjeta de curso."""
    return rx.box(
        rx.vstack(
            rx.box(
                rx.image(
                    src=course.get("thumbnail", "/placeholder-course.jpg"),
                    width="100%",
                    height="200px",
                    object_fit="contain",
                ),
                width="100%",
                overflow="hidden",
                border_radius="lg",
                margin_bottom="3",
                padding_top="12px",
            ),
            rx.heading(
                course.get("title", "Untitled Course"),
                size="6",
                padding_x="4px",
                text_align="center",
                width="100%"
            ),
            rx.text(
                course.get("description", "No description"),
                color="gray.600",
                size="2",
                no_of_lines=3,
                padding_x="4px",
                width="100%"
            ),
            rx.hstack(
                rx.badge(
                    course.get("level", "beginner"),
                    color_scheme="blue",
                    margin="4px"
                ),
                rx.spacer(),
                rx.text(
                    f"${course.get('price', 0):.2f}",
                    font_weight="bold",
                    size="4",
                    color="green.600",
                    padding_x="4px"
                ),
                width="100%",
            ),
            rx.text(
                f"Instructor: {course.get('instructor_name', 'Unknown')}",
                color="gray.500",
                size="1",
                padding="4px",
            ),
            spacing="3",
            align_items="start",
            width="100%",
        ),
        border_radius="lg",
        border="1px solid",
        border_color="gray.200",
        box_shadow="sm",
        overflow="hidden",
        transition_property="box-shadow, border-color, transform",
        transition_duration="200ms",
        transition_timing_function="ease-in-out",
        _hover={
            "box_shadow": "md",
            "border_color": "blue.400",
            "transform": "translateY(-4px)",
            "cursor": "pointer",
        },
    )


def index() -> rx.Component:
    """ Página principal de la plataforma E-Learning JCB. """
    return rx.vstack(
        navbar(),
        rx.container(
            rx.vstack(
                # Header
                rx.heading(
                    "¡Bienvenido a E-Learning JCB!",
                    size="9",
                    margin_bottom="2",
                    text_align="center",
                    max_width="100%",
                ),
                rx.text(
                    "¡Aprende y Crece con nosotros!",
                    size="8",
                    color="gray.600",
                    margin_bottom="8",
                    text_align="center",
                ),
                rx.text(
                    "Descubre nuestros cursos online impartidos por expertos en programación, administración de sistemas y más. Aprende a tu ritmo, mejora tus habilidades y obtén certificaciones reconocidas en el sector IT.",
                    size="6",
                    color="gray.600",
                    margin_bottom="8",
                    text_align="center",
                ),
                # Mensaje de error
                rx.cond(
                    State.error != "",
                    rx.callout(
                        State.error,
                        icon="triangle_alert",
                        color_scheme="red",
                        margin_bottom="4",
                    ),
                ),
                # Estado de carga
                rx.cond(
                    State.loading,
                    rx.spinner(size="3"),
                ),
                # Cuadrícula de cursos
                rx.cond(
                    State.courses.length() > 0,
                    rx.vstack(
                        rx.heading("Cursos Populares", size="7", margin_bottom="4", text_align="center"),
                        rx.grid(
                            
                            rx.foreach(State.courses, course_card),
                            columns="3",
                            spacing="4",
                            width="100%",
                        ),
                        width="100%",
                        align_items="center",
                    ),
                ),
                # Estado vacío
                rx.cond(
                    (State.courses.length() == 0) & (~State.loading) & (State.error == ""),
                    rx.box(
                        rx.text(
                            "No hay cursos disponibles en este momento.",
                            color="gray.500",
                            text_align="center",
                        ),
                        padding="8",
                    ),
                ),
                spacing="4",
                width="100%",
                padding_y="8",
                align_items="center",
                on_mount=State.load_courses,
            ),
            width="100%",
            max_width="100%",
            padding_x="2rem",
        ),
        width="100%",
        spacing="0",
    )

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
                    navbar_link("Inicio", "/#"),
                    navbar_link("Cursos", "/#"),
                    navbar_link("Instructores", "/#"),
                    navbar_link("Contacto", "/#"),
                    navbar_link("Login", "/#"),
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
                            rx.menu.item("Home"),
                            rx.menu.item("About"),
                            rx.menu.item("Pricing"),
                            rx.menu.item("Contact"),
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

app = rx.App()
app.add_page(index)
