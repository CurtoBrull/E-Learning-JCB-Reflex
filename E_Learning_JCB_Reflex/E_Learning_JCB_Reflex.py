"""E-Learning JCB Platform - Main application file."""

import reflex as rx
from rxconfig import config
from E_Learning_JCB_Reflex.services.course_service import get_all_courses
from E_Learning_JCB_Reflex.models.course import Course


class State(rx.State):
    """The app state."""

    courses: list[dict] = []
    loading: bool = False
    error: str = ""

    async def load_courses(self):
        """Load courses from database."""
        self.loading = True
        self.error = ""
        try:
            courses_list = await get_all_courses()
            # Convert Course objects to dictionaries for Reflex state
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
    """Component to display a single course card."""
    return rx.box(
        rx.vstack(
            rx.image(
                src=course.get("thumbnail", "/placeholder-course.jpg"),
                width="100%",
                height="200px",
                object_fit="cover",
                border_radius="lg",
            ),
            rx.heading(course.get("title", "Untitled Course"), size="6"),
            rx.text(
                course.get("description", "No description"),
                color="gray.600",
                size="2",
                no_of_lines=3,
            ),
            rx.hstack(
                rx.badge(course.get("level", "beginner"), color_scheme="blue"),
                rx.spacer(),
                rx.text(
                    f"${course.get('price', 0):.2f}",
                    font_weight="bold",
                    size="4",
                    color="green.600",
                ),
                width="100%",
            ),
            rx.text(
                f"By {course.get('instructor_name', 'Unknown')}",
                color="gray.500",
                size="1",
            ),
            spacing="3",
            align_items="start",
        ),
        padding="4",
        border_radius="lg",
        border="1px solid",
        border_color="gray.200",
        box_shadow="sm",
        _hover={
            "box_shadow": "md",
            "border_color": "blue.400",
            "cursor": "pointer",
        },
        transition="all 0.2s",
    )


def index() -> rx.Component:
    """Main page - E-Learning Platform."""
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.vstack(
            # Header
            rx.heading(
                "E-Learning JCB Platform",
                size="9",
                margin_bottom="2",
            ),
            rx.text(
                "Discover and enroll in amazing courses",
                size="5",
                color="gray.600",
                margin_bottom="8",
            ),
            # Load courses button
            rx.button(
                "Load Courses from Database",
                on_click=State.load_courses,
                size="3",
                color_scheme="blue",
                margin_bottom="6",
                loading=State.loading,
            ),
            # Error message
            rx.cond(
                State.error != "",
                rx.callout(
                    State.error,
                    icon="triangle_alert",
                    color_scheme="red",
                    margin_bottom="4",
                ),
            ),
            # Loading state
            rx.cond(
                State.loading,
                rx.spinner(size="3"),
            ),
            # Courses grid
            rx.cond(
                State.courses.length() > 0,
                rx.vstack(
                    rx.heading("Available Courses", size="7", margin_bottom="4"),
                    rx.grid(
                        rx.foreach(State.courses, course_card),
                        columns="3",
                        spacing="4",
                        width="100%",
                    ),
                    width="100%",
                ),
            ),
            # Empty state
            rx.cond(
                (State.courses.length() == 0) & (~State.loading) & (State.error == ""),
                rx.box(
                    rx.text(
                        "Click 'Load Courses' to fetch courses from MongoDB",
                        color="gray.500",
                    ),
                    padding="8",
                ),
            ),
            spacing="4",
            width="100%",
            padding_y="8",
        ),
        max_width="1200px",
    )


app = rx.App()
app.add_page(index)
